from scholarly import scholarly
import pandas as pd

def read_names_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            names = [line.strip() for line in file.readlines()]
        return names
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

file_path = 'names.txt'
authors = read_names_from_file(file_path)
results = []
missing = False
missingstr = f"""One or more names returned no results. 
A common reason is the publishing name and name provided in {file_path} differ. 
Try searching Google Scholar manually to find publishing name."""

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
    try:
        author_result = next(scholarly.search_author(author))
    except StopIteration:
        print(f"No results for {author}")
        missing = True
        pass

    author = scholarly.fill(author_result)
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

if missing:
    print(missingstr)

#save as csv
df = pd.DataFrame(results)
df.to_csv('metrics.csv', index=False)