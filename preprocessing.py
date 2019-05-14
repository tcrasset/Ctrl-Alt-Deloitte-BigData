import pandas as pd
import csv


df = pd.read_csv('Devices.csv', delimiter=';', error_bad_lines=False, encoding='latin1')

# Drop redundant first columns; same as second
df.drop(columns= ['SiteName'], inplace=True)
print("Column name and number of NANs of clean df",df.isna().sum())

clean_df = df[[c for c in df if df[c].isnull().sum() < len(df)/10]]
print("Column name and number of NANs of clean df",clean_df.isna().sum())

print("Columns removed from df after cleaning",[c for c in df.columns if c not in clean_df.columns])
print("Length of dirty Devices", len(df))
print("Length of cleaned Devices", len(clean_df))

print("Length of dirty Devices columns", len(df.columns))
print("Length of cleaned Devices columns", len(clean_df.columns))

print("Unique value numbers per column")


# df[[c for c in df if df.apply(pd.Series.nunique) < 20]]


clean_df.to_csv("Devices_clean.csv", index=False)

