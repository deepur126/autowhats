# Whatsapp automation by Python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os

os.getcwd()
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 500)
print("%s"%driver.title)
print()

name = input("Enter name of user: ")

if (driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))):
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
else:
    search = driver.find_element_by_xpath('//span[@data-icon = "search"]')
    search.click()
    usr = driver.find_element_by_xpath('//label[@input = "text"]')
    usr.send_keys(name)
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

msg = input("Enter Message: ")

msg_box = driver.find_element_by_xpath('//div[@contenteditable = "true"]')
msg_box.send_keys(msg)

bt = driver.find_element_by_xpath('//span[@data-icon = "send"]')
bt.click()
time.sleep(2)
print("Message Sent.......")
time.sleep(10)

print( )
print("Driver exiting......")
driver.quit()
