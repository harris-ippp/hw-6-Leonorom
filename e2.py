import requests
import sys
from bs4 import BeautifulSoup

for line in open("ELECTION_ID"):
    electionid = line.split()[-1]
    url = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(electionid)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    soup = str(soup)

    year = line.split()[0]
    file_name = year +".csv"
    with open(file_name, "w") as out:
       out.write(soup)
