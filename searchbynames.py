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

file_path = 'names.txt' #input("Please enter the path to names.txt: ")
authors = read_names_from_file(file_path)
results = []
missing = False
tries = 0
max_tries = 3

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
    email = ""
    while tries < max_tries and not ends_with_university_domain(email):
        try:
            tries += 1
            author_result = next(scholarly.search_author(author_name))
            author = scholarly.fill(author_result, sections=['basics', 'indices'])
            email = author['email_domain']
        except StopIteration:
            print(f"No results for {author_name}, trying again")
            missing = True
            pass

    tries = 0
    if not missing and ends_with_university_domain(email):
        print({'Author': author['name'], 'Affiliation': get_affiliation(author['email_domain']), 'Citations' : author['citedby'], 'H-index': author["hindex"]})
        results.append({'Author': author['name'], 'Affiliation': get_affiliation(author['email_domain']), 'Citations' : author['citedby'], 'H-index': author["hindex"]})
    missing = False

#save as csv
df = pd.DataFrame(results)
df.to_csv('metrics.csv', index=False)