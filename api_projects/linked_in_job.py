import requests
from password import LINKED_IN_JOB_SEARCH_API_KEY

class LinkedInJobSearch:
    def __init__(self):
        self.endpoint = "https://linkedin-job-api.p.rapidapi.com/job/search"
        self.headers = {
            "x-rapidapi-key": LINKED_IN_JOB_SEARCH_API_KEY,
            "x-rapidapi-host": "linkedin-job-api.p.rapidapi.com"
        }

    def search_jobs(self, keyword, location, remote_filter):
        querystring = {
            "keyword": keyword,
            "location": location,
            "remoteFilter": remote_filter,
            "page": "1"
        }

        response = requests.get(self.endpoint, headers=self.headers, params=querystring)

        if response.status_code == 200:
            data = response.json()["data"]
            jobs = []
            for d in data:
                title = d["title"]
                company = d["companyDetails"]["name"]
                location = d["companyDetails"]["location"]
                job_url = d["jobPostingUrl"]
                description = d["description"]
                jobs.append({
                    "title": title,
                    "company": company,
                    "location": location,
                    "url": job_url,
                    "description": description
                })
            return jobs

        else:
            return {"error": "Failed to fetch data"}






