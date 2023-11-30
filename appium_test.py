from appium import webdriver
import time

APPIUM_HOST="192.168.56.101"
APPIUM_PORT=4723

import appium.options.windows as aw
opt = webdriver.WindowsOptions()

capabilities = {
    "platformName": 'Windows',
    "deviceName":'Windows10',
    "app":"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
}

driver = webdriver.Remote("http://{APPIUM_HOST}:{APPIUM_PORT}/wd/hub",)

driver.get("http://example.com")
time.sleep(20)
driver.close()



