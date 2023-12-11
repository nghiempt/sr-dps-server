import os
import csv
import pandas as pd
from make_final_dataset_only_prompt import READ_DATA_SAFETY
from make_final_dataset_only_prompt import READ_PRIVACY_POLICY
import json
import asyncio

async def extract_ds_pp(input_csv_path, output_csv_path):
    with open(input_csv_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        new_data = []
        for index, row in enumerate(csv_reader):
            print("========== " + str(index + 1) + " times ==========")
            preprocess_data_safety = await READ_DATA_SAFETY().scrape_link(row['data_safety_link'])
            data_safety = json.dumps(READ_DATA_SAFETY().formated_data(preprocess_data_safety))
            # privacy_policy = json.loads(READ_PRIVACY_POLICY().generate_result(row['privacy_policy_link']))
            new_row = [row['app_id'], data_safety, ""]
            new_data.append(new_row)

    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['app_id', 'app_data_safety', 'app_privacy_policy'])
        csv_writer.writerows(new_data)

input_directory = '../dataset/formated_data/app.csv'
output_file_path = 'dspp.csv'
asyncio.run(extract_ds_pp(input_directory, output_file_path))