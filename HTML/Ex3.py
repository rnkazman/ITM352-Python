from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
itm_url = "https://shidler.hawaii.edu/itm/people"

itm_html = urllib.request.urlopen(itm_url)

html_to_parse = BeautifulSoup(itm_html, "html.parser")

# Modify the following line of code to create a list of audiobooks found in the webpage:
List_of_itm_people = html_to_parse.find_all('h2', class_="title")

itm_people = []
for element in List_of_itm_people:
    itm_people.append(element.text)
    print(element.text)
    
print("number of itm people found: " + str(len(itm_people)))
