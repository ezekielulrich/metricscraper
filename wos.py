import requests
import pandas as pd

api_key = '180146437ac53bfedb19d7421867592364e296a2'

# Define the universities you're interested in
universities = [
    'Massachusetts Institute of Technology'
]

# Define the query to search for materials engineering/manufacturing professors
query = 'CU=materials engineering/manufacturing AND (AD={})'

# Initialize an empty list to store the results
results = []

# Loop through the universities
for university in universities:
    # Make API request
    url = f'https://api.clarivate.com/api/wos?databaseId=WOS&usrQuery={query.format(university)}'
    headers = {'X-ApiKey': api_key}
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        for record in data['Data']:
            name = record.get('AU', [''])[0]
            h_index = record.get('H-index', '')
            results.append({'Name': name, 'University': university, 'H-index': h_index})
    else:
        print(f'Error fetching data for {university}. Status code: {response.status_code}')

# Create a DataFrame
df = pd.DataFrame(results)

# Save to CSV
df.to_csv('professors_data.csv', index=False)
