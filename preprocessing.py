import pandas as pd
import csv


df = pd.read_csv('Devices.csv', delimiter=';', error_bad_lines=False, encoding='latin1')

# Drop redundant columns
df.drop(columns= ['SiteName', 'BiosDate'], inplace=True)
print("Column name and number of NANs of clean df",df.isna().sum())

# Rename values
df.replace({"ConfigName": {'Canada_1':'Canada'}})

Type_dict = {
    'SIEDP':'siedp',
    'Snow Inventory Agent for Linux':'Snow Agent Linux',
    'Snow Agent - Linux' : 'Snow Agent Linux',
    'Snow Inventory Client for Linux' : 'Snow Agent Linux',

    'Snow Inventory Client for Windows' : 'Snow Agent Windows',
    'Snow Agent - Windows' : 'Snow Agent Windows',
    'Snow Inventory Client for Windows - 64 bit' : 'Snow Agent Windows',

    'Windows (64-bit)' : 'Windows',
}
df.replace({"Type": Type_dict}, inplace=True)

MainboardType_dict = {

    'Multiple processors': 'Multi Processor',
    'Single processor' : 'Single Processor'
}
df.replace({"MainboardType": MainboardType_dict}, inplace=True)


clean_df = df[[c for c in df if df[c].isnull().sum() < len(df)/10]]
print("Column name and number of NANs of clean df",clean_df.isna().sum())

print("\nColumns removed from df after cleaning\n",[c for c in df.columns if c not in clean_df.columns])
print("\nLength of dirty Devices\n", len(df))
print("\nLength of cleaned Devices\n", len(clean_df))

print("\nLength of dirty Devices columns\n", len(df.columns))
print("\nLength of cleaned Devices columns\n", len(clean_df.columns))

print("\nUnique value numbers per column\n")

for col in clean_df.columns:
    if len(clean_df[col].unique()) < 20:
        print(col)
        print(clean_df[col].unique().tolist())




# df[[c for c in df if df.apply(pd.Series.nunique) < 20]]


clean_df.to_csv("Devices_clean.csv", index=False)

