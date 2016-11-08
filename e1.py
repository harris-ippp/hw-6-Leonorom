import requests
import sys
from bs4 import BeautifulSoup


office_id = {"President" : 1, "Senator" : 6, "Representative" : 5}
search_site = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:{}/stage:{}"
full_url = search_site.format(office_id['President'], 'General')

election_ids = []
election_years = []

req = requests.get(full_url)
soup = BeautifulSoup(req.text, 'html.parser')

soup.find_all('tr','election_item')


for elections in soup.find_all('tr', 'election_item'):
    eid = elections['id'].split('-')[-1]
    election_ids.append(eid)
    year = elections.find('td', 'year first').string
    election_years.append(year)



with open("ELECTION_ID", 'w')  as f:
    for i in range (len(election_ids)):
        line = " ".join([election_years[i],election_ids[i]])
        f.write(line+"\n")
