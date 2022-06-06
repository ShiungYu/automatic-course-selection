from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from requests import get
import time
import threading
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
url = 'https://ais.ntou.edu.tw/Default.aspx'
#driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
email = driver.find_element_by_id("M_PORTAL_LOGIN_ACNT")
password = driver.find_element_by_id("M_PW")
email.send_keys('輸入學號')
password.send_keys('輸入密碼')
login = driver.find_element_by_xpath('/html/body/header/section/div[3]/div/form/div[5]/span[2]/input')
login.click()

driver.switch_to.frame("menuFrame")
driver.find_element_by_xpath('/html/body/form/div[3]/table/tbody/tr[1]/td/div/div/table[1]/tbody/tr/td[4]/a').click()
time.sleep(0.5)
driver.find_element_by_xpath(
    '/html/body/form/div[3]/table/tbody/tr[1]/td/div/div/div/table[3]/tbody/tr/td[5]/a').click()
time.sleep(0.5)
driver.find_element_by_xpath(
    '/html/body/form/div[3]/table/tbody/tr[1]/td/div/div/div/div/table[2]/tbody/tr/td[6]/a').click()

driver.switch_to.default_content()
driver.switch_to.frame("mainFrame")
driver.find_element_by_xpath(
    "/html/body/form/div[3]/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table[1]/tbody/tr[1]/td/input[1]").send_keys(
    "輸入課號")
a = driver.find_element_by_xpath(
    "/html/body/form/div[3]/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table[1]/tbody/tr[1]/td/input[2]")
a.click()
time.sleep(0.5)
while (1):
    try:
        b = driver.find_element_by_xpath(
            "/html/body/form/div[3]/div/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td[2]/div/div/table/tbody/tr[2]/td[1]/a")
        b.click()
        print("click accepted")
    except:
        print("no click")
    try:
        driver.switch_to.alert.accept()
        print("alert accepted")
    except:
        print("no alert")
