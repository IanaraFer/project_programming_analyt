import pandas as pd

# Read the CSV file, skipping bad lines
df = pd.read_csv('StationDetails.csv', on_bad_lines='skip')

# Remove '(null)' and replace with NaN
df.replace('(null)', pd.NA, inplace=True)

# Standardize column names
df.columns = [col.lower().replace(' ', '_') for col in df.columns]

# Trim whitespace from all string columns
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Convert 'height(m)' to float
df['height(m)'] = pd.to_numeric(df['height(m)'], errors='coerce')

# Handle missing data in 'close_year' column, you might want to fill with 0 or drop those rows
df['close_year'] = df['close_year'].fillna(0)

# Save the cleaned and normalized data to a new CSV file
df.to_csv('Cleaned_StationDetails.csv', index=False)