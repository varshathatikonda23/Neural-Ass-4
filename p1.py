import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'data.csv'
data_frame = pd.read_csv(file_path)

# Show basic statistical description about the data
print(data_frame.describe())

# Check for null values and replace them with the mean
data_frame.fillna(data_frame.mean(), inplace=True)

# Select all four columns and aggregate the data using: min, max, count, mean
columns_to_aggregate = data_frame.columns  # Use all columns
aggregated_data = data_frame[columns_to_aggregate].agg(['min', 'max', 'count', 'mean'])
print(aggregated_data)

# Filter the dataframe to select the rows with calories values between 500 and 1000
filtered_data_frame_1 = data_frame[(data_frame['Calories'] >= 500) & (data_frame['Calories'] <= 1000)]

# Filter the dataframe to select the rows with calories values > 500 and pulse < 100
filtered_data_frame_2 = data_frame[(data_frame['Calories'] > 500) & (data_frame['Pulse'] < 100)]

# Create a new dataframe modified_data_frame without the "Maxpulse" column
modified_data_frame = data_frame.drop('Maxpulse', axis=1)

# Delete the "Maxpulse" column from the main data_frame dataframe
data_frame.drop('Maxpulse', axis=1, inplace=True)

# Convert the datatype of Calories column to int
data_frame['Calories'] = data_frame['Calories'].astype(int)

# Create a scatter plot for Duration and Calories
data_frame.plot.scatter(x='Duration', y='Calories', title='Scatter Plot: Duration vs Calories')
plt.show()