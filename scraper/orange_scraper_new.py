from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import date, datetime, timedelta
import platform, os, sys, time, csv

def takeFirst(elem):
    return elem[0]

class ORANGE_Scraper_New():
    def __init__(self):
        self.base_url = 'https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=reportsSearch.process'
        self.display_data = []

    def startScraping(self):
        curDate = datetime.now()
        year = curDate.year
        month = curDate.month
        day = curDate.day

        if platform.system() is 'Windows':
            #driver = webdriver.Chrome(os.getcwd() + '/WebDriver/chromedriver.exe')
            # driver = webdriver.Chrome()
            #driver = webdriver.PhantomJS(os.getcwd() + '/WebDriver/phantomjs.exe')
            driver = webdriver.Chrome(os.getcwd() + '/WebDriver/chromedriver.exe')

        else:
            driver = webdriver.Chrome(os.getcwd() + '/WebDriver/chromedriver')

        driver.maximize_window()
        driver.get(self.base_url)

        tbl_rows = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "table#example_1 > tbody > tr"))
        )

        curMonthData = []
        for i, row in enumerate(tbl_rows):
            # print("1: ", i)
            cols = row.find_elements_by_tag_name('td')
            curMonthData.append([cols[0].text.strip(), cols[1].text.strip(), cols[2].text.strip(),
                                      cols[3].text.strip(), cols[4].text.strip(), cols[5].text.strip(),
                                      cols[6].text.strip()])
        curMonthData.reverse()

        month_opt = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='reportSelectMonth']/option[{}]".format(month)))
        )
        month_opt.click()

        search_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
        )
        search_btn.click()

        tbl_rows = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "table#example_1 > tbody > tr"))
        )

        preMonthData = []
        for i, row in enumerate(tbl_rows):
            # print("2: ", i)
            cols = row.find_elements_by_tag_name('td')
            preMonthData.append([cols[0].text.strip(), cols[1].text.strip(), cols[2].text.strip(),
                                      cols[3].text.strip(), cols[4].text.strip(), cols[5].text.strip(),
                                      cols[6].text.strip()])
        preMonthData.reverse()

        driver.close()
        driver.quit()

        self.display_data = curMonthData + preMonthData
        self.display_data.sort(key=takeFirst)
        self.display_data.reverse()

    def save_csv(self):
        filename = 'orange_result_new.csv'
        output_file = open(filename, 'w', encoding='utf-8', newline='')
        writer = csv.writer(output_file)

        headers = ['Date', 'Drug Name', 'Submission', 'Active Ingredients', 'Company', 'Submission Classfication', 'Submission Status']
        writer.writerow(headers)

        for i, row in enumerate(self.display_data):
            writer.writerow(row)

if __name__ == '__main__':
    app = ORANGE_Scraper_New()
    app.startScraping()
    app.save_csv()
