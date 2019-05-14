import pandas as pd
import csv


df = pd.read_csv('Devices.csv', delimiter=';', header=None, error_bad_lines=False, encoding='latin1')


df.dropna(thresh=5,inplace=True)
df.to_csv("Devices_clean.csv")
