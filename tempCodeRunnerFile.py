from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
brow = webdriver.Chrome()
brow.get('https://mos.ru')

try:
    brow.find_element(By.ID, 'ьа3')
except NoSuchElementException:
    print('her')