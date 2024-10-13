import pandas as pd

# List of individuals' ages
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]

# Convert the list to a DataFrame
df = pd.DataFrame(ages, columns=['Age'])

# Summarize the DataFrame using the describe method
summary = df.describe()

print(summary)