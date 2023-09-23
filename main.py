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
    author_result = next(scholarly.search_author('np suh'))
    print(author_result)
    '''
    
    print('Program is running...')

    print('Finding university IDs...')
    universities = ['MIT', 'University of Michigan', 'Georgia Tech', 'University of Illinois at Urbana-Champaign', 'Stanford', 'Northwestern University']
    keywords = ['manufacturing', 'supply chains', 'manufacturing systems', 'supply chain management', 'mechanical engineering']
    IDs = [scholarly.search_org(uni)[0]['id'] for uni in universities]
    authors = []
    results = []
    tries = 0
    max_tries = 3

    # get all authors from a university

    print('Retrieving authors...')

    for ID in IDs:
        try:
            query = scholarly.search_author_by_organization(int(ID))
            while True:
                author = next(query)
                if have_common_elements(author['interests'], keywords):
                    authors.append(author['name'])
                    print(f"Added {author['name']} to list of names")
        except StopIteration:
            print("Done searching authors")
    
    # see which authors have keywords as interests and append to results

    for author_name in authors:
        print(f"Searching for {author_name} metrics and interests")
        while tries < max_tries:
            tries += 1
            try:
                author_result = next(scholarly.search_author(author_name))
                author = scholarly.fill(author_result, sections=['basics', 'indices'])
                print({'Author': author['name'], 'Affiliation': author['email_domain'], 'Citations' : author['citedby'], 'H-index': author["hindex"]})
                results.append({'Author': author['name'], 'Affiliation': get_affiliation(author['email_domain']), 'Citations' : author['citedby'], 'H-index': author["hindex"]})
            except StopIteration:
                print(f"No results for {author_name}, trying again")
                pass
    
    #save as csv
    print('Saving to metrics.csv')
    df = pd.DataFrame(results)
    df.to_csv('metrics.csv', index=False)
    print('Saved to metrics.csv')

if __name__ == "__main__":
    main()