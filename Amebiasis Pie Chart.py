from collections import Counter
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('rows.csv')

# Extract data from the fourth column
data_column = df.iloc[:, 3]

# Count the frequency of each unique value
data_counts = Counter(data_column)

# Prepare data for pie chart
data_labels = list(data_counts.keys())
data_values = list(data_counts.values())

# Create a pie chart
output_notebook()  # For Jupyter Notebook, use output_file() for HTML file
pie_chart = figure(title="Pie Chart", toolbar_location=None,
                   tools="hover", tooltips="@data_label: @data_value", 
                   x_range=(-0.5, 1.0))

pie_chart.wedge(x=0, y=1, radius=0.4,
                start_angle=0, end_angle=[2 * pi * (v / sum(data_values)) for v in data_values],
                color=viridis(len(data_labels)), legend_label=data_labels)

# Show the pie chart
show(pie_chart)
