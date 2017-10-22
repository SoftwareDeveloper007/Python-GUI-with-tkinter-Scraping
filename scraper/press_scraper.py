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