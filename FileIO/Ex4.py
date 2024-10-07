import csv

# Read the 1,000 lines of taxi data from the taxi_1000.csv file and 
# calculate the total of all fares, the average of those fares, and the 
# maximum trip distance (based on the Trip Miles field) for fares greater
# than $10 only.

with open("taxi_1000.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    totalFares = 0
    averageFare = 0
    maxDistance = 0
    numRows = 0
    for line in csv_reader:
        if (numRows > 0):
            tripFare = float(line[10])
            distance = float(line[5])
            if tripFare > 10:
                totalFares += tripFare
                if distance > maxDistance:
                    maxDistance = distance
        numRows += 1

    print(f"We read {numRows} rows from the file.")
    print(f"The total of all fares above $10 was {round(totalFares,2)}")
    print(f"The average fare for fares above $10 was {round(totalFares/numRows,2)}")
    print(f"The maximum distance for fares above $10 was {maxDistance} miles")