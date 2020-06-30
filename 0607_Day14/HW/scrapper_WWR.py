import requests
from bs4 import BeautifulSoup

URL = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={{job_name}}"


def extract_job(html):
  title = html.find("a").find("h2").find("span", {"class":"title"})
  company = html.find("a").find("h2").find("span", {"class":"company"})
  link = html.find("a")["href"]
  return {
      'title': title,
      'company': company,
      'link': link
  }


def extract_jobs():
  jobs = []
  result = requests.get(f"{URL}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("li", {"class":"feature"})
  for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs 


def get_jobs():
    jobs = extract_jobs()
    return jobs