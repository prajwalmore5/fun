from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('E:\Work\Praxis posters\chromedriver.exe')
driver.get('https://web.whatsapp.com/')

name = input('enter name')
msg = input('enter message')
count = int(input('enter count'))

input('Enter anything after scanning QR code')

driver.find_element_by_class_name('_2MSJr').send_keys(name)
driver.find_element_by_class_name('_2MSJr').send_keys(Keys.ENTER)


msg_box = driver.find_element_by_class_name('_2S1VP')
for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('_35EW6')
    driver.find_element_by_class_name('_35EW6').send_keys(Keys.ENTER)
