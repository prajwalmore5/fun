from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome('E:\Work\Praxis posters\chromedriver.exe')
driver.get("https://www.flipkart.com")

time.sleep(2)

driver.find_element_by_class_name('_2zrpKA').send_keys('username')
#driver.find_element_by_name('js-username-field email-input js-initial-focus').send_keys('username')

driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input').send_keys('password')
#driver.find_element_by_name('js-password-field').send_keys('password')

driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input').send_keys(Keys.ENTER)
time.sleep(3)
while (True):
    driver.get('https://www.flipkart.com/redmi-note-5-pro-black-64-gb/p/itmf2fc3xgmxnhpx?pid=MOBF28FTQPHUPX83&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_5&lid=LSTMOBF28FTQPHUPX83BUJJ2C&fm=SEARCH&iid=43c20924-e3da-4163-98ed-3965565bef97.MOBF28FTQPHUPX83.SEARCH&ppt=Homepage&ppn=Homepage&ssid=cmj1ofoyyo0000001537862396286&qH=286b43aac83aafdc')  
    #buy
    driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[2]/form/button').click()
    


    
               
        
               
               

    
    
