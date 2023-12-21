import baseClasses
import time
import history
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

class Chrome(baseClasses.TargetApplication):
    def __init__(self, environment):
        self.targetName="Google Chrome"
        self.environment = environment
        #set the path for the history file 
        if self.environment.envName == "Windows 10":
            self.historyPath = "/Users/User/AppData/Local/Google/Chrome/User Data/Default/History"
        elif self.environment.envName == "Android":
            self.historyPath = "/data/data/com.android.chrome/app_chrome/Default/History"
        else:
            print(f"Environment: {self.environment.envName} not implimented ")
            raise RuntimeError()
        
    def __del__(self):
        print(f"cleaning up {self.targetName}")

    def getAndroidDriver(self):
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
            newCommandTimeout=0,
            waitForIdleTimeout=100,
            forceAppLaunch=True,
            ChromedriverArgsOption = ["--user-data-dir '/data/data/com.android.chrome/app_chrome/'"]
        )


        options = UiAutomator2Options().load_capabilities(capabilities)
        appium_server_url = 'http://localhost:4723'
        driver = webdriver.Remote(appium_server_url, options=options)
        return driver
    def getArtifact(self):
        self.environment.createSession()
        print(f"getting {self.targetName} artifact in the {self.environment.envName} env")
        #if self.environment.envName == "Windows 10":
        #    filePath = "/Users/User/AppData/Local/Google/Chrome/User Data/Default/History"
        #elif self.environment.envName == "Android":
        #    filePath = "/data/data/com.android.chrome/app_chrome/Default/History"
        #else:
        #    print(f"Environment: {self.environment.envName} not implimented ")
        #    raise RuntimeError()
        return self.environment.getFile(self.historyPath)
    
    def getArtifactCount(self):
        self.environment.createSession()
        self.environment.getFile(self.historyPath)
        return history.parseHistory("./tmp/History")

    def createArtifact(self,timeout):
        self.environment.closeSession()
        driver = self.getAndroidDriver()
        driver.get("http://example.com")
        time.sleep(1)
        driver.get("http://example.com")
        #driver.swipe(530,530,530,1250,400)
        time.sleep(2)
        self.closeTabs(driver)
        #tabs = driver.find_element(by=AppiumBy.ID,value='com.android.chrome:id/tab_switcher_button')
        #tabs.click()
        #time.sleep(1)
        #
        #close = driver.find_elements(by=AppiumBy.ID,value='com.android.chrome:id/action_button')
        #for button in close:
        #    button.click()
        time.sleep(10)
        driver.background_app(5)
        time.sleep(5)
        driver.get("http://httpbin.org")
        time.sleep(2)
        #print(driver.get_window_size())
        driver.swipe(530,530,530,1250,400)

        time.sleep(100)
        driver.terminate_app('com.android.chrome')
        driver.quit()
        time.sleep(0.1)
    
    def cleanArtifacts(self):
        self.environment.createSession()
        print(f"removing history database")
        self.environment.removeFile(self.historyPath)

    def setupArtifacts(self):
        self.environment.closeSession()
        print(f"setting up artifacts")
        driver = self.getAndroidDriver()
        try:
            driver.get("https://facebook.com")
            time.sleep(1)
            driver.get("https://reddit.com")
            time.sleep(1)
            driver.get("https://google.com")
            time.sleep(1)
            driver.get("https://kuleuven.be")
            time.sleep(10)
            print("sending tabs request")
            #driver.tap()
            self.closeTabs(driver)
            #tabs = driver.find_element(by=AppiumBy.ID,value='com.android.chrome:id/tab_switcher_button')
            #tabs.click()
            #time.sleep(5)
            #print("sending close request")
            #
            #close = driver.find_elements(by=AppiumBy.ID,value='com.android.chrome:id/action_button')
            #for button in close:
            #    button.click()
        except Exception as e:
            print(f"error occured {e}")
            driver.terminate_app('com.android.chrome')
            exit(1)
        time.sleep(10)
        driver.terminate_app('com.android.chrome')
        driver.quit()

    def closeTabs(self,driver):
        tabs = driver.find_element(by=AppiumBy.ID,value='com.android.chrome:id/tab_switcher_button')
        tabs.click()
        time.sleep(5)
        driver.tap([(1017,158)],100)
        time.sleep(1)
        driver.tap([(559,440)],100)
        time.sleep(1)
        driver.tap([(800,1300)],100)
