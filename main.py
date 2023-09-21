'''
ChatGPT generated this, probably full of errors :(
Debug time
'''

import requests

api_key = '180146437ac53bfedb19d7421867592364e296a2'

# Define your search query
search_query = 'AU=(Associate Professor OR Professor) AND AD=Massachusetts Institute of Technology AND WC=(Manufacturing Engineering)'

api_url = 'https://api.clarivate.com/api/wos/'

headers = {
    'X-ApiKey': api_key,
    'Content-Type': 'application/json'
}

# Perform a search to retrieve author data
def search_author_data(query):
    payload = {
        "databaseId": "WOS",
        "usrQuery": query,
        "queryLanguage": "en",
        "count": 100,  # Adjust as needed
        "firstRecord": 1,
        "fields": [
            {
                "name": "Relevance",
                "sort": "D"
            }
        ]
    }
   
    response = requests.post(api_url + 'search/query', json=payload, headers=headers)
    return response.json()

# Get the h-index for a given author
def get_h_index(author_id):
    payload = {
        "databaseId": "WOS",
        "idType": "eid",
        "retrieveParameters": {
            "count": 100,
            "firstRecord": 1,
            "fields": [
                {
                    "name": "D",
                    "sort": "D"
                }
            ]
        }
    }
   
    response = requests.get(api_url + f'retrieve/author/{author_id}', params=payload, headers=headers)
    print("Response:", response)
    author_data = response.json()
   
    # Extract and return the h-index
    h_index = author_data['data']['h_index']
    return h_index

# Main function to collect h-index values
def main():
    # Perform the search
    search_result = search_author_data(search_query)
   
    # Extract author data and calculate the average h-index
    authors = search_result['Data']['Records']
    h_indexes = []
   
    for author in authors:
        author_id = author['UID']
        h_index = get_h_index(author_id)
        h_indexes.append(h_index)
   
    # Calculate the average h-index
    average_h_index = sum(h_indexes) / len(h_indexes)
   
    print(f"Total Professors: {len(h_indexes)}")
    print(f"Average h-index: {average_h_index:.2f}")

if __name__ == "__main__":
    main()