import os
import requests

print("Welcome to IsItDown.py!")
print("Please write a URL or URLs you want to check. (separated by comma)")

sites = input("")
sites_split = sites.split(',')
sites_strip = []

for site in sites_split:
  sites_strip.append(site.strip())

for urls in sites_strip:
  try:
    if "https://" not in urls or "http://" not in urls:
      url = "https://" + urls
    if "https://" in urls or "http://" in urls:
      url = urls
    r = requests.get(f"{url}")
    if r.status_code == 200:
      print(f"{url} is up!")
    else:
      print(f"{url} is down!")
  except:
    print(f"{urls} is not a valid URL")
  
print("Do you want to start over? y/n")
answer1 = input("")
if answer1 == "y":
  os.system("clear")
  os.system("python main.py")
elif answer1 == "n":
  print("k, bye!")
