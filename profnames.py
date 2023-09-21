from scholarly import scholarly

def get_professors_from_scholar(query, university_name, num_results=10):
    search_query = scholarly.search_pubs(query)
    professors = []

    for i in range(num_results):
        try:
            result = next(search_query)
            print(result)
            authors = result['bib']['author']
            
            for author in authors:
                '''
                if 'manufacturing' in author:
                '''
                if university_name in author['affiliation'].lower():
                    professors.append(author)
        except StopIteration:
            break

    return professors

university_name = "stanford"
query = f"{university_name} AND manufacturing"
professors = get_professors_from_scholar(query, university_name, num_results=10)

print(f"Professors at {university_name}:")
for professor in professors:
    print(professor)
