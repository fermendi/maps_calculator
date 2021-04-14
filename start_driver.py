#
# @file <start_driver.py>
#
# @author Fernando Mendiburu - <fernando.mendiburu@ee.ufcg.edu.br>
#

import time

from selenium import webdriver
from common import Functions, Path
from exceptions import BrowserImplementationException

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Data:
    TIMEOUT = 20
    CHROME_EXECUTABLE_PATH = Path.PATH + Path.CHROMEDRIVER_FILE
    OPTIONS = webdriver.ChromeOptions()
    OPTIONS.add_argument('--headless')
    OPTIONS.add_argument("--start-maximized")


class Browser:
    CHROME = "Chrome"
    FIREFOX = "Firefox"


class StartDriver:
    def __init__(self, browser):
        self.start_driver(browser)

    def __del__(self):
        try:
            self.driver.quit()
        except:
            pass

    def start_driver(self, browser):
        if browser == Browser.CHROME:
            self.driver = webdriver.Chrome(executable_path=Data.CHROME_EXECUTABLE_PATH,
                                           chrome_options=Data.OPTIONS)
            print('Init driver...')
        else:
            raise BrowserImplementationException(browser)


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, Data.TIMEOUT).until(EC.element_to_be_clickable(by_locator)).click()
        time.sleep(Functions.get_time_step())

    def enter_text(self, by_locator, text):
        web_element = WebDriverWait(self.driver, Data.TIMEOUT).until(EC.presence_of_element_located(by_locator))
        web_element.clear()
        web_element.send_keys(text)

    def is_part_text_present(self, by_locator, element_text):
        try:
            element = WebDriverWait(self.driver, Data.TIMEOUT).until(EC.presence_of_element_located(by_locator))
            if element.text.find(element_text) >= 0:
                return True
            else:
                return False
        except:
            return False

    def is_element(self, by_locator):
        try:
            WebDriverWait(self.driver, Data.TIMEOUT).until(EC.presence_of_element_located(by_locator))
            return True
        except:
            return False

    def search_element(self, by_locator):
        time.sleep(Functions.get_time_step())
        return self.driver.find_element(by_locator[0],by_locator[1])

    def search_elements(self, by_locator):
        time.sleep(Functions.get_time_step())
        return self.driver.find_elements(by_locator[0],by_locator[1])


# -------------------------------------------------------------------------------------------
# ------------------------------------------Main---------------------------------------------
# -------------------------------------------------------------------------------------------

if __name__ == '__main__':
    pass