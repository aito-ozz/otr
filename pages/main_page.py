from .base_page import BasePage
from locators import ManePageLocators as MPL
from src.enum.global_enums import GlobalErrorMessages as GEM
from selenium.common.exceptions import NoSuchElementException
from variables import *
import requests


class MainPage(BasePage):

    global links_list
    links_list = []

    def header(self):
        try:
            h = self.browser.find_element(*MPL.header)
        except NoSuchElementException:
            print(GEM.HEADER_IS_MISSING.value)
    
    def footer(self):
        try:
            f = self.browser.find_element(*MPL.footer)
        except NoSuchElementException:
            print(GEM.FOOTER_IS_MISSING.value)
        
    def all_links(self):
        self.browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        links = self.browser.find_elements(*MPL.urls)
        for i in links:
            links_list.append(i.get_attribute('href'))

    def link_request(self):
        count_failed_pages = 0
        for link in links_list:
            responce = requests.get(link)
            if responce.status_code != expected_status_code:
                failed_pages = open("FailedPages.txt", "a+")
                failed_pages.write(str(link) + ' ' + str(responce.status_code) + '\n')
                failed_pages.close()
                count_failed_pages += 1
            else:
                continue
        assert count_failed_pages == 0, GEM.WRONG_STATUS_CODE.value

    def adress_bar(self):
        count_failed_urls = 0
        for link in links_list:
            self.browser.get(link)
            if link != self.browser.current_url:
                failed_urls = open("FailedUrls.txt", "a+")
                failed_urls.write(str(link) + ' != ' + str(self.browser.current_url) + '\n')
                failed_urls.close()
                count_failed_urls += 1
            else:
                continue
        assert count_failed_urls == 0, GEM.WRONG_URL.value
