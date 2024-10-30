# Open up a URL and print some content from it.
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://shidler.hawaii.edu/itm/people"

# Open the web page
print (f"Opening {url}...")
webpage = urllib.request.urlopen(url)

# iterate through each line in the webpage and search for the <title>:
for line in webpage:
    line = line.decode('utf-8')

    # Modify the following line to specify critera
    if '<h2' in line:
        print(line)
