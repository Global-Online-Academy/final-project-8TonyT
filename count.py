import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('rows.csv')

# Get the unique values in the first column
unique_values = df.iloc[:, 0].unique()

# Count the number of unique values
num_unique_values = len(unique_values)

# Print out the unique values
print("Unique values in the first column:")
for value in unique_values:
    print(value)

# Print the count of unique values
print("\nNumber of unique values:", num_unique_values)
