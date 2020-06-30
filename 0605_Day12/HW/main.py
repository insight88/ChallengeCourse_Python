import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

# """
# When you try to scrape reddit make sure to send the 'headers' on your request.
# Reddit blocks scrappers so we have to include these headers to make reddit think
# that we are a normal computer and not a python script.
# How to use: requests.get(url, headers=headers)
# """

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


# """
# All subreddits have the same url:
# i.e : https://reddit.com/r/javascript
# You can add more subreddits to the list, just make sure they exist.
# To make a request, use this url:
# https://www.reddit.com/r/{subreddit}/top/?t=month
# This will give you the top posts in per month.
# """

subreddits = [
  "baseball",
  "soccer",
  "football",
  "tennis",
  "golf",
  "WWE",
  "running",
  "fitness",
]

def scrap_post(subreddit="", selects=[]):
  url = f"https://www.reddit.com/r/{subreddit}/top/?t=month"
  request_subreddit = requests.get(url, headers=headers)
  soup = BeautifulSoup(request_subreddit.text, "html.parser")

  total_posts = soup.find("div", {"class", "rpBJOHq2PR60pnwJlUyP0"})
  votes_post = total_posts.find_all("div", {"class","_1rZYMD_4xY3gRcSS3p8ODO"})
  title_post = total_posts.find_all("h3", {"class","_eYtD2XCVieq6emjKBH3m"})
  url = total_posts.find_all("a", {"class","SQnoC3ObvgnGjWt90zD9Z"})

  
  for n in enumerate(url):
    votes = votes_post[n].string
    # if "k" in votes:
    #   votes = votes.replace("k", "")
    #   votes = int(float(votes))*1000
    title = title_post[n].string
    link = "https://www.reddit.com" + url[n]['href']
    selects.append({"vote":votes, "title":title,"link":link, 
    "subreddit":subreddit})

app = Flask("DayEleven")

@app.route("/")
def home():
  add_args = request.args.get("add")
  print(add_args)
  if add_args is None:
    return render_template("home.html", subreddits=subreddits)
  check_url = f"https://reddit.com/r/{add_args}"
  requests_check = requests.get(check_url, headers=headers)
  if requests_check.status_code == 200:
    subreddits.append(f"{add_args}")
    return render_template("home.html", subreddits=subreddits)
  elif requests_check.status_code != 200:
    if "r/" in add_args:
      return render_template("error.html", error_no = "1")
    else:
      return render_template("error.html", error_no = "2")


@app.route("/read")
def read():
  selects = []
  selected = []
  selected_args = request.args
  
  for subreddit in subreddits:
    if subreddit in selected_args:
      selected.append(subreddit)
    scrap_post(subreddit, selects)

  selects.sort(key=lambda select:select["vote"], reverse=True)
  return render_template("read.html", posts=selects, selected = selected_args)

app.run(host="0.0.0.0")