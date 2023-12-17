import framework.vboxCommands as vboxCommands
from selenium import webdriver
import framework.history as history
import datetime
import time
VMName="Windows10"
VMUsername="user"
VMPassword="user123"
VMIP="192.168.56.101"

debugPrints=1

def getSeleniumDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=/Users/user/AppData/Local/Google/Chrome/User Data/")
    driver = webdriver.Remote(
    command_executor=f'http://{VMIP}:4444/wd/hub',
    options=options
    )
    return driver
def getHistory():
    vboxCommands.vboxGetFile(VMName,"/Users/User/AppData/Local/Google/Chrome/User Data/Default/History", "./tmp/",VMUsername,VMPassword)
    return history.parseHistory("./tmp/History")
def visitSites(url):
    driver = getSeleniumDriver()
    driver.get(url)
    time.sleep(2)
    driver.close()
    driver.quit()

def checkHistory(currentCount, cycle):
    driver = getSeleniumDriver()
    driver.get("http://example.com")
    print("waiting for update in history")
    sleeptime = 20
    if cycle > 25:
        sleeptime = 30
    if cycle > 50:
        sleeptime = 40
    if cycle > 100:
        sleeptime = 50
    time.sleep(sleeptime)
    driver.close()
    driver.quit()
    time.sleep(2)
    print("done waiting")
    if getHistory() < currentCount:
        print("smaller")
        return 1
    return 0


def main():
    print("Testing data rollover for chrome on windows10")
    print("starting VM")
    vboxCommands.vboxStartMachine(VMName)
    print("Getting current history amount")
    print(f"There are currently {getHistory()} history entries")
    print("Visiting websites")
    for i in range(0,400,2):
        visitSites(f"https://forums.virtualbox.org/viewtopic.php?t={i}")
        if i%50 ==0:
            getHistory()
    print("Done")       

if __name__=="__main__":
    main()