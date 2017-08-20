import csv
import openpyxl
import xlrd

from scraper.data_processor import *

class scraper_2():
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

                    stop_words = ['.', ',', '-', ';', '(', ')', '&']
                    for stop_word in stop_words:
                        while(stop_word in manufacturer_d_address):
                            manufacturer_d_address = manufacturer_d_address.replace(stop_word, '')

                    if search_word in manufacturer_d_address:
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



if __name__ == '__main__':
    app = scraper_2()
    app.search_companies()