'''
This code could be optimized by using scholarly.search_author_by_organization() instead. Perhaps 
this could be used in conjunction with scholarly.search_keyword('Manufacturing' OR ...) to find
all professors associated with manufacturing at a given university. 
Additionally, the sections kword in fill can be used to get only the data we are interested in. 
This means calculating the h-index by hand is uneeded
'''

'''
Use a search string including manufacturing OR ... instead of names.txt

Need to go to a given university, and for all professors in that university, 
check if they have published papers relating to manufacturing, and if they have,
retrive the h-index 

Make an option to search via keyword
Use LLM to make additional search terms after user puts in their own
'''

from scholarly import scholarly
import pandas as pd
import re

def have_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return len(common_elements) > 0


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
    

def main():
    # debug
    '''
    author_result = next(scholarly.search_author('Stephen C. Graves'))
    print(author_result)
    '''
    

    universities = ['MIT', 'University of Michigan', 'Georgia Tech', 'University of Illinois at Urbana-Champaign', 'Stanford', 'Northwestern University']
    keywords = ['manufacturing', 'supply chains', 'manufacturing systems', 'supply chain management']
    IDs = [scholarly.search_org(uni)[0]['id'] for uni in universities]
    authors = []
    results = []
    missing = False
    tries = 0
    max_tries = 3

    # get all authors from a university
    for ID in IDs:
        try:
            query = scholarly.search_author_by_organization(int(ID))
            while True:
                name = next(query)['name']
                authors.append(name)
                print(f"Added {name} to list of names")
        except StopIteration:
            print("Done searching authors")
    
    # see which authors have keywords as interests
    for author_name in authors:
        print(f"Searching for information on {author_name}")
        while tries < max_tries:
            try:
                tries += 1
                author_result = next(scholarly.search_author(author_name))
                author = scholarly.fill(author_result, sections=['basics', 'indices', 'interests'])
                if have_common_elements(author_result['interests'], keywords):
                    print({'Author': author['name'], 'Affiliation': author['email_domain'], 'Citations' : author['citedby'], 'H-index': author["hindex"]})
                    results.append({'Author': author['name'], 'Affiliation': get_affiliation(author['email_domain']), 'Citations' : author['citedby'], 'H-index': author["hindex"]})
            except StopIteration:
                print(f"No results for {author_name}, trying again")
                missing = True
                pass
    
    #save as csv
    df = pd.DataFrame(results)
    df.to_csv('metrics.csv', index=False)

if __name__ == "__main__":
    main()