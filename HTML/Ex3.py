# Parse a web site to extract specific contents, using BeautifulSoup
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
itm_url = "https://shidler.hawaii.edu/itm/people"

itm_html = urllib.request.urlopen(itm_url)

html_to_parse = BeautifulSoup(itm_html, "html.parser")
pretty_html = html_to_parse.prettify()

lines = pretty_html.splitlines()
num_lines_to_print = 10

# Print the first few lines
for line in lines[:num_lines_to_print]:
    print(line)

# Find just the ITM people
List_of_itm_people = html_to_parse.find_all('h2', class_="title")

# Create a list of the people retrieved
itm_people = []
for element in List_of_itm_people:
    itm_people.append(element.text)
    print(element.text)
    
print("number of itm people found: " + str(len(itm_people)))
unique_itm_people = list(set(itm_people))
print("number of unique itm people found: " + str(len(unique_itm_people)))
