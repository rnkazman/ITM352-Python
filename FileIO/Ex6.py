# Read a file of questions and answers and save it as a dictionary

import json

# Open the JSON file and load its content
with open('quiz.json', 'r') as file:
    data = json.load(file)

# Now 'data' is a dictionary containing the JSON data
print(data)