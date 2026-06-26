from datetime import datetime
import requests

import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import sqlite3
url='https://web.archive.org/web/20230908091635%20/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs=["Name","MC_USD_Billion"]
csv_path1="Largest_banks_data.csv"
csv_path2="exchange_rate.csv"
db_name="Banks.db"
table_name="Largest_banks"

def log_progress(message):
    format_time="%Y-%h_%d-%H:%M:%S"
    now=datetime.now()
    time_now=now.strftime(format_time)
    with open ("code_log.txt","a")as file:
        file.write(time_now +" : "+message+"\n")
       
def extract(url, table_attribs):
    df=pd.DataFrame(columns=table_attribs)
    result=requests.get(url).text
    data=BeautifulSoup(result,"html.parser")
    table=data.find("table")
    tbody=table.find("tbody")
    rows=tbody.find_all("tr")
    for row in rows :
        cells=row.find_all("td")
        if(len(cells)<2):
            continue
        Name=cells[1].text.strip()
        MC_USD_Billion=cells[2].text.strip()[:-1]
        df=pd.concat([df,pd.DataFrame({"Name":[Name],"MC_USD_Billion":[MC_USD_Billion]})],ignore_index=True)
    df["MC_USD_Billion"]=df["MC_USD_Billion"].astype(float)
    return df

def transform(df, csv_path):
    data_frame_info=pd.read_csv(csv_path)
    for row in data_frame_info.itertuples(index=False,name="row"):
        df["MC_"+row.Currency+"_Billion"]=np.round(df["MC_USD_Billion"]*row.Rate,2)
    return df
def load_to_csv(df, output_path):
    df.to_csv(output_path)
def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name,sql_connection,if_exists="replace",index=False)
def run_query(query_statement, sql_connection):
    df=pd.read_sql(query_statement,sql_connection)
    print(df)

log_progress("Preliminaries complete. Initiating ETL process")
df=extract(url,table_attribs)
log_progress("Data extraction complete. Initiating Transformation process")
print(df)

df=transform(df,csv_path2)
print(df)
print("market capitalization of the 5th largest bank in billion EUR")
print(df['MC_EUR_Billion'][4])
log_progress("Data transformation complete. Initiating Loading process")

load_to_csv(df,csv_path1)
log_progress("Data saved to CSV file")

conn=sqlite3.connect(db_name)
log_progress("SQL Connection initiated")
load_to_db(df,conn,table_name)

log_progress("Data loaded to Database as a table, Executing queries")
print("SELECT * FROM Largest_banks")

run_query(f"select * from {table_name}",conn)
print("SELECT AVG(MC_GBP_Billion) FROM Largest_banks")
run_query(f"select AVG(MC_GBP_Billion) from {table_name}",conn)
print('SELECT Bank name from Largest_banks LIMIT 5')
run_query(f"select  Name from {table_name} LIMIT 5",conn)
log_progress("Process Complete")
conn.close()
log_progress("Server Connection closed")
