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
def visitSites():
    driver = getSeleniumDriver()
    driver.get("https://facebook.com")
    driver.get("https://google.com")
    driver.get("https://reddit.com")
    driver.get("https://example.com")
    time.sleep(5)
    driver.close()
    driver.quit()
def setDate(newDate):
    formatted_date = newDate.strftime("%d-%m-%y")
    output = vboxCommands.vboxRunCommand(VMName,"C:\\Windows\\System32\\cmd.exe", ["/c" , "date", formatted_date], VMUsername,VMPassword,15000)
    if output.returncode != 0:
        print("setting time timed out")
        exit(-1)
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
    currentDate = datetime.datetime.now().date()
    setDate(currentDate)
    print("Getting current history amount")
    print(f"There are currently {getHistory()} history entries")
    print("Visiting websites")
    visitSites()
    currentCount=getHistory()
    print(f"There are currently {currentCount} history entries")
    print(f"Current date: {currentDate}")
    for i in range(5,200,5):
        newDate= currentDate + datetime.timedelta(days=i)
        setDate(newDate)
        print(f"Current set date is {newDate}, {i} days from now")
        if checkHistory(currentCount,i)==1:
            print(f"After {i} days the history count changed from {currentCount} to {getHistory()}")
            break
    print("Done")       
    setDate(currentDate)

if __name__=="__main__":
    main()