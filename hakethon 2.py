import pandas as pd

# Load the simulated dataset
df = pd.read_csv('simulated_financial_inclusion_data.csv')

# Display the first few rows of the dataset
print(df.head())

print(df.isnull().sum())



import matplotlib.pyplot as plt

#histogram 
plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Age')
plt.show()

import matplotlib.pyplot as plt

#scatter plot
colors = {True: 'green', False: 'blue'}

scatter = plt.scatter(df['Age'], df['Income'], c=df['Access_to_Banking'].map(colors))

plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Scatter Plot: Age vs. Income')
plt.show()

