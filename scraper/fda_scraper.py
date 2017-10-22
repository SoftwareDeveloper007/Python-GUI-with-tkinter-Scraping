from bs4 import BeautifulSoup
try:
    from urllib2 import urlopen
except:
    from urllib.request import urlopen
import re

try:
    from urlparse import urlparse, urljoin
except:
    from urllib.parse import urlparse, urljoin

class FDA_MedWatch():
    def __init__(self, url = 'http://www.fda.gov/Safety/MedWatch/default.htm'):
        self.url = url
        #o = urlparse(self.url)
        page = urlopen(self.url)
        self.soup = BeautifulSoup(page.read(), 'html.parser')

    def parse(self):
        self.links = []
        self.titles = []
        self.descs = []
        self.dates = []

        whatsnew = self.soup.find("div", {"class": "panel-body"})
# below will cast all items as a string...hopefully resolving format issue....
        for link in whatsnew.find_all('a'):
            #print(urljoin(self.url, link.get('href')))
            self.links.append(urljoin(self.url, link.get('href')))

        for title in whatsnew.find_all('linktitle'):
            #print(title.contents)
            self.titles.append(title.text)

        regex1 = re.compile('(.*?) Posted ', re.IGNORECASE)

        for desc in whatsnew.find_all('desc'):
            try:
                self.descs.append(regex1.findall(desc.text)[0])
                #temp = desc.text(' ')

            except:
                self.descs.append('-')
            #print(regex1.findall(desc.text))

            txt = desc.text.split(' ')

            if 'Posted' in txt:
                self.dates.append(txt[txt.index('Posted') + 1])
            elif 'Updated' in txt:
                self.dates.append(txt[txt.index('Updated') + 1])