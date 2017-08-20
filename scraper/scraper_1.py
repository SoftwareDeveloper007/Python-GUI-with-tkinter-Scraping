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


class Press_Announcements():
    def __init__(self, url = 'https://www.fda.gov/NewsEvents/Newsroom/PressAnnouncements/default.htm'):
        self.url = url
        #o = urlparse(self.url)
        page = urlopen(self.url)
        self.soup = BeautifulSoup(page.read(), 'html.parser')

    def parse(self):
        self.total_data = []
        self.month_name = []

        months_seps = self.soup.find_all("div", {"class": "panel-body"})
        month_names = self.soup.find_all("h2", {"class": "panel-title"})

        for month in month_names:
            temp = month.text
            while "\t" in temp:
                temp = temp.replace("\t", "")
            while "\r" in temp:
                temp = temp.replace("\r", "")
            while "\n" in temp:
                temp = temp.replace("\n", "")
            temp = temp.split(" ")
            temp = " ".join(temp)

            self.month_name.append(temp)

        for body in months_seps:
            lines = body.find_all("li")
            body_data = []
            for line in lines:
                body_data.append({
                    "date": line.text,
                    "content": line.find("a").text
                })
            self.total_data.append(body_data)

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


if __name__ == '__main__':
    #parse_ctrl = data_parse()
    #parse_ctrl.parse()
    #print(parse_ctrl.links)
    #pass
    ctrl2 = Drug_Recalls()
    ctrl2.parse()