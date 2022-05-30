import plotly.express as px
import csv
import numpy as np


def plot_figure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x="Coffee in ml", y="sleep in hours")
        fig.show()


def getDataSource(data_path):
    coffee_in_ml = []
    sleep_hours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_in_ml.append(float(row['Coffee in ml']))
            sleep_hours.append(float(row['sleep in hours']))

    return {'x': coffee_in_ml, 'y': sleep_hours}


def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation : ", correlation[0, 1])


def setup():
    data_path = "cups of coffee vs hours of sleep.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plot_figure(data_path)
