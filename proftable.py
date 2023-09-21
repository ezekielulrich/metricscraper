import requests
import json
import csv

api_key = 'a73b018eefad1357d06592f99c9af9ad'

universities = ['MIT', 'University of Michigan', 'Stanford']
professors_data = []

url = "https://api.elsevier.com/content/search/author"

response = requests.get(url + '?query=' + 'Stephen Graves', headers={'Accept':'application/json', 'X-ELS-APIKey': api_key})

# Print the response
response_json = response.json()
print(response_json)

'''
for university in universities:
    # Define the API endpoint for the search
    url = f'https://api.elsevier.com/content/search/scopus'
    params = {
        'query': f'AFFIL({university}) AND (AUTHOR-STATUS(professor) OR AUTHOR-STATUS(assocprof))',
        'apiKey': api_key,
        'field': 'h-index,affilname,authid,given-name,surname'
    }

    # Make the API call
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        for entry in data['search-results']['entry']:
            name = f"{entry['author']['given-name']} {entry['author']['surname']}"
            h_index = entry.get('h-index', 'N/A')
            university = entry['affilname']

            professors_data.append([name, h_index, university])
    else:
        print(f'Error fetching data for {university}. Status code: {response.status_code}')

# Write the data to a CSV file
with open('professors_data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Name', 'H-Index', 'University'])
    csvwriter.writerows(professors_data)
'''