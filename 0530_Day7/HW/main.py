import os
import requests
from bs4 import BeautifulSoup
import math

os.system("clear")

url = "https://www.iban.com/currency-codes"

countries = []

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
  items = row.find_all("td")
  name = items[0].text
  code = items[2].text
  if name and code:
    if name != "No universal currency":
      country = {
        'name': name.capitalize(),
        'code': code
      }
      countries.append(country)

def format_currency(a, b):
  trans = f"https://transferwise.com/gb/currency-converter/{country1['code']}-to-krw-rate?amount={a}"
  request2 = requests.get(trans)
  soup2 = BeautifulSoup(request2.text, "html.parser")
  section = soup2.find("section")
  won = section.find("input", {"class":"js-TargetAmount"})["value"]
  print(country1['code'],a, " is ₩", math.floor(float(won)))

def convert():
  global country1, country2
  country1 = countries[choice1]
  country2 = countries[choice2]
  print(f"How many {country1['code']} do you want to convert to {country2['code']}?")
  try:
    number = int(input())
    format_currency(number, "KRW")
  except ValueError:
    print("That wasn't a number.")
    convert()

def ask_another():
  print("Now choose another country")
  try:
    global choice2
    choice2 = int(input("#: "))
    if choice2 > len(countries):
      print("Choose a number from the list.")
      ask_another()
    else:
      country = countries[choice2]
      print(country['name'])
      print("")
      convert()
  except ValueError:
    print("That wasn't a number.")
    ask_another()

def ask_you():
  try:
    global choice1
    choice1 = int(input("#: "))
    if choice1 > len(countries):
      print("Choose a number from the list.")
      ask_you()
    else:
      country = countries[choice1]
      print(country['name'])
      print("")
      ask_another()
  except ValueError:
    print("That wasn't a number.")
    ask_you()

print("Welcom to CurrencyConvert PRO 2000")
print("")
for index, country in enumerate(countries):
  print(f"#{index} {country['name']}")

print("")
print("Where are you from? Choose a country by number")
print("")

ask_you()

# print(format_currency(5000, "KRW", locale="ko_KR"))