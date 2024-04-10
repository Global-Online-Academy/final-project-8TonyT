import pandas as pd
from collections import Counter
from collections import defaultdict
from bokeh.plotting import figure, output_file
from bokeh.io import save, show
from bokeh.models import ColumnDataSource
from bokeh.models import Label
import csv

with open('rows.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

