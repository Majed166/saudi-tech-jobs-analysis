"""
Step 2: answer the questions I care about and save charts + small result tables.

  1. which tech track has the most openings?
  2. which skills are asked for the most (overall and per track)?
  3. how many years of experience do they want? how many jobs are open to juniors?
  4. where are the jobs?

run:  python src/analyze.py   (after clean.py)
"""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("data/tech_jobs.csv")
n = len(df)
BLUE = "#2f6f9f"
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})


def barh(series, title, xlabel, fname, color=BLUE):
    series = series.sort_values()
    fig, ax = plt.subplots(figsize=(8, 0.42 * len(series) + 1.5))
    ax.barh(series.index, series.values, color=color)
    for i, v in enumerate(series.values):
        ax.text(v, i, f" {v:g}", va="center")
    ax.set_title(title, loc="left", fontweight="bold")
    ax.set_xlabel(xlabel)
    fig.tight_layout()
    fig.savefig(f"figures/{fname}", dpi=150)
    plt.close(fig)


# ---------- 1. tracks ----------
tracks = df["track"].value_counts()
tracks.rename("jobs").to_csv("results/jobs_per_track.csv")
barh(tracks, f"Tech job postings by track (n={n})", "number of postings", "01_tracks.png")

# ---------- 2. skills ----------
# one row per (job, skill)
sk = df.assign(skill=df["skills_found"].fillna("").str.split(";")).explode("skill")
sk = sk[sk["skill"] != ""]
# languages are not really "tech skills", I report them separately
lang = ["Arabic language", "English language"]
tech_sk = sk[~sk["skill"].isin(lang)]

top = (tech_sk["skill"].value_counts() / n * 100).round(1)
top.rename("pct_of_jobs").to_csv("results/skills_overall.csv")
barh(top.head(15), "Top 15 skills (% of tech postings that mention it)", "% of postings", "02_top_skills.png")

# top 5 skills inside each track
rows = []
for track, g in tech_sk.groupby("track"):
    size = (df["track"] == track).sum()
    for skill, c in g["skill"].value_counts().head(5).items():
        rows.append({"track": track, "skill": skill, "pct_of_track_jobs": round(c / size * 100, 1)})
per_track = pd.DataFrame(rows)
per_track.to_csv("results/top_skills_per_track.csv", index=False)

# heatmap: tracks x most common skills
common = top.head(14).index
heat = (tech_sk[tech_sk["skill"].isin(common)].groupby(["track", "skill"]).size().unstack(fill_value=0))
heat = heat.div(df["track"].value_counts(), axis=0).mul(100).reindex(columns=common).loc[tracks.index]
fig, ax = plt.subplots(figsize=(11, 5))
im = ax.imshow(heat.values, cmap="Blues", aspect="auto", vmin=0, vmax=70)
ax.set_xticks(range(len(common)), common, rotation=40, ha="right")
ax.set_yticks(range(len(heat)), heat.index)
for i in range(heat.shape[0]):
    for j in range(heat.shape[1]):
        v = heat.values[i, j]
        if v >= 1:
            ax.text(j, i, f"{v:.0f}", ha="center", va="center", fontsize=9, color="white" if v > 40 else "black")
ax.set_title("Skill demand inside each track (% of the track's postings)", loc="left", fontweight="bold")
for s in ax.spines.values():
    s.set_visible(False)
fig.tight_layout()
fig.savefig("figures/03_skills_by_track.png", dpi=150)
plt.close(fig)

# ---------- 3. experience ----------
order = ["Intern / Fresh grad", "Junior", "Mid", "Senior", "Lead / Manager", "Not stated"]
levels = df["level"].value_counts().reindex(order).fillna(0).astype(int)
levels.rename("jobs").to_csv("results/levels.csv")
barh(levels[::-1], "Seniority level of the postings", "number of postings", "04_levels.png")

yrs = df.dropna(subset=["min_years"])
exp = yrs.groupby("track")["min_years"].agg(["count", "median"]).sort_values("median")
exp["pct_2_years_or_less"] = yrs.groupby("track")["min_years"].apply(lambda s: round((s <= 2).mean() * 100, 1))
exp.to_csv("results/experience_per_track.csv")

# ---------- 4. cities ----------
city = df[df["city_en"] != "Not stated"]["city_en"].value_counts()
city.rename("jobs").to_csv("results/cities.csv")
barh(city.head(8), f"Where the jobs are (only postings with a city, n={city.sum()})", "number of postings", "05_cities.png")

# ---------- print a short summary ----------
print(f"tech postings: {n}")
print("\ntracks:\n", tracks.to_string())
print("\ntop skills (% of postings):\n", top.head(15).to_string())
print("\nlanguages (% of postings):\n", (sk[sk['skill'].isin(lang)]['skill'].value_counts() / n * 100).round(1).to_string())
print("\ntop 5 per track:\n", per_track.to_string(index=False))
print("\nlevels:\n", levels.to_string())
print(f"\nmin years stated in {len(yrs)} postings, median = {yrs['min_years'].median()}")
print(f"asking for 2 years or less: {(yrs['min_years'] <= 2).mean() * 100:.1f}%")
print("\nexperience per track:\n", exp.to_string())
print("\ncities:\n", city.to_string())
print("\nremote:\n", df["remote"].value_counts().to_string())
