# Read from the survey_1000.csv file using csv_reader from the csv module
# Calculate average, max, min values for REALINC, if values are > 0.
# Report the # of values > 0.
import csv

line_number = 0
total_RealInc = 0
max_RealInc = 0
min_RealInc = 99999999999   # Choose a very large number for min income
num_values = 0
with open("survey_1000.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    for line in csv_reader:
        if (line_number > 0):
            RealInc = float(line[5456])
            if (RealInc > 0):
                num_values += 1
                total_RealInc += RealInc
                if (RealInc < min_RealInc):
                    min_RealInc = RealInc
                if (RealInc > max_RealInc):
                    max_RealInc = RealInc
        line_number += 1
   
print (f"Number of non-zero values: {num_values}")
print (f"Average RealInc: ${round(total_RealInc / num_values, 2)}")
print (f"Min Realinc: ${round(min_RealInc,2)}  Max RealInc: ${round(max_RealInc,2)}")
