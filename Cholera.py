import pandas as pd
from collections import Counter
from collections import defaultdict
from bokeh.plotting import figure, show, output_file
from bokeh.io import save, show
from bokeh.models import ColumnDataSource
from bokeh.models import Label
import csv

# Define the file path
file_path = "rows.csv"
y_values = []
# Initialize a list to store the selected lines
selected_lines = []

# Open the CSV file
with open(file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Iterate over each line in the CSV file
    for row in csv_reader:
        # Check if the words "Amebiasis", "California", and "Total" are present in the current line
        if "Cholera" in row[0] and "California" in row[1] and "Total" in row[3]:
            y_values.append(str(row[4]))  # Convert to float if the values are numeric

# Output to a standalone HTML file
output_file("Cases of Cholera during 2001-2014 in California.html")
years = ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"]
# Create a new plot with a title and axis labels
p = figure(x_range=years, height=350, title="Cases of Cholera during 2001-2014 in California", 
           toolbar_location=None, tools="")

# Add bars
colors="green"
p.vbar(x=years, top=y_values, width=0.5,color=colors)

# Show the plot
show(p)


# Now, selected_lines contains only the lines that contain "Amebiasis", "California", and "Total"
# You can further process or analyze these lines as needed
