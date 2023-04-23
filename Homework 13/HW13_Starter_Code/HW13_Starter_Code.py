# ITP 216 Homework 13
# Fall 2022

import pandas as pd
import matplotlib.pyplot as plt


def main():
    # reading in the dataset
    df = pd.read_csv("weather.csv")

    # removing rows of data where the observed temp is null
    df = df[df["TOBS"].notnull()]

    # making a column for year: allows us to easily get the last 10 years
    df["YEAR"] = df["DATE"].str[0:4]
    years_list = list(df["YEAR"].unique())

    # making a column for month: allows us to group by month
    df["MONTH_DAY"] = df["DATE"].str[-5:]
    df = df[df['MONTH_DAY'] != '02-29']  # drop leap years
    month_days_list = list(df["MONTH_DAY"].unique())

    df.sort_values(inplace=True, by='MONTH_DAY')
    print(df[['DATE', 'YEAR', 'MONTH_DAY', 'TOBS']])

    # list of months to label the x-axis of both graphs
    month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


if __name__ == '__main__':
    main()
