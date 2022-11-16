from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import requests
from requests import request
import urllib3
import time
import os


class SeliumWebsiteController:
    def __init__(self):
        urllib3.disable_warnings()
        self.driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')

    def ReturnWebpage(self, webpage_url=None, sleep=1, use_soup=True):
        if not webpage_url is None:
            self.driver.get(webpage_url)
        time.sleep(sleep)
        if use_soup:
            return BeautifulSoup(self.driver.page_source, "html.parser")
        else:
            return self.driver.page_source

    def PressButton(self, sleep=1, class_name=None, id_name=None):
        if not class_name == None:
            button = self.driver.find_element(By.CLASS_NAME, class_name)
        elif not id_name == None:
            button = self.driver.find_element(By.ID, id_name)
        else:
            return None

        button.click()
        return self.ReturnWebpage(sleep=sleep)

    def ScrollWebpage(self, y_amount, sleep=1):
        self.driver.execute_script(f"window.scroll(0, {y_amount})")
        time.sleep(sleep)

class RequestsWebsiteController:
    def __init__(self, verify=True):
        self.verify = verify
        if not self.verify:
            urllib3.disable_warnings()

    def ReturnWebpage(self, webpage_url, sleep=1, use_soup=True):
        page = requests.get(webpage_url, verify=self.verify)
        time.sleep(sleep)
        if use_soup:
            return BeautifulSoup(page.content, "html.parser")
        else:
            return page.content

    def DownloadImage(self, image_url, image_name, folder_path="Data/images", sleeep=1):
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        full_path = folder_path + "/" + image_name
        pull_image = requests.get(image_url, vrify=self.verify)
        with open(full_path, "wb") as handler:
            handler.write(pull_image.content)
        time.sleep(sleeep)


class RequestWebsiteController:
    def __init__(self, verify=True):
        self.verify = verify
        if not self.verify:
            urllib3.disable_warnings()

    def ReturnWebpage(self, webpage_url, method="GET", sleep=1, use_soup=True, headers=None, auth="", params=None):
        if params is None:
            params = {}
        if headers is None:
            headers = {}
        page = request(method, webpage_url, headers=headers, auth=auth, params=params)
        time.sleep(sleep)
        if use_soup:
            return BeautifulSoup(page.content, "html.parser")
        else:
            return page.content
