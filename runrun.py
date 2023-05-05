
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Define the capabilities for the LambdaTest platform
options = webdriver.ChromeOptions()
options.browser_version = "112.0"
options.platform_name = "Windows 11"
lt_options = {}
lt_options["username"] = "sandhyas"
lt_options["accessKey"] = "Z9BgK71LnJEzw5WxFHVWT7sALiJMh9HklABf7WMMX2hyJ4BS4u"
lt_options["project"] = "test"
lt_options["build"] = "build23"
lt_options["name"] = "testing selenium in lambda"
lt_options["selenium_version"] = "4.8.0"
lt_options["w3c"] = True
lt_options["plugin"] = "python-python"
options.set_capability('LT:Options', lt_options)

# Define the URL for the LambdaTest Selenium grid
hub_url = "https://hub.lambdatest.com/wd/hub"

# Create a remote driver instance using the capabilities and URL
driver = webdriver.Remote(
    command_executor=hub_url,
    options=options
)

# Navigate to Google and print the page title




driver.get("https://accounts.lambdatest.com/")

uname = driver.find_element(By.ID,"email")
uname.send_keys("sandhyas@lambdatest.com")
time.sleep(2)

pswd = driver.find_element(By.ID,"password")
pswd.send_keys("Lambdatest23@")
time.sleep(2)

submit = driver.find_element(By.ID,"login-button")
submit.send_keys(Keys.ENTER)

time.sleep(30)





# Close the browser
driver.quit()
