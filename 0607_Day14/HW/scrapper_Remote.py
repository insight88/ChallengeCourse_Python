import requests
from bs4 import BeautifulSoup

URL = f"https://remoteok.io/remote-{{job_name}}-jobs"


def extract_job(html):
  title = html.find("td", {"class":"company position company_and_position"}).find("h2").text
  company = html.find("td", {"class":"company position company_and_position"}).find("h3").text
  link = html.find("td", {"class":"company"}).find("a")["href"]
  return {
      'title': title,
      'company': company,
      'link': link
  }


def extract_jobs():
  jobs = []
  result = requests.get(f"{URL}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("tr", {"class":"job"})
  for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs 


def get_jobs():
    jobs = extract_jobs()
    return jobs