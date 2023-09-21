import requests

def get_author_publications(author_name, api_key):
    base_url = "https://api.elsevier.com/content/search/scopus"

    headers = {
        "X-ELS-APIKey": api_key,
        "Accept": "application/json"
    }

    params = {
        "query": f"AU-ID(au-name({author_name}))",
        "count": 100
    }

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if data.get('search-results'):
            return data['search-results']['entry']
        else:
            return []
    else:
        return []

def calculate_h_index(publications):
    citations = [pub['citedby-count'] for pub in publications if 'citedby-count' in pub]
    citations.sort(reverse=True)

    h_index = 0
    for i, citation_count in enumerate(citations, start=1):
        if i <= citation_count:
            h_index = i
        else:
            break

    return h_index

# Replace 'YOUR_API_KEY' with your actual API key from Scopus
api_key = 'a73b018eefad1357d06592f99c9af9ad'
author_names = ["Albert Einstein"]

for author_name in author_names:
    publications = get_author_publications(author_name, api_key)
    h_index = calculate_h_index(publications)
    print(f"{author_name}: h-index = {h_index}")
