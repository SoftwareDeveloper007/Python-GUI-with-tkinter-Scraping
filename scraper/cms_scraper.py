from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import platform, os, sys, time, csv

def takeFirst(elem):
    return elem[0]


class CMS_Scraper():
    def __init__(self):
        self.start_url = 'https://www.cms.gov/medicare-coverage-database/reports/draft-lcd-status-report.aspx?' \
                         'name=373*1|374*1|378*1|375*1|379*1|376*1|380*1|377*1|381*1&bc=AQAAAgAAAAAAAA%3d%3d&#ResultAnchor'
        self.output_data = []
        self.urls = []

    def startScraping(self):
        if platform.system() is 'Windows':
            #driver = webdriver.Chrome(os.getcwd() + '/WebDriver/chromedriver.exe')
            #driver = webdriver.Chrome()
            #driver = webdriver.PhantomJS(os.getcwd() + '/WebDriver/phantomjs.exe')
            driver = webdriver.Chrome(os.getcwd() + '/WebDriver/chromedriver.exe')

        else:
            driver = webdriver.Chrome(os.getcwd() + '/WebDriver/chromedriver')


        driver.maximize_window()
        driver.get(self.start_url)

        def page_loading(num_tries = 5):
            print(num_tries, 'th try to load web page')
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "table#ctl00_ctl00_ctl00_CMSGMainContentPlaceHolder"
                                                                     "_ToolContentPlaceHolder_MCDContentPlaceHolder_DraftLCDReport1_LCDGridView"))
                )
                isSuccess = True
            except:
                isSuccess = False
                if num_tries > 0:
                    driver.refresh()
                    isSuccess = page_loading(num_tries-1)

            return isSuccess

        if page_loading():
            print('Successfully Loaded the web page')
        else:
            print("Can't access to the web page")


        pageRow = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "tr.PagerRow"))
        )
        popup = pageRow.find_elements_by_css_selector('select > option')[3]
        popup.click()
        time.sleep(10)
        table = driver.find_element_by_css_selector('table#ctl00_ctl00_ctl00_CMSGMainContentPlaceHolder_ToolContentPlaceHolder_MCDContentPlaceHolder_DraftLCDReport1_LCDGridView')
        trs = table.find_elements_by_tag_name('tr')
        print(len(trs), 'rows found')

        for i, tr in enumerate(trs):
            if i in [0,1, len(trs)-1]:
                continue
            row = []
            row.append(tr.find_element_by_tag_name('th').text)
            self.urls.append(tr.find_element_by_tag_name('th').find_element_by_tag_name('a').get_attribute('href'))
            for td in tr.find_elements_by_tag_name('td'):
                txt = td.text.replace('&nbsp', '')
                row.append(txt)

            self.output_data.append(row)

        #print(self.output_data)
        #print(self.urls)
        driver.quit()

if __name__ == '__main__':
    app = CMS_Scraper()
    app.startScraping()