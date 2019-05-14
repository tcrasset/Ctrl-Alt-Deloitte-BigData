import pandas as pd
import csv


df = pd.read_csv('Devices.csv', delimiter=';', error_bad_lines=False, encoding='latin1')

# Drop redundant columns
df.drop(columns= ['SiteName', 'BiosDate'], inplace=True)

# Unique values per column
# print('==================================================================')
# print("Unique values per column\n")
# for col in df.columns:
#     if len(df[col].unique()) < 20:
#         print(col)
#         print(df[col].unique().tolist())
# print('==================================================================')

# # Column name and number of NANs of dirty df
# print('==================================================================')
# print("Column name and number of NANs of dirty df",df.isna().sum())
# print('==================================================================')


# Rename values so that they match
df.replace({"ConfigName": {'Canada_1':'Canada', 'Australia Agent Win': 'Australia'}}, inplace=True)

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
    'Multi ProcessorPCI ACPI AGP' :'Multi Processor',
    'Multi ProcessorPCI ACPI': 'Multi Processor',
    'Multi ProcessorPCI ACPI USB AGP': 'Multi Processor',
    'Single processor' : 'Single Processor',
}
df.replace({"MainboardType": MainboardType_dict}, inplace=True)
df['MainboardType'] = df['MainboardType'].fillna("NA")

Manufacturer_dict = {
'VMware, Inc.' : 'VMWare Inc.',
'VMWare, Inc.' : 'VMWare Inc.',
'VMWare Inc' : 'VMWare Inc.',
'VMware Inc.' : 'VMWare Inc.',
'IBM CORPORATION' : 'IBM',
'HP' : 'Hewlett-Packard',
'LENOVO': 'Lenovo',

}
df.replace({"Manufacturer": Manufacturer_dict}, inplace=True)

# Create clean df, drop if more than 'percentage_to_drop' % missing values
percentage_to_drop = 10
clean_df = df[[c for c in df if df[c].isnull().sum() < len(df) * percentage_to_drop/100]]
# print("Column name and number of NANs of clean df",clean_df.isna().sum())

# print("\nColumns removed from df after cleaning\n",[c for c in df.columns if c not in clean_df.columns])

# print("\nLength of dirty Devices\n", len(df))
# print("\nLength of cleaned Devices\n", len(clean_df))

# print("\nLength of dirty Devices columns\n", len(df.columns))
# print("\nLength of cleaned Devices columns\n", len(clean_df.columns))


# # Unique value numbers per column
# print("\nUnique value numbers per column\n")

# for col in clean_df.columns:
#     if len(clean_df[col].unique()) < 100:
#         print(col)
#         print(clean_df[col].unique().tolist())

clean_df.to_csv("Devices_clean.csv", index=False)

print(clean_df['ConfigName'].value_counts())

# Count the occurences of the different values and save to csv
clean_df['ConfigName'].value_counts().reset_index().to_csv('ConfigNameCount.csv')
clean_df['Manufacturer'].value_counts().reset_index().to_csv('ManufacturerCount.csv')
clean_df['MainboardType'].value_counts().reset_index().to_csv('MainboardTypeCount.csv')
