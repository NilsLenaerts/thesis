import vboxCommands
import time
import history

vmName = "Windows10"
vmUser = "user"
vmPass = "user123"


if __name__=="__main__":

    vboxCommands.vboxGetFile(vmName,"/Users/User/AppData/Local/Google/Chrome/User Data/Default/History", "./",vmUser,vmPass)
    history.parseHistory("./History")
    #history.openChrome("https://docs.python.org/3/library/subprocess.html")
    #history.openChrome("https://unix.stackexchange.com/questions/238180/execute-shell-commands-in-python")
    #vboxCommands.vboxGetFile(vmName,"/Users/User/AppData/Local/Google/Chrome/User Data/Default/History", "./",vmUser,vmPass)
    #history.parseHistory("./History")

    exit(0)
    print(vboxCommands.vboxGetRunningVMs())    

    vboxCommands.vboxStartMachine(vmName)
    vboxCommands.vboxGetFile(vmName,"/Users/User/AppData/Local/Google/Chrome/User Data/Default/History", "./",vmUser,vmPass)
    history.parseHistory("./History")
    vboxCommands.vboxRunCommand(vmName,"/Program Files/Google/Chrome/Application/chrome.exe", "reddit.com", vmUser, vmPass, 10000)
    vboxCommands.vboxGetFile(vmName,"/Users/User/AppData/Local/Google/Chrome/User Data/Default/History", "./",vmUser,vmPass)
    history.parseHistory("./History")

    vboxCommands.vboxShutDownMachine(vmName)
    print(vboxCommands.vboxGetRunningVMs())    