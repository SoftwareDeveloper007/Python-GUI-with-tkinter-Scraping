from bs4 import BeautifulSoup
try:
    from urllib2 import urlopen
except:
    from urllib.request import urlopen
import re


class Drug_Recalls():
    def __init__(self, url = 'https://www.fda.gov/Drugs/DrugSafety/DrugRecalls/default.htm'):
        self.url = url
        #o = urlparse(self.url)
        page = urlopen(self.url)
        self.soup = BeautifulSoup(page.read(), 'html.parser')

    def parse(self):
        self.total_data = []
        tbody = self.soup.find("tbody").find_all("tr")

        for line in tbody:
            line_sep = line.find_all("td")
            self.total_data.append({
                "date": line_sep[0].text,
                "brand": line_sep[1].find("a").text,
                "description": line_sep[2].text,
                "problem": line_sep[3].text,
                "company": line_sep[4].text,
            })