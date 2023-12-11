import os
import csv
import pandas as pd

def extract_columns(input_directory, output_csv_path):
    id_counter = 1
    aggregated_data = []

    
    for filename in os.listdir(input_directory):
        if filename.endswith(".csv"):
            input_csv_path = os.path.join(input_directory, filename)

            with open(input_csv_path, 'r', newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.DictReader(csvfile)

                app_count = 0
                for row in csv_reader:
                    if app_count == 50:
                        break
                    aggregated_data.append((str(id_counter), row['pkg_name']))
                    id_counter += 1
                    app_count += 1

    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['id', 'pkg_name'])
        csv_writer.writerows(aggregated_data)


def extract_columns_one_file(input_csv_path, output_csv_path):
    with open(input_csv_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        data = [(str(i + 1), row['category']) for i, row in enumerate(csv_reader)]

    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['id', 'category'])
        csv_writer.writerows(data)

# input_directory = '../dataset/quick_download'
# output_file_path = 'full_app_pkg.csv'
# extract_columns(input_directory, output_file_path)


# df = pd.read_csv('app_750.csv')

# Remove blank
# df_cleaned = df.dropna(subset=['app_name'])
# df_cleaned['app_id'] = range(1, len(df_cleaned) + 1)

# Remove duplicate
# df_cleaned = df.drop_duplicates(subset=['category'], keep='first')
# df_cleaned['id'] = range(1, len(df_cleaned) + 1)

#Remove unessessary string
# df['category'] = df['category'].str.replace('Play Pass', '', regex=True)

#Replace category with id
# app_df = pd.read_csv('app_750.csv')
# category_df = pd.read_csv('category.csv')
# category_mapping = dict(zip(category_df['category'], category_df['id']))
# app_df['category'] = app_df['category'].map(category_mapping)

# app_df.to_csv('app.csv', index=False)