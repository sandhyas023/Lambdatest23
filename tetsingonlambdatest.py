from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Set up the LambdaTest options

user = "sandhyas"
accesskey = "Z9BgK71LnJEzw5WxFHVWT7sALiJMh9HklABf7WMMX2hyJ4BS4u"
grid_Url = "@hub.lambdatest.com/wd/hub"
url = f"http://{user}:{accesskey}{grid_Url}"
lt_options = {
    "username": "sandhyas",
    "accesskey": "Z9BgK71LnJEzw5WxFHVWT7sALiJMh9HklABf7WMMX2hyJ4BS4u",
    "project": "Untitled",
    "selenium_version": "4.8.0",
    "w3c": True,
    "plugin": "python-python"
}

# Set up the Chrome options
chrome_options = ChromeOptions()
chrome_options.browser_version = "112.0"
chrome_options.platform_name = "Windows 11"
chrome_options.set_capability('LT:Options', lt_options)

# Set up the remote driver
driver = webdriver.Remote(
    command_executor=url,
    desired_capabilities=chrome_options.to_capabilities()
)

# Open a webpage
driver.get("https://www.google.com")

# Close the driver
driver.quit()
