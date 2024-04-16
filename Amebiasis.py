import pandas as pd
from collections import Counter
from collections import defaultdict
from bokeh.plotting import figure, show, output_file
from bokeh.io import save, show
from bokeh.models import ColumnDataSource
from bokeh.models import Label
import csv


file_path = "rows.csv"
y_values = []

selected_lines = []


with open(file_path, 'r') as file:

    csv_reader = csv.reader(file)
    

    for row in csv_reader:

        if "Amebiasis" in row[0] and "California" in row[1] and "Total" in row[3]:
            y_values.append(str(row[4])) 

output_file("Cases of Amebiasis during 2001-2014 in California.html")
years = ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"]

p = figure(x_range=years, height=350, title="Cases of Amebiasis during 2001-2014 in California", toolbar_location=None, tools="")


colors = "red"
p.vbar(x=years, top=y_values, width=0.5, color=colors)


show(p)

