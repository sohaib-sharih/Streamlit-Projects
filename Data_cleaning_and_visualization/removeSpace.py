import pandas as pd

# Load the CSV file
df = pd.read_csv("new.csv")
"""
# Strip spaces from all string values in the DataFrame
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Save the cleaned data back to CSV

df.to_csv("cleaned_file.csv", index=False)
"""

df.dropna(how='all', inplace=True)  # Remove empty rows
df.dropna(axis=1, how='all', inplace=True)  # Remove empty columns

df.to_csv("cleaned_fileB2.csv", index=False)

