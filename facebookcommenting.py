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
time.sleep(3)
#comment_box = driver.find_element_by_class_name('_4-h7 _5qtn fbReactComposerAttachmentSelector_STATUS').send_keys(Keys.ENTER)
driver.find_element_by_class_name('_5qtp').click()
time.sleep(6)
user = driver.find_element_by_xpath('//*[@id="js_1e"]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div')
user.click()
user.send_keys(post)
driver.find_element_by_class_name('_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft').click()
