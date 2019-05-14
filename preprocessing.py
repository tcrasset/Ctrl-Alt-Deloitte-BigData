import pandas as pd
import csv


df = pd.read_csv('Devices.csv', delimiter=';', header=None, error_bad_lines=False, encoding='latin1')



print(len(df))
print(df.isna().sum())

clean_df = df[[c for c in df if df[c].isnull().sum() < len(df)/2]]

print(clean_df.isna().sum())

clean_df.to_csv("Devices_clean.csv")

