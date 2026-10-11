import json
from datetime import date
FILE_NAME = "jobs.json"
try:
with open(FILE_NAME, "r") as f:
return json.load(f)
except:
return[]
def save_jobs(jobs):
with open(FILE_NAME, "w") as f:
json.dump(jobs, f, indent=2)
def add_applications():
jobs = load_jobs()
company = input("Company Name:")
role = input("Role:")
new_job = {
"company": company,
"role": role,
"date": str(date.today()),
"status": "Applied"
}
jobs.append(new_jobs)
save_jobs(jobs)
print(f"\n Successfully added {company} to tracker!")
print(f"Total applications: {len(jobs)}")
if __name__ =="__main__":
add_applications()
