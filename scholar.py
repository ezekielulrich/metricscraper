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
    results.append({'Author': author['name'], 'Affiliation': author['affiliation'], 'Citations' : author['citedby'], 'H-index': hindex(author['publications'])})

print(author['citedby'])
print(len(author['publications']))
print(hindex(author['publications']))
print(results)

#save as csv
df = pd.DataFrame(results)
df.to_csv('metrics.csv', index=False)