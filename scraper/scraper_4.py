from bs4 import BeautifulSoup
try:
    from urllib2 import urlopen
except:
    from urllib.request import urlopen
try:
    from urlparse import urlparse, urljoin
except:
    from urllib.parse import urlparse, urljoin

import re, time
from datetime import date, datetime, timedelta

def download(url, num_retries=5):
    """Download function that also retries 5XX errors"""
    try:
        html = urlopen(url).read()
    except urllib.error.URLError as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
                html = download_html(url, num_retries-1)
    return html


class HHS_Scraper():
    def __init__(self):
        self.base_url = 'https://www.federalregister.gov/documents/search?conditions%5Bagencies%5D%5B%5D=health-and-human' \
                        '-services-department&conditions%5Bpublication_date%5D%5Bgte%5D={0}%2F{1}%2F{2}'
        self.output_data = []

    def urlGeneration(self):
        curDate = datetime.now() - timedelta(days=10)
        curDateStr = str(curDate.date()).split('-')
        self.base_url = self.base_url.format(curDateStr[1], curDateStr[2], curDateStr[0])
        self.urls = []

        for i in range(1, 100):
            url = self.base_url + '&page={0}'.format(i)
            self.urls.append(url)

    def startScraping(self):

        for i, url in enumerate(self.urls):
            html = download(url)
            #print(html)
            soup = BeautifulSoup(html, 'html.parser')
            rows = soup.find_all("div", {"class":"document-wrapper"})
            for row in rows:
                try:
                    _title = row.find("h5").text.strip()
                except:
                    _title = ''
                try:
                    _agency = row.find("p", {"class":"metadata"}).find_all("a")[0].text.strip()
                except:
                    _agency = ''
                try:
                    _date = row.find("p", {"class":"metadata"}).find_all("a")[1].text.strip()
                except:
                    _date = ''
                try:
                    _desc = row.find("p", {"class":"description"}).text.strip()
                except:
                    _desc = ''
                #print(_title)
                #print(_agency)
                #print(_date)
                #print(_desc)

                self.output_data.append([_title, _agency, _date, _desc])

            if 'No documents were found' in soup.text:
                break
        print(len(self.output_data))



if __name__ == '__main__':
    app = HHS_Scraper()
    app.urlGeneration()
    app.startScraping()
