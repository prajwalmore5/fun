from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome('E:\Work\Praxis posters\chromedriver.exe')
driver.get("https://www.twitter.com")

login = '//*[@id="doc"]/div/div[1]/div[1]/div[2]/div[2]/div/a[2]'
login_page = driver.find_element_by_xpath(login).click()
time.sleep(3)

driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) > input').send_keys('username')
#driver.find_element_by_name('js-username-field email-input js-initial-focus').send_keys('youonlyliveonce1998yolo@gmail.com')

driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input').send_keys('password')
#driver.find_element_by_name('js-password-field').send_keys('youonlyliveonce')

driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input').send_keys(Keys.ENTER)
time.sleep(3)

post = input("Enter tweet here.")

#comment_box = driver.find_element_by_class_name('_4-h7 _5qtn fbReactComposerAttachmentSelector_STATUS').send_keys(Keys.ENTER)
driver.find_element_by_css_selector('#tweet-box-home-timeline').send_keys(post)
driver.find_element_by_css_selector('#timeline > div.timeline-tweet-box > div > form > div.TweetBoxToolbar > div.TweetBoxToolbar-tweetButton.tweet-button > button > span.button-text.tweeting-text').click()
