"""This file handles the loading into the database part of the project


https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
https://datatofish.com/pandas-dataframe-to-sql/

"""
# Module Imports
import mariadb
import sys
import pandas as pd


### load data into database ###

###Stage
def load_yahoo_gold():
    df_tw = pd.read_csv("../data/stage/yahoo_gold_stage.csv")

    for index, row in df_tw.iterrows():
        cur.execute("INSERT INTO cip_project.yahoo_gold_stage (date,open,high,low,close,adjusted_close,volume,percent_change,name,source) VALUES(?,?,?,?,?,?,?,?,?,?)",
        (row.date, row.open, row.high, row.low, row.close, row.adjusted_close, row.volume, row.percent_change, row["name"], row.source))

def load_yahoo_oil():
    df_tw = pd.read_csv("../data/stage/yahoo_oil_stage.csv")

    for index, row in df_tw.iterrows():
        cur.execute("INSERT INTO cip_project.yahoo_oil_stage (date,open,high,low,close,adjusted_close,volume,percent_change,name,source) VALUES(?,?,?,?,?,?,?,?,?,?)",
        (row.date, row.open, row.high, row.low, row.close, row.adjusted_close, row.volume, row.percent_change, row["name"], row.source))

def load_yahoo_nasdaq():
    df_tw = pd.read_csv("../data/stage/yahoo_nasdaq_stage.csv")

    for index, row in df_tw.iterrows():
        cur.execute("INSERT INTO cip_project.yahoo_nasdaq_stage (date,open,high,low,close,adjusted_close,volume,percent_change,name,source) VALUES(?,?,?,?,?,?,?,?,?,?)",
        (row.date, row.open, row.high, row.low, row.close, row.adjusted_close, row.volume, row.percent_change, row["name"], row.source))

##Source - all values are strings
def load_yahoo_gold_src():
    df_tw = pd.read_csv("../data/src/yahoo_gold_src.csv")

    for index, row in df_tw.iterrows():
        cur.execute("INSERT INTO cip_project.yahoo_gold_src (date,symbol,open,high,low,close,adjusted_close,volume) VALUES(?,?,?,?,?,?,?,?)",
        (row["date"], row["symbol"], row["open"], row["high"], row["low"], row["close"], row["adjusted_close"], row["volume"]))

def load_yahoo_oil_src():
    df_tw = pd.read_csv("../data/src/yahoo_oil_src.csv")

    for index, row in df_tw.iterrows():
        cur.execute("INSERT INTO cip_project.yahoo_oil_src (date,symbol,open,high,low,close,adjusted_close,volume) VALUES(?,?,?,?,?,?,?,?)",
        (row["date"], row["symbol"], row["open"], row["high"], row["low"], row["close"], row["adjusted_close"], row["volume"]))

def load_yahoo_nasdaq_src():
    df_tw = pd.read_csv("../data/src/yahoo_nasdaq_src.csv")

    for index, row in df_tw.iterrows():
        cur.execute("INSERT INTO cip_project.yahoo_nasdaq_src (date,symbol,open,high,low,close,adjusted_close,volume) VALUES(?,?,?,?,?,?,?,?)",
        (row["date"], row["symbol"], row["open"], row["high"], row["low"], row["close"], row["adjusted_close"], row["volume"]))


try:
    # Connect to MariaDB
    conn = mariadb.connect(
        user="admin",
        password="password",
        host="127.0.0.1",
        port=3306,
        database="cip_project",
        autocommit=True  # automatically commit SQL statements

    )
    # Get Cursor
    cur = conn.cursor()

    # Load data
    load_yahoo_gold()
    load_yahoo_oil()
    load_yahoo_nasdaq()
    load_yahoo_gold_src()
    load_yahoo_oil_src()
    load_yahoo_nasdaq_src()

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
