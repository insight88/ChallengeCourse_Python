import os
import requests
from bs4 import BeautifulSoup
import re

os.system("clear")
url = "https://www.iban.com/currency-codes"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
tbody = soup.find("tbody")
names = tbody.find_all("td")
countries = []

print("Hello! Please choose a country by number:")

number = 0

for name in names:

  countries.append(name.string)
  country_name = countries[number]

  if number%4 == 0:
    print(f"# {int(number/4)} {country_name}")
    number += 1
  else:
    number += 1

def inputs():

  try:
    input_number = int(input("#: "))
    if input_number >= 0 and input_number <= 267:
      print(f"You choose {countries[input_number*4]}")
      print(f"The currency code is {countries[input_number*4+2]}") 
    elif input_number > 267 or input_number < 0:
      print("Choose a number from the list")
      inputs()

  except: 
    print("That wasn't a number")
    inputs()

inputs()