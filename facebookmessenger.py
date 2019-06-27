from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome('E:\Work\Praxis posters\chromedriver.exe')
driver.get("https://www.facebook.com")
email = driver.find_element_by_name("email")
#username = input("Enter username")
email.send_keys('youonlyliveonce1998yolo@gmail.com')
password = driver.find_element_by_name("pass")
#passw = input("Enter password")
password.send_keys('password')
password.send_keys(Keys.ENTER)
post = input("Enter post here.")

input("disable notifications.")

loadhome = driver.find_element_by_css_selector('#u_0_c > a').click()
#comment_box = driver.find_element_by_class_name('_4-h7 _5qtn fbReactComposerAttachmentSelector_STATUS').send_keys(Keys.ENTER)
#select chat
driver.find_element_by_css_selector('#fbDockChatBuddylistNub > a').click()
#search user
user = input('enter user name')
driver.find_element_by_class_name('_58al').send_keys(user)
driver.find_element_by_class_name('_58al').send_keys(Keys.ENTER)
#send message
msg = input('enter message')
driver.find_element_by_class_name('_1mf _1mj').send_keys(msg)
driver.find_element_by_class_name('_1mf _1mj').send_keys(Keys.ENTER)

