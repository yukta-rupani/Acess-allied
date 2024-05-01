import numpy as np
import pandas as pd

# Define the size of the dataset
num_samples = 1000

# Generate synthetic data for features
age = np.random.randint(18, 80, num_samples)
gender = np.random.choice(['Male', 'Female'], num_samples)
income = np.random.normal(50000, 20000, num_samples)  # Normal distribution with mean 50000 and standard deviation 20000
access_to_banking = np.random.choice([True, False], num_samples)
# Add more features as needed

# Create a DataFrame to store the data
data = pd.DataFrame({
    'Age': age,
    'Gender': gender,
    'Income': income,
    'Access_to_Banking': access_to_banking
    # Add more columns here
})

# Display the first few rows of the dataset
print(data.head())

# Save the dataset to a CSV file for future use
data.to_csv('simulated_financial_inclusion_data.csv', index=False)
