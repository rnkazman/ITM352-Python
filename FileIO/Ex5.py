import json

# Save the dictionary of quiz questions as a JSON file
QUESTIONS = {
     "What is the airspeed of an unladen swallow in miles/hr": 
     ["12", "8", "11", "15"],
     "What is the capital of Texas": 
     ["Austin", "San Antonio", "Dallas", "Waco"],
      "The Last Supper was painted by which artist": 
     ["Da Vinci", "Rembrandt", "Picasso", "Michelangelo"]
}

# Specify the file name
filename = 'quiz.json'

# Open the file in write mode and save the dictionary as JSON
with open(filename, 'w') as file:
    json.dump(QUESTIONS, file, indent=4)

print(f"Data has been written to {filename}")