from scholarly import scholarly
import pandas as pd
import re

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
tries = 0
max_tries = 3

def hindex(pubs):
    citations = [pub['num_citations'] for pub in pubs if 'num_citations' in pub]

    h_index = 0
    for i, citation_count in enumerate(citations, start=1):
        if i <= citation_count:
            h_index = i
        else:
            break

    return h_index

def ends_with_university_domain(input_string):

    university_patterns = [
        r".*mit\.edu$",
        r".*umich\.edu$",
        r".*gatech\.edu$",
        r".*illinois\.edu$",
        r".*stanford\.edu$",
        r".*northwestern\.edu$"
    ]

    for pattern in university_patterns:
        if re.match(pattern, input_string):
            return True

    return False

def get_affiliation(input_string):
    if re.match(r".*mit\.edu$", input_string):
        return 'MIT'
    elif re.match(r".*umich\.edu$", input_string):
        return "UMichigan"
    elif re.match(r".*gatech\.edu$", input_string):
        return "Georgia Tech"
    elif re.match(r".*illinois\.edu$", input_string):
        return "UIUC"
    elif re.match(r".*stanford\.edu$", input_string):
        return "Stanford"
    elif re.match(r".*northwestern\.edu$", input_string):
        return "Northwestern"
    else:
        return "Other"


for author_name in authors:
    print(f"Searching for information on {author_name}")
    try:
        tries += 1
        author_result = next(scholarly.search_author(author_name))
        author = scholarly.fill(author_result)
    except StopIteration:
        print(f"No results for {author_name}")
        missing = True
    
    while tries < max_tries and not ends_with_university_domain(author['email_domain']):
        try:
            tries += 1
            print("Found author of same name not associated with given universities, trying again...")
            author_result = next(scholarly.search_author(author_name))
            author = scholarly.fill(author_result)
        except StopIteration:
            print(f"No results for {author_name}")
            missing = True
            pass

    tries = 0
    results.append({'Author': author['name'], 'Affiliation': get_affiliation(author['email_domain']), 'Citations' : author['citedby'], 'H-index': hindex(author['publications'])})

if missing:
    print(missingstr)

#save as csv
df = pd.DataFrame(results)
df.to_csv('metrics.csv', index=False)