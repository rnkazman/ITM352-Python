# Apply a style to a scatterplot
import pandas as pd
import matplotlib.pyplot as plt

# Use the seaborn visualization style
#plt.style.use('ggplot')
#plt.style.use('dark_background')
plt.style.use('fivethirtyeight')

trips_df = pd.read_json('../Trips from area 8.json')

trip_miles_gt_0 = trips_df[['trip_miles', 'fare']].query('trip_miles > 0')
fare_series = trip_miles_gt_0.fare
trip_miles = trip_miles_gt_0.trip_miles

fig = plt.figure()
plt.plot(trip_miles, fare_series, marker = 'o', linestyle = "none",
              label = "Taxi Fare", alpha = 0.3)
plt.title('Fares by Taxi Trip Miles')
plt.xlabel('Miles')
plt.ylabel('Dollars')
plt.legend()
plt.savefig("FaresXmiles-538.png", dpi = 300)
plt.show()