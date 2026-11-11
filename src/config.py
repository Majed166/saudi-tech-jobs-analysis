# keywords used to pick tech jobs and to find skills in the job text
# I built these lists by reading through the titles and fixing wrong matches

# track -> regex patterns that are checked against the job title (lowercase)
TRACKS = {
    "Data & AI": [
        r"\bdata (scien|analy|engineer|architect|govern|quality|manage|steward|warehouse|integration|platform|modell?er)",
        r"\b(senior |staff |lead |junior )?data analyst", r"\bmachine learning\b", r"\bml engineer", r"\bai\b",
        r"artificial intelligence", r"business intelligence", r"\bbi (developer|analyst|engineer|specialist)",
        r"power ?bi", r"\betl\b", r"big data", r"\bnlp\b", r"computer vision", r"data engineering",
        r"محلل بيانات", r"عالم بيانات", r"مهندس بيانات", r"ذكاء اصطناعي",
    ],
    "ERP & Business Systems": [
        r"\bsap\b", r"\boracle\b", r"\berp\b", r"dynamics", r"salesforce", r"\bodoo\b", r"servicenow",
        r"business analyst", r"system(s)? analyst", r"\bcrm\b",
    ],
    "Software Development": [
        r"software (engineer|developer|development|architect)", r"\bdeveloper\b", r"\bprogrammer\b",
        r"full.?stack", r"front.?end", r"back.?end", r"\bweb (developer|designer)", r"\bmobile (developer|engineer|app)",
        r"\bandroid\b", r"\bios\b", r"\bflutter\b", r"\breact\b", r"\b\.net\b", r"\bjava\b", r"\bpython\b", r"\bphp\b",
        r"مطور", r"مبرمج", r"برمجيات",
    ],
    "Cybersecurity": [
        r"cyber", r"information security", r"\bsoc\b", r"security (analyst|engineer|architect|consultant|specialist|operations)",
        r"penetration", r"\bgrc\b", r"threat", r"أمن سيبراني", r"الأمن السيبراني", r"أمن المعلومات",
    ],
    "Cloud & DevOps": [
        r"devops", r"\bcloud\b", r"site reliability", r"\bsre\b", r"kubernetes", r"\baws\b", r"\bazure\b",
        r"platform engineer", r"infrastructure engineer",
    ],
    "Networks & IT Support": [
        r"network (engineer|administrator|technician|specialist|architect|security)", r"\bit (support|technician|administrator|admin|specialist|engineer|officer|helpdesk|help desk|systems?|infrastructure|operations|service|desk|executive|coordinator|analyst)",
        r"system(s)? administrator", r"help ?desk", r"desktop support", r"technical support", r"\bnoc\b",
        r"data ?cent(er|re)", r"تقنية المعلومات", r"تقنية معلومات", r"دعم فني", r"شبكات",
    ],
    "QA & Testing": [r"\bqa\b", r"quality assurance (engineer|analyst|tester)", r"\btest(er|ing)? (engineer|analyst|automation)", r"\bsdet\b", r"software test"],
    "UI/UX & Product": [r"\bux\b", r"\bui\b", r"product (manager|owner|designer)", r"user experience", r"scrum master"],
    "IT Management": [
        r"\bit (manager|director|head|lead|project|program|governance)", r"\bcto\b", r"\bcio\b", r"enterprise architect",
        r"solutions? architect", r"technical (project|program|delivery) manager", r"digital transformation",
        r"مدير تقنية",
    ],
}

# titles that match the patterns above but are not really tech jobs
NOT_TECH = [
    r"sales", r"account (executive|manager)", r"business develop", r"مندوب", r"مطور الاعمال", r"مطور أعمال",
    r"nurse", r"data entry", r"مدخل بيانات", r"recruit", r"instructor", r"teacher", r"civil", r"mechanical",
    r"marketing", r"real estate", r"property developer", r"franchise",
    r"\bqc\b", r"inspect", r"document controller", r"\bcnc\b", r"program developer", r"retinal",
    r"power generation", r"asset management", r"customer support", r"go-to-market", r"trainer",
]

# skill name -> regex, checked against title + description + skills text
SKILLS = {
    "SQL": r"\bsql\b", "Python": r"\bpython\b", "Java": r"\bjava\b(?!script)", "JavaScript": r"\bjavascript\b|\bjs\b",
    "TypeScript": r"\btypescript\b", "C#/.NET": r"c#|\.net\b|\bdotnet\b|asp\.net", "C++": r"c\+\+", "PHP": r"\bphp\b",
    "React": r"\breact(\.?js)?\b", "Angular": r"\bangular\b", "Node.js": r"\bnode(\.?js)?\b", "HTML/CSS": r"\bhtml\b|\bcss\b",
    "Flutter": r"\bflutter\b", "Swift/iOS": r"\bswift\b|\bios\b", "Kotlin/Android": r"\bkotlin\b|\bandroid\b",
    "REST APIs": r"\brest(ful)?\b|\bapis?\b", "Git": r"\bgit\b|\bgithub\b|\bgitlab\b",
    "Docker": r"\bdocker\b", "Kubernetes": r"\bkubernetes\b|\bk8s\b", "CI/CD": r"ci/cd|\bjenkins\b|continuous integration",
    "AWS": r"\baws\b|amazon web services", "Azure": r"\bazure\b", "GCP": r"\bgcp\b|google cloud",
    "Linux": r"\blinux\b|\bunix\b", "Power BI": r"power ?bi", "Tableau": r"\btableau\b", "Excel": r"\bexcel\b",
    "Machine Learning": r"machine learning|\bml\b", "Deep Learning": r"deep learning|tensorflow|pytorch",
    "GenAI/LLM": r"\bllms?\b|generative ai|\bgenai\b|\bgpt\b|large language", "Spark/Hadoop": r"\bspark\b|\bhadoop\b|databricks",
    "ETL/Data Pipelines": r"\betl\b|data pipelines?|\bairflow\b", "NoSQL": r"\bnosql\b|mongodb|\bredis\b|cassandra",
    "Oracle": r"\boracle\b", "SAP": r"\bsap\b", "Agile/Scrum": r"\bagile\b|\bscrum\b",
    "Networking": r"\btcp/ip\b|\bccna\b|\bccnp\b|\bcisco\b|\bfirewalls?\b|\brouting\b", "SIEM/SOC": r"\bsiem\b|\bsplunk\b|\bsoc\b",
    "Security Certs": r"\bcissp\b|\bcism\b|\bceh\b|\boscp\b|security\+", "ISO 27001/NCA": r"iso ?27001|\bnca\b|\bnist\b",
    "Windows Server/AD": r"windows server|active directory", "ITIL": r"\bitil\b", "Testing/Automation": r"\bselenium\b|test automation|\bcypress\b",
    "Figma": r"\bfigma\b", "Arabic language": r"\barabic\b", "English language": r"\benglish\b",
}

CITY_EN = {
    "الرياض": "Riyadh", "جدة": "Jeddah", "الدمام": "Dammam", "الخبر": "Khobar", "الشرقية": "Eastern Province",
    "المدينه المنوره": "Madinah", "المدينة المنورة": "Madinah", "القطيف": "Qatif", "الجبيل": "Jubail", "تبوك": "Tabuk",
    "مكة المكرمة": "Makkah", "أبها": "Abha", "الظهران": "Dhahran", "ينبع": "Yanbu", "الأحساء": "Al Ahsa",
    "الهفوف": "Al Ahsa", "حائل": "Hail", "بريدة": "Buraydah", "الطائف": "Taif", "جازان": "Jazan", "نجران": "Najran",
    "Unknown": "Not stated",
}
