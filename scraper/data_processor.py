import csv
import openpyxl
import xlrd
from collections import defaultdict
from scraper.download_zip import *
import os

class data_processor():
    def __init__(self):
        self.upzipped_file = download_zip()
        #os.chdir(cwd)
        pass

    def parse_txt_file(self):

        #input_txt = open('Data/foidevAdd.txt', 'r')
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
        #print(self.total_data)

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

        #print(self.company_names)


    def save_parsed_data(self):
        self.output_csv = open('Data/foidevAdd.csv', 'w', encoding='utf-8', newline='')
        self.csv_writer = csv.writer(self.output_csv)

        self.csv_writer.writerow(self.header)

        for row in self.total_data:
            self.csv_writer.writerow(row)
        self.output_csv.close()

if __name__ == '__main__':
    app = data_processor()
    app.parse_txt_file()
    app.parse_xls_file()
    app.save_parsed_data()
