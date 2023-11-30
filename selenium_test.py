from selenium import webdriver
import time


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/Users/user/AppData/Local/Google/Chrome/User Data/")
driver = webdriver.Remote(
   command_executor='http://192.168.56.101:4444/wd/hub',
   options=options
)
try:
    driver.get_log('driver')
    driver.get("https://facebook.com")
    driver.get("http://example.com")
    driver.get("https://uhasselt.be")
    time.sleep(1)
finally:
    driver.close()
    driver.quit()