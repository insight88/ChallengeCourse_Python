import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"


def extract_job(html):
  result = requests.get(alba_url)
  soup = BeautifulSoup(result.text, "html.parser")
  URL = soup.find("li", {"class":"first impact"} or {"class":"impact"}).find("a")["href"]
  result2 = requests.get(f"{URL}")
  html = BeautifulSoup(result2.text, "html.parser")

  place = html.find("td", {"class":"local first"}).get_text
  title = html.find("td", {"class":"title"}).find("span")
  time = html.find("td", {"class":"data"}).find("span")
  pay = html.find("td", {"class":"pay"}).find("span").get_text
  date = html.find("td", {"class":"regDate last"}).get_text

  return {
    'place': place,
    'title': title, 
    'time': time,
    'pay': pay,
    'date': date
  }


def extract_jobs():
  jobs = []
  result = requests.get(alba_url)
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("li", {"class":"impact"} or {"class":"first impact"})
  for result in results:
    job = extract_job(result)
    jobs.append(job)
  return jobs


def get_jobs():
  jobs = extract_jobs()
  return jobs


def save_to_file(jobs):
  result = requests.get(alba_url)
  soup = BeautifulSoup(result.text, "html.parser")
  find_company = soup.find("span", {"class":"company"})
  company = find_company.get_text(strip=True)
  file = open(f"{company}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["place", "title", "time", "pay", "date"])
  for job in jobs:
    print(list(job.values()))
    writer.writerow(list(job.values()))
  return


jobs = get_jobs()
save_to_file(jobs)