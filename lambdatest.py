from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://accounts.lambdatest.com/"

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

uname = driver.find_element(By.ID,"email")
uname.send_keys("sandhyas@lambdatest.com")
time.sleep(2)

pswd = driver.find_element(By.ID,"password")
pswd.send_keys("Lambdatest23@")
time.sleep(2)

submit = driver.find_element(By.ID,"login-button")
submit.send_keys(Keys.ENTER)

time.sleep(30)



