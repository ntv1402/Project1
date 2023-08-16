import pandas as pd

# Read JSON data
with open('population.json', 'r') as json_file:
    data = pd.read_json(json_file)

# Export data to Excel
data.to_excel('population.xlsx', index=False)
