from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import platform, os, sys, time, csv

class GENOME_Scraper():
    def __init__(self):
        self.base_url = 'https://www.genomeweb.com/breaking-news'
        self.output_data = []

    def startScraping(self):

        if platform.system() is 'Windows':
            driver = webdriver.Chrome(os.getcwd() + '/WebDriver/chromedriver.exe')
            #driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome(os.getcwd() + '/WebDriver/chromedriver')

        driver.maximize_window()
        driver.get(self.base_url)
        news = driver.find_element_by_css_selector('div.view-breaking-news').find_elements_by_css_selector('div.views-row')

        for new in news:
            date = new.find_element_by_css_selector('div.container-inline.fieldlayout.node-field-byline').text.strip()
            content = new.find_element_by_css_selector('h3').text.strip()
            self.output_data.append([date, content])

        driver.quit()

if __name__ == '__main__':
    app = GENOME_Scraper()
    app.startScraping()
