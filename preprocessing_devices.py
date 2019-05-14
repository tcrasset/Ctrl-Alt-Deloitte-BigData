import pandas as pd


df = pd.read_csv('Devices.csv', delimiter=';', error_bad_lines=False, warn_bad_lines=False, encoding='latin1')

# Drop redundant columns
df.drop(columns= ['SiteName', 'BiosDate'], inplace=True)

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

# Export whole Devices file to csv
clean_df.to_csv("Devices_clean.csv", index=False)

# Count the occurences of the different values and save to csv
clean_df['ConfigName'].value_counts().reset_index().to_csv('ConfigNameCount.csv')
clean_df['Manufacturer'].value_counts().reset_index().to_csv('ManufacturerCount.csv')
clean_df['MainboardType'].value_counts().reset_index().to_csv('MainboardTypeCount.csv')
