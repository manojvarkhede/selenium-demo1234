import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://facebook.com")
driver.maximize_window()

inputname = driver.find_element(By.NAME, "email")
inputname.send_keys("manoj")
inputpass = driver.find_element(By.NAME,"pass")
inputpass.send_keys("123456")
btnlogin=driver.find_element(By.NAME,"login")
btnlogin.click()