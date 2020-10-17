"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""


from flask import Flask, render_template, request, redirect
from scrapper_Remote import get_jobs as get_Remote_jobs
from scrapper_WWR import get_jobs as get_WWR_jobs
from scrapper_SO import get_jobs as get_SO_jobs

Remote_jobs = get_Remote_jobs()
WWR_jobs = get_WWR_jobs()
SO_jobs = get_SO_jobs
jobs = Remote_jobs + WWR_jobs + SO_jobs

app = Flask("RemoteJobs")

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/result")
def result():
  return render_template("result.html")

app.run(host="0.0.0.0")