import requests

def get_author_publications(author_name, university, api_key):
    url = f"http://api.elsevier.com/content/search/author"

    headers = {
        "X-ELS-APIKey": api_key,
        "Accept": "application/json"
    }

    params = {
        "query" : f"AFFIL%28{university}%29+AND+SUBJAREA%28MATE%29",
        "count" : 100
    }

    response = requests.get(url, headers=headers, params=params)
    print(response)

    if response.status_code == 200:
        data = response.json()
        print(data)
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

api_key = 'a73b018eefad1357d06592f99c9af9ad'
author_names = ["Albert Einstein"]
universities = ["Institute for Advanced Studies"]

for author_name in author_names:
    publications = get_author_publications(author_name, "Institute for Advanced Studies", api_key)
    h_index = calculate_h_index(publications)
    print(f"{author_name}: h-index = {h_index}")
