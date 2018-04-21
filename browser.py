import datetime
import os
import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Browser(object):
    locator_dictionary = {}

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1800x6000')
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome()

    def __getattr__(self, k):
        if k in self.locator_dictionary:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    self.locator_dictionary[k]
                )
            )
            return self.find_element(*self.locator_dictionary[k])
        else:
            raise AttributeError(
                '\'{}\' has no attribute \'{}\''.format(
                    self.__class__.__name__, k
                )
            )

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, k):
        return self.driver.find_elements(*self.locator_dictionary[k])

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def open_page(self, url):
        self.driver.get(url)

    def delete_cookies(self):
        return self.driver.delete_all_cookies()
        self.driver.refresh()

    def screen_shot(self, step_str):
        screen = re.sub(r'[^\w\s-]', '', step_str).replace(" ", "_")
        date = datetime.datetime.fromtimestamp(time.time()).strftime(
            '%d%m%Y%H:%M:%S_'
        )
        dir_date = datetime.datetime.fromtimestamp(time.time()).strftime(
            '%d_%m_%Y'
        )
        if not os.path.isdir('Screenshots_{}'.format(dir_date)):
            os.mkdir('Screenshots_{}'.format(dir_date))
        screen_file = ('{}{}.png'.format(date, screen))
        self.driver.save_screenshot(
            os.path.abspath(
                os.path.join('Screenshots_{}'.format(dir_date), screen_file)
            )
        )

    def element_is_selected(self, k):
        self.find_element(*self.locator_dictionary[k]).is_selected()
