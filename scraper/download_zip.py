from urllib import *
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
import urllib.request
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os, zipfile
import shutil

target_url = 'https://www.fda.gov/medicaldevices/deviceregulationandguidance/postmarketrequirements/reportingadverseevents/ucm127891.htm'

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

def download_zipfile(url, out_file, num_retries = 5):
    """Download function that also retries 5XX errors"""
    try:
        response = urlopen(url)
        shutil.copyfileobj(response, out_file)
    except urllib.error.URLError as e:
        print('Download error:', e.reason)
        response = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
                download_zipfile(url, out_file, num_retries-1)


class download_zip():
    def __init__(self, url = target_url):
        self.url = url
        self.html = download(self.url)
        self.get_url_zip()
        self.download_zipfile()
        self.unzip()

    def get_url_zip(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        rows = soup.find('table').find('tbody').find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            for col in cols:
                if 'foidevadd.zip' in col.text:
                    #print(col.get_attr('href'))
                    self.zip_url = col.find('a')['href']
                    self.zip_name = col.text
                    return
    def download_zipfile(self):
        cwd = os.getcwd()
        self.newdir = cwd + "\\test"
        #print(self.newdir)
        if os.path.isdir(self.newdir) is False:
            os.mkdir(self.newdir)

        completeName = os.path.join(self.newdir, self.zip_name)

        with open(completeName, 'wb') as out_file:
            #f.write(zip_content)
            #f.close()
            download_zipfile(self.zip_url, out_file)

    def unzip(self):
        #os.chdir(self.newdir)
        #print('newdir: ', self.newdir)

        for item in os.listdir(self.newdir):  # loop through items in dir
            if item.endswith(".zip"):  # check for ".zip" extension
                self.file_name = self.newdir+"\\"+item # get full path of files
                zip_ref = zipfile.ZipFile(self.file_name)  # create zipfile object
                zip_ref.extractall(self.newdir)  # extract file to dir
                zip_ref.close()  # close file
                os.remove(self.file_name)  # delete zipped file
                #print('item: ', item)
                #print('filename: ', self.file_name)

if __name__ == '__main__':
    app = download_zip(target_url)
    #app.get_url_zip()
    #app.download_zipfile()
    #app.unzip()

