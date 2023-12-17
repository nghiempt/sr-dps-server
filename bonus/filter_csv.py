# read column 'privacy_policy_content' in file csv

import csv
import os
import sys
import re
import pandas as pd

# read csv file
def read_csv_file(file_name):
    df = pd.read_csv(file_name, encoding='utf-8')
    return df

# read column 'privacy_policy_content' in file csv
def read_column_in_csv(file_name, column_name):
    df = read_csv_file(file_name)
    return df[column_name]

print(read_column_in_csv('/Users/nghiempt/Observation/sr-dps/sr-dps-server/bonus/android_app_info.csv', 'privacy_policy_content'))