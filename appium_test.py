import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
import json

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='934814e7',
    language='en',
    locale='US',
    appPackage= "com.android.chrome",
    appActivity= "com.google.android.apps.chrome.Main",
    intentCategory= "android.intent.category.LAUNCHER",
    intentAction= "android.intent.action.MAIN",
    noReset=True,
    disableWindowAnimation=True,
    waitForIdleTimeout=100,
    forceAppLaunch=True,
    ChromedriverArgsOption = ["--user-data-dir '/data/data/com.android.chrome/app_chrome/'"]
)


options = UiAutomator2Options().load_capabilities(capabilities)
appium_server_url = 'http://localhost:4723'
driver = webdriver.Remote(appium_server_url, options=options)
driver.get('https://reddit.com')
time.sleep(1)

tabs = driver.find_element(by=AppiumBy.ID,value='com.android.chrome:id/tab_switcher_button')
tabs.click()
time.sleep(1)

close = driver.find_elements(by=AppiumBy.ID,value='com.android.chrome:id/action_button')
for button in close:
    button.click()
time.sleep(5)
driver.terminate_app('com.android.chrome')
driver.quit()



#//android.widget.ImageButton[@content-desc="Switch or close tabs"]
#com.android.chrome:id/tab_switcher_button