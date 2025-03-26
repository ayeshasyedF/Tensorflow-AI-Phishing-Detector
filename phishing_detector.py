import pandas as pd

# Create a dummy dataset
data = {
    'URL': ['http://example1.com', 'http://example2.com', 'http://phishingsite.com'],
    'NumDots': [2, 2, 3],
    'SubdomainLevel': [1, 1, 2],
    'PathLevel': [2, 3, 1],
    'Label': ['legitimate', 'legitimate', 'phishing']
}

# Convert to a pandas DataFrame
dataset = pd.DataFrame(data)

# Show the first few rows
print(dataset.head())
