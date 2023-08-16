import pandas as pd

# Load JSON data with specified encoding
with open('book.json', 'r', encoding='utf-8') as json_file:
    data = pd.read_json(json_file)

# Specify Excel output file
excel_file = 'output.xlsx'

# Write the data to Excel
data.to_excel(excel_file, index=False)

print(f"JSON data has been imported and saved to '{excel_file}'")
