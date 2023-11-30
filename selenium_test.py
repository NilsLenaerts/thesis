from selenium import webdriver
import time

future = 1
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/Users/user/AppData/Local/Google/Chrome/User Data/")
driver = webdriver.Remote(
   command_executor='http://192.168.56.101:4444/wd/hub',
   options=options
)
try:
    print(driver.get_log('driver'))
    driver.get("http://example.com")
    if future==0:
        driver.get("https://facebook.com")
        driver.get("https://google.com")
        driver.get("https://reddit.com")

    print(driver.get_log('driver'))
    print(driver.get_log('browser'))

    if future==1:
        time.sleep(30)
    else:
        time.sleep(5)
finally:
    driver.close()
    driver.quit()
