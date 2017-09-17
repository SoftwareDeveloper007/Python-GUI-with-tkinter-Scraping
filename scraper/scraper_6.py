from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import platform, os, sys, time, csv

class AXIOS_Scraper():
    def __init__(self):
        self.base_url = 'https://www.axios.com/health-care/'
        self.output_data = []
        self.cnt = 15

    def startScraping(self):

        if platform.system() is 'Windows':
            driver = webdriver.Chrome(os.getcwd() + '/WebDriver/chromedriver.exe')
            #driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome(os.getcwd() + '/WebDriver/chromedriver')

        driver.maximize_window()
        driver.get(self.base_url)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

        posts = driver.find_elements_by_css_selector('div.axios-post')

        for i, post in enumerate(posts):
            if i == 15:
                break
            author = post.find_element_by_css_selector('div.author-avatar').find_elements_by_tag_name('li')

            if len(author) > 2:
                tmp = []
                for elm in author[:-1]:
                    tmp.append(elm.text.strip())
                author_name = ',\n'.join(tmp)

            else:
                author_name = author[0].text.strip()

            date = author[-1].text.strip()

            title = post.find_element_by_css_selector('h2').text.strip()
            content = post.find_element_by_css_selector('div.widget__body').text.strip()

            #print(author_name)
            #print(date)
            #print(title)
            #print(content)

            self.output_data.append([date, author_name, title, content])

        print(len(self.output_data))

        driver.quit()

if __name__ == '__main__':
    app = AXIOS_Scraper()
    app.startScraping()