import plotly.express as px
import csv
import numpy as np


def plot_figure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x="Days Present", y="Marks In Percentage")
        fig.show()


def getDataSource(data_path):
    daysPresent = []
    percentage = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            daysPresent.append(float(row['Days Present']))
            percentage.append(float(row['Marks In Percentage']))

    return {'x': daysPresent, 'y': percentage}


def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation : ", correlation[0, 1])


def setup():
    data_path = "Student Marks vs Days Present.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plot_figure(data_path)
