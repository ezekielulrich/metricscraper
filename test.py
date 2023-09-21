import requests
from bs4 import BeautifulSoup

def get_h_index(name):
    url = f'https://scholar.google.com/scholar?q={name.replace(" ", "+")}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        h_index_tag = soup.find('td', {'class': 'gsc_rsb_f gs_ibl'})
        
        if h_index_tag:
            return h_index_tag.text.strip()
        else:
            return None
    else:
        print(f"Error: Unable to fetch data for {name}")
        return None

names = ["Stephen Graves"]  # Add the list of names here

for name in names:
    h_index = get_h_index(name)
    if h_index is not None:
        print(f"The h-index of {name} is {h_index}")
    else:
        print(f"Could not retrieve h-index for {name}")
