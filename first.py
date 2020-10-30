from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import USERNAME, PASSWORD, EMAIL
import time
import random


def login(username, password):
    browser = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')

    browser.get('https://my.account.sony.com/central/signin/?client_id=fe1fdbfa-f1a1-47ac-b793-e648fba25e86#/signin/ca?entry=ca')
    time.sleep(random.randrange(3, 5))

    browser.close()
    browser.quit()


if __name__ == "__main__":
    login(USERNAME, PASSWORD)
