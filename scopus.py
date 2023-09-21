import requests

def get_author_publications(last, first, university, api_key):
    url = f'https://api.elsevier.com/metrics/metrics?metrics=ScholarlyOutput%2CCitedPublications&authors=6701858763%2C20433296900&yearRange=5yrs&includeSelfCitations=true&byYear=true&includedDocs=AllPublicationTypes&journalImpactType=CiteScore&showAsFieldWeighted=false&indexType=hIndex'

    headers = {
        "X-ELS-APIKey": api_key,
        "Accept": "application/json"
    }

    params = {
        "query" : '',
        "count" : 100
    }

    response = requests.get(url, headers=headers, params=params)
    #debug printing
    print(response.url)
    print(response.headers)

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

api_key = '84373796f32936169439fc00d3d3857a'
names = [["Albert", "Einstein"]]
universities = ["Institute for Advanced Studies"]

for name in names:
    publications = get_author_publications(name[1], name[0], "Institute for Advanced Studies", api_key)
    h_index = calculate_h_index(publications)
    print(f"{name[1], name[0]}: h-index = {h_index}")
