import pandas as pd

# Creating a simple DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
print()

# Add a new column
df['Profession'] = ['Engineer', 'Doctor', 'Architect', 'Scientist']
print(df)
print()

# Filter the DataFrame based on age
filtered_df = df[df['Age'] > 30]
print(filtered_df)
print()