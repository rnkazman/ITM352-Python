import urllib.request
url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"

# Open the web page
webpage = urllib.request.urlopen(url)

# iterate through each line in the webpage and search for the <title>:
for line in webpage:
    line = line.decode('utf-8')

    # Modify the following line to specify critera
    if '<title>' in line:
        print(line)
