from scholarly import scholarly
import pandas as pd

authors = ['Stephen C. Graves']
results = []

def hindex(pubs):
    citations = [pub['num_citations'] for pub in pubs if 'num_citations' in pub]

    h_index = 0
    for i, citation_count in enumerate(citations, start=1):
        if i <= citation_count:
            h_index = i
        else:
            break

    return h_index

for author in authors:
    query = scholarly.search_author(author)
    # Retrieve the first result from the iterator
    first_author_result = next(query)

    # Retrieve all the details for the author
    author = scholarly.fill(first_author_result)
    print(author)
    affiliation = "Other"
    match(author['email_domain']):
        case '@mit.edu': 
            affiliation = "MIT"
        case 'umich.edu':
            affiliation = "University of Michigan"
        case 'northwestern.edu':
            affiliation = "Northwestern"
        case 'gatech.edu':
            affiliation = "Georgia Tech"
        case 'stanford.edu':
            affiliation = "Stanford"
        case 'illinois.edu':
            affiliation = "UIUC"

    results.append({'Author': author['name'], 'Affiliation': affiliation, 'Citations' : author['citedby'], 'H-index': hindex(author['publications'])})

#save as csv
df = pd.DataFrame(results)
df.to_csv('metrics.csv', index=False)