import pytest
from pages.main_page import MainPage
from variables import *


def test_org_teh_resh(browser):
    page = MainPage(browser, url)
    page.open()
    page.header()
    page.footer()
    page.all_links()
    page.link_request()
    page.adress_bar()
