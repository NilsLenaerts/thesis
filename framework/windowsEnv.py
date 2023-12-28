import baseClasses
import vboxCommands
import os
from selenium import webdriver
import datetime

class WindowsEnvironment(baseClasses.BaseEnvironment):
    def __init__(self):
        #set the vm name, user and password
        self.envName="Windows 10"
        self.VM_NAME="Windows10"
        self.VM_USERNAME="user"
        self.VM_PASSWORD="user123"
        self.VM_IPADDR="192.168.56.101"
        #start vm when class is created and sets time to today
        vboxCommands.vboxStartMachine("Windows10")
        self.setDate(datetime.datetime.now().date())
    
    def getFile(self, path):
        if not os.path.exists("tmp/"):
            os.makedirs("tmp")
        file = vboxCommands.vboxGetFile(self.VM_NAME, path, "./tmp/",self.VM_USERNAME,self.VM_PASSWORD)
        return file
        return super().getFile(path)
    
    def setDate(self, newDate):
        formatted_date = newDate.strftime("%d-%m-%y")
        output = vboxCommands.vboxRunCommand(self.VM_NAME,"C:\\Windows\\System32\\cmd.exe", ["/c" , "date", formatted_date], self.VM_USERNAME,self.VM_PASSWORD,15000)
        if output.returncode != 0:
            print("setting time timed out")
            raise TimeoutError()
    
    def removeFile(self,path):
        vboxCommands.vboxRemoveFile(self.VM_NAME,path, self.VM_USERNAME, self.VM_PASSWORD)
        