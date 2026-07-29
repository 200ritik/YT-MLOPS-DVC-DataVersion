import pandas as pd
import os

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
# Save the DataFrame to a CSV file

os.makedirs("data/raw", exist_ok=True)

# define the path to the CSV file
file_path = os.path.join("data/raw", "sample_data.csv")
df.to_csv(file_path, index=False)
print(f"DataFrame saved to {file_path}")
