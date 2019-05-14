import pandas as pd
import csv


df = pd.read_csv('Devices.csv', delimiter=';', error_bad_lines=False, encoding='latin1')
print("Length of dirty Devices", len(df))
# print(df.isna().sum())

clean_df = df[[c for c in df if df[c].isnull().sum() < len(df)/2]]

print([c for c in df.columns if c not in clean_df.columns])
print("Length of cleaned Devices", len(clean_df))
# print(clean_df.isna().sum())

clean_df.to_csv("Devices_clean.csv", index=False)

