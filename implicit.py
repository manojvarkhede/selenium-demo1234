import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

driver.implicitly_wait(10)

text = driver.find_element(By.XPATH,'//*[@id="start"]/button').click()
text = driver.find_element(By.XPATH,'//*[@id="finish"]/h4').text
print("Text:",text)

