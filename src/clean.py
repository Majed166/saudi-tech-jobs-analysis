"""
Step 1: take the raw Bayt listings, keep only the tech jobs and add some columns
(track, skills, years of experience, level, city in English).

run:  python src/clean.py
"""
import re
import pandas as pd
from config import TRACKS, NOT_TECH, SKILLS, CITY_EN

RAW = "data/raw/saudi_arabia.csv"
OUT = "data/tech_jobs.csv"


def find_track(title):
    title = str(title).lower()
    for bad in NOT_TECH:
        if re.search(bad, title):
            return None
    # first track that matches wins, so the order in config.py matters
    for track, patterns in TRACKS.items():
        for p in patterns:
            if re.search(p, title):
                return track
    return None


def find_skills(text):
    text = str(text).lower()
    found = [name for name, p in SKILLS.items() if re.search(p, text)]
    return ";".join(found)


def min_years(row):
    # bayt has a structured field but most rows are empty there,
    # so if it is empty I look for "3+ years" style text in the description
    m = re.search(r"الحد الأدنى: (\d+)", str(row["num_of_exp_years"]))
    if m:
        return int(m.group(1))
    m = re.search(r"(\d{1,2})\s*(?:\+|-\s*\d{1,2}|to \d{1,2})?\s*\+?\s*(?:years?|yrs?)", str(row["text"]).lower())
    if m and int(m.group(1)) <= 20:
        return int(m.group(1))
    return None


def find_level(row):
    t = str(row["title"]).lower()
    if re.search(r"intern|trainee|co-?op|tamheer|graduate|fresh|متدرب|تدريب", t):
        return "Intern / Fresh grad"
    if re.search(r"junior|\bjr\b|associate|entry", t):
        return "Junior"
    if re.search(r"manager|head|director|lead|principal|chief|مدير", t):
        return "Lead / Manager"
    if re.search(r"senior|\bsr\b|staff|expert", t):
        return "Senior"
    y = row["min_years"]
    if pd.isna(y):
        return "Not stated"
    if y <= 1:
        return "Junior"
    if y <= 4:
        return "Mid"
    return "Senior"


def main():
    df = pd.read_csv(RAW, low_memory=False)
    print("raw rows:", len(df))

    df = df.drop_duplicates(subset=["title", "company_name", "description"])
    print("after removing duplicates:", len(df))

    df["track"] = df["title"].apply(find_track)
    tech = df[df["track"].notna()].copy()
    print("tech jobs:", len(tech))

    tech["text"] = tech["title"].fillna("") + " " + tech["description"].fillna("") + " " + tech["skills"].fillna("")
    tech["skills_found"] = tech["text"].apply(find_skills)
    tech["min_years"] = tech.apply(min_years, axis=1)
    tech["level"] = tech.apply(find_level, axis=1)
    tech["city_en"] = tech["city"].map(CITY_EN).fillna("Other")
    tech["month"] = pd.to_datetime(tech["date"]).dt.strftime("%Y-%m")

    cols = ["title", "company_name", "month", "city_en", "remote", "track", "level", "min_years", "skills_found"]
    tech[cols].to_csv(OUT, index=False)
    print("saved", OUT)


if __name__ == "__main__":
    main()
