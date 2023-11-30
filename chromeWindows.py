import vboxCommands
import selenium
import history
import datetime
import time
VMName="Windows10"
VMUsername="user"
VMPassword="user123"
VMIP="192.168.56.101"

debugPrints=1

def getSeleniumDriver():
    options = selenium.webdriver.ChromeOptions()
    options.add_argument("user-data-dir=/Users/user/AppData/Local/Google/Chrome/User Data/")
    driver = selenium.webdriver.Remote(
    command_executor=f'http://{VMIP}:4444/wd/hub',
    options=options
    )
    return driver
def getHistory():
    vboxCommands.vboxGetFile(VMName,"/Users/User/AppData/Local/Google/Chrome/User Data/Default/History", "./tmp/",VMUsername,VMPassword)
    return history.parseHistory("./tmp/History")
def visitSites():
    driver = getSeleniumDriver()
    driver.get("https://facebook.com")
    driver.get("https://google.com")
    driver.get("https://reddit.com")
    driver.get("https://example.com")
    time.sleep(5)
def setDate(newDate):
    vboxCommands.vboxRunCommand(VMName,"C:\\Windows\\System32\\cmd.exe", ["runas", "/user:Administrator" , "date", "26/11/2024"], VMUsername,VMPassword,0)

def checkHistory(currentCount):
    driver = getSeleniumDriver()
    driver.get("http://example.com")
    time.sleep(20)
    if getHistory() < currentCount:
        return 1
    return 0


def main():
    print("Testing data rollover for chrome on windows10")
    print("starting VM")
    vboxCommands.vboxStartMachine(VMName)
    print("Getting current history amount")
    print(f"There are currently {getHistory()} history entries")
    print("Visiting websites")
    visitSites()
    currentCount=getHistory()
    print(f"There are currently {currentCount} history entries")
    currentDate = datetime.datetime.now().date()
    print(f"Current date: {currentDate}")
    for i in range(100,__step=5):
        newDate= currentDate + datetime.timedelta(days=i)
        setDate(newDate)
        print(f"Current set date is {newDate}",end="\r")
        if checkHistory:
            print(f"After {i} days the history count changed from {currentCount} to {getHistory()}")
            break
    print("Done")       


if __name__=="__main__":
    main()