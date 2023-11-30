import vboxCommands
import time
import history

vmName = "Windows10"
vmUser = "user"
vmPass = "user123"


if __name__=="__main__":
    
    vboxCommands.vboxTimeOffset(vmName, 0)
    vboxCommands.vboxStartMachine(vmName)
    time.sleep(10)
    history.openChrome("https://forums.virtualbox.org/viewtopic.php?t=104874")
    time.sleep(15)
    history.closeChrome()

    vboxCommands.vboxGetFile(vmName,"/Users/User/AppData/Local/Google/Chrome/User Data/Default/History", "./",vmUser,vmPass)
    history.parseHistory("./History")
    
    vboxCommands.vboxShutDownMachine(vmName)
    time.sleep(5)
    vboxCommands.vboxTimeOffset(vmName, 3600*24*220*1000)
    
    vboxCommands.vboxStartMachine(vmName)
    time.sleep(10)
    #vboxCommands.vboxRunCommand(vmName,"C:\\Windows\\System32\\cmd.exe", ["runas", "/user:Administrator" , "date", "26/11/2024"], vmUser,vmPass,0)
    vboxCommands.vboxRunCommand(vmName,"/Program Files/Google/Chrome/Application/chrome.exe", ["https://forums.virtualbox.org/viewtopic.php?t=104866"], vmUser, vmPass, 20000)
    vboxCommands.vboxRunCommand(vmName,"/Program Files/Google/Chrome/Application/chrome.exe", ["https://forums.virtualbox.org/viewtopic.php?t=104864"], vmUser, vmPass, 20000)
    vboxCommands.printOutput(vboxCommands.vboxRunCommand(vmName,"/Program Files/Google/Chrome/Application/chrome.exe", ["https://forums.virtualbox.org/viewtopic.php?t=104862"], vmUser, vmPass, 20000))
    
    vboxCommands.vboxGetFile(vmName,"/Users/User/AppData/Local/Google/Chrome/User Data/Default/History", "./",vmUser,vmPass)
    history.parseHistory("./History")
    vboxCommands.vboxShutDownMachine(vmName)
    vboxCommands.vboxTimeOffset(vmName, 0)
    #history.openChrome("https://www.formula1.com/en/racing/2023/Brazil.html")
    #time.sleep(10)
    #history.openChrome("https://unix.stackexchange.com/questions/238180/execute-shell-commands-in-python")
    #vboxCommands.vboxGetFile(vmName,"/Users/User/AppData/Local/Google/Chrome/User Data/Default/History", "./",vmUser,vmPass)
    #history.parseHistory("./History")
    exit(0)

    vboxCommands.vboxRunCommand(vmName,"/Program Files/Google/Chrome/Application/chrome.exe", "https://forums.virtualbox.org/viewtopic.php?t=104876", vmUser, vmPass, 10000)
    vboxCommands.vboxRunCommand(vmName,"/Program Files/Google/Chrome/Application/chrome.exe", "https://forums.virtualbox.org/viewtopic.php?t=104874", vmUser, vmPass, 10000)
    vboxCommands.vboxRunCommand(vmName,"/Program Files/Google/Chrome/Application/chrome.exe", "https://forums.virtualbox.org/viewtopic.php?t=104872", vmUser, vmPass, 10000)  
    vboxCommands.vboxRunCommand(vmName,"/Program Files/Google/Chrome/Application/chrome.exe", "https://forums.virtualbox.org/viewtopic.php?t=104866", vmUser, vmPass, 20000)
    vboxCommands.vboxRunCommand(vmName,"/Program Files/Google/Chrome/Application/chrome.exe", "https://forums.virtualbox.org/viewtopic.php?t=104864", vmUser, vmPass, 20000)
    vboxCommands.vboxRunCommand(vmName,"/Program Files/Google/Chrome/Application/chrome.exe", "https://forums.virtualbox.org/viewtopic.php?t=104862", vmUser, vmPass, 20000)  
    
    #

    history.openChrome("https://forums.virtualbox.org/viewtopic.php?t=104878")
    history.openChrome("https://forums.virtualbox.org/viewtopic.php?t=104876")
    history.openChrome("https://forums.virtualbox.org/viewtopic.php?t=104874")

    print(vboxCommands.vboxGetRunningVMs())    

    vboxCommands.vboxStartMachine(vmName)
    vboxCommands.vboxGetFile(vmName,"/Users/User/AppData/Local/Google/Chrome/User Data/Default/History", "./",vmUser,vmPass)
    history.parseHistory("./History")
    vboxCommands.vboxRunCommand(vmName,"/Program Files/Google/Chrome/Application/chrome.exe", "reddit.com", vmUser, vmPass, 10000)
    vboxCommands.vboxGetFile(vmName,"/Users/User/AppData/Local/Google/Chrome/User Data/Default/History", "./",vmUser,vmPass)
    history.parseHistory("./History")

    vboxCommands.vboxShutDownMachine(vmName)
    print(vboxCommands.vboxGetRunningVMs())    
