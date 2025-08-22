import pandas as pd
from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["indeed", "linkedin", "naukri", "zip_recruiter", "google"],
    search_term="software engineer fresher",
    google_search_term="software engineer fresher jobs near India since yesterday",
    location="India",
    results_wanted=20,
    hours_old=72,
    country_indeed="India",
)

print(f"Found {len(jobs)} jobs")
print(jobs.head())

jobs.to_excel("jobs.xlsx", index=False, engine="openpyxl")
