from urllib import *
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
import urllib.request
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os, zipfile, shutil
import csv, openpyxl, xlrd
from collections import defaultdict

class MAUDE_Scraper():
    def __init__(self):
        self.data_processor = data_processor()
        self.data_processor.parse_txt_file()
        self.data_processor.parse_xls_file()
        self.data_processor.save_parsed_data()
        pass

    def search_companies(self):

        self.display_data = []
        self.date_received = []
        self.company_name = []
        self.brand_name = []
        self.generic_name = []
        self.report_key = []

        for our_company_name in self.data_processor.company_names:
            #print('Our Company Name: ', our_company_name)
            for row_i, row in enumerate(self.data_processor.total_data):
                search_words = our_company_name.split(' ')
                manufacturer_d_address = row[8]
                #print('\tCompany Name:', manufacturer_d_address)
                for i in range(len(search_words)):
                    search_word = ' '.join(search_words[:i+1])
                    #print(search_word)

                    stop_words = ['.', ',', ';', '(', ')', '&', '  ']
                    for stop_word in stop_words:
                        while(stop_word in manufacturer_d_address):
                            manufacturer_d_address = manufacturer_d_address.replace(stop_word, ' ')

                    if search_word in manufacturer_d_address.split(' '):
                        #print(manufacturer_d_address, search_word)
                        # DATE_RECEIVED, MANUFACTURER_D_NAME, BRAND_NAME, GENERIC_NAME, MDR_REPORT_KEY
                        '''
                        self.display_data.append({
                            'date_received': row[5],
                            'company_name': row[8],
                            'brand_name':  row[6],
                            'generic_name':  row[7],
                            'report_key':  row[0],
                        })
                        '''
                        self.date_received.append(row[5])
                        self.company_name.append(row[8])
                        self.brand_name.append(row[6])
                        self.generic_name.append(row[7])
                        self.report_key.append(row[0])

                        break

        #print(self.display_data)

class data_processor():
    def __init__(self):
        self.upzipped_file = download_zip()
        # os.chdir(cwd)
        pass

    def parse_txt_file(self):

        # input_txt = open('Data/foidevAdd.txt', 'r')
        file_name = self.upzipped_file.file_name.replace('.zip', '.txt')
        input_txt = open(file_name, 'r')
        lines = input_txt.read().split('\n')
        new_lines = []
        for line in lines:
            if line is not '':
                new_lines.append(line.split('|'))

        self.header = new_lines[0]
        self.total_data = new_lines[1:]

        input_txt.close()

    def parse_xls_file(self):

        self.company_names = []
        try:
            self.input_xls = xlrd.open_workbook('Data/Scraper Company  Names.xls')
            sheet = self.input_xls.sheet_by_index(0)
            for rx in range(sheet.nrows):
                if sheet.row(rx)[0].value != '' and sheet.row(rx)[0].value != 'Company Name':
                    self.company_names.append(sheet.row(rx)[0].value)

        except:
            pass

    def save_parsed_data(self):
        self.output_csv = open('Data/foidevAdd.csv', 'w', encoding='utf-8', newline='')
        self.csv_writer = csv.writer(self.output_csv)

        self.csv_writer.writerow(self.header)

        for row in self.total_data:
            self.csv_writer.writerow(row)
        self.output_csv.close()

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
                html = download_html(url, num_retries - 1)
    return html

def download_zipfile(url, out_file, num_retries=5):
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
                download_zipfile(url, out_file, num_retries - 1)

class download_zip():
    def __init__(self, url=target_url):
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
                    # print(col.get_attr('href'))
                    self.zip_url = col.find('a')['href']
                    self.zip_name = col.text
                    return

    def download_zipfile(self):
        cwd = os.getcwd()
        self.newdir = cwd + "\\test"
        # print(self.newdir)
        if os.path.isdir(self.newdir) is False:
            os.mkdir(self.newdir)

        completeName = os.path.join(self.newdir, self.zip_name)

        with open(completeName, 'wb') as out_file:
            # f.write(zip_content)
            # f.close()
            download_zipfile(self.zip_url, out_file)

    def unzip(self):

        for item in os.listdir(self.newdir):  # loop through items in dir
            if item.endswith(".zip"):  # check for ".zip" extension
                self.file_name = self.newdir + "\\" + item  # get full path of files
                zip_ref = zipfile.ZipFile(self.file_name)  # create zipfile object
                zip_ref.extractall(self.newdir)  # extract file to dir
                zip_ref.close()  # close file
                os.remove(self.file_name)  # delete zipped file

if __name__ == '__main__':
    app = MAUDE_Scraper()
    app.search_companies()