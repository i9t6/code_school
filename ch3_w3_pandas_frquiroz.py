#!/home/paco/py3/bin/python
#Python 3.8.5
import pandas as pd 
from datetime import date
import matplotlib.pyplot as plt

my_csv_file = "cisco_networks_failure_logs_dump.csv"
df = pd.read_csv(my_csv_file, parse_dates=['date'])

print("\n 1.Basic information and shape of the Data Frame")
print(" ----------- Info ----------- ")
print(df.info())
print("\n ----------- Shape ----------- ")
print(df.shape)

print("\n\n 2.How many Severity P1 affectations with outage happened between December 2020 and January 2021 per region per customer?")
df_2 =  df[ ( df["outage"] == True ) &  ( df["severity"] == "P1") & (df["date"]>=pd.Timestamp("2020-12-1")) & (df["date"]<=pd.Timestamp("2021-1-31"))].groupby(['Region','customer'])["severity"].count()
print(df_2)


print("\n\n 3.How  many  PSIRTs  caused  affectations  during the last  year  at  the  customer Wordpedia, grouped by region, device family and psirt name?")
df_3 = df[(df["customer"] == "Wordpedia") & (df["date"]<=pd.Timestamp("2020-12-31")) ].groupby(['Region','device_family','psirts_current_ios'])['psirts_current_ios'].count()
print(df_3)


print("\n\n 4.Which  device  families  from  customer Zooxo had affectations  in  2021  per region?")
df_4 = df[(df["customer"] == "Zooxo") &  (df["date"]>=pd.Timestamp("2021-1-1")) ].groupby(['Region','device_family'])['device_family'].count()
print(df_4)

print("\n\n5.For the latter, plot a pie chart, adding a title and percentages")
print('\n image saved "image.png" file in')
plt.figure()
df_4.head(5).plot(kind='pie',title='Zooxo',legend=True,figsize=(10, 10),autopct='%1.1f%%')
#plt.show()
plt.savefig("image.png")

