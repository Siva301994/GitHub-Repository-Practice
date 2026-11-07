import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# Basic operations
print("\nMean age:", df['Age'].mean())
print("Max age:", df['Age'].max())
