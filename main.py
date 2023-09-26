'''
Make an option to search via keyword
Make an option to specify universities
Use LLM to make additional search terms after user puts in their own
Need to find a way to select only professors and associate professors - in affiliation, check if affiliation contains substring "professor"
This will have to be what we do, since manualy checking affiliation incorrectly eliminates some results
'''

from scholarly import scholarly
import pandas as pd

def savefile(results):
    #save as csv
    print('Saving to metrics.csv')
    df = pd.DataFrame(results)
    df.to_csv('metrics.csv', index=False)
    print('Saved to metrics.csv')

def common(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return len(common_elements) > 0

def main():
    
    print('Running...')

    keywords = [
        "lithography", "material deposition", "low-dimensional material", 
        "thin-film deposition", "nanomaterial synthesis", "nanofabrication", 
        "materials characterization", "nanocomposite", "material testing", 
        "sintering", "crystal growth", "materials synthesis", "composite materials", 
        "nanostructure", "materials processing", "microfabrication", "surface coating", 
        "metallurgy", "polymer processing", "additive manufacturing", "3d printing", 
        "chemical vapor deposition", "electrospinning", "sol-gel synthesis", 
        "thermal analysis", "x-ray diffraction", "electron microscopy", "nanoparticles", 
        "nanotubes", "nanowires", "biomaterials", "nanoengineering", "nanopatterning", 
        "quantum dots", "photolithography", "spin coating", "photovoltaic materials", 
        "dielectric material", "nanolithography", "nanoprocessing", "nanomanufacturing", 
        "nanotechnology", "biomimetic material", "smart material", "nanosensor", 
        "nanostructured polymers", "bioinspired materials", "metamaterials", 
        "nanoindentation", "nanorobotics", "nanotribology", "nanomechanics", 
        "nanophotonics", "nanoelectronics", "microfluidics", "nanofluidics", "manufacturing"
    ]
    keycaps = [keyword.capitalize() for keyword in keywords]
    keywords = keywords + keycaps

    print('Finding university IDs...')
    universities = ['MIT', 'University of Michigan', 'Georgia Tech', 'University of Illinois at Urbana-Champaign', 'Stanford', 'Northwestern University']
    IDs = [scholarly.search_org(uni)[0]['id'] for uni in universities]
    authors = []
    results = []
    savectr = 50

    # get all authors associated with keywords from a university

    print('Retrieving authors...')

    for ID, university in zip(IDs, universities):
        try:
            query = scholarly.search_author_by_organization(int(ID))
            while True:
                author = next(query)
                print(f"Checking if {author['name']} of {university} is a professor and associated with keywords")
                if common(author['interests'], keywords) and 'prof' in author['affiliation'].lower():
                    authors.append({'name' : author['name'], 'uni' : university})
                    print(f"Added {author['name']} and {university} to list")
        except:
            print(f"Done searching {university}")
    
    # get metrics and append to results
    for author_name in authors:
        print(f"Searching for {author_name['name']} metrics")
        try:
            author_result = next(scholarly.search_author(author_name['name']))
            author = scholarly.fill(author_result, sections=['basics', 'indices'])
            print({'Author': author_name['name'], 'Affiliation': author_name['uni'], 'Citations' : author['citedby'], 'H-index': author["hindex"]})
            results.append({'Author': author_name['name'], 'Affiliation': author_name['uni'], 'Citations' : author['citedby'], 'H-index': author["hindex"]})
            savectr -= 1
            if not savectr:
                savefile(results)
                savectr = 50
        except:
            print(f"Something went wrong searching for {author['name']}")
            pass
    
    savefile(results)

if __name__ == "__main__":
    main()