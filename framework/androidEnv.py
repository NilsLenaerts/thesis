import datetime
import baseClasses
import os
import subprocess

import adb_shell
from adb_shell.adb_device import AdbDeviceTcp, AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner

class AndroidEnvironment(baseClasses.BaseEnvironment):

    def __init__(self):
        self.envName="Android"
        self.device = self.getAdbSession()
        self.setDate(datetime.datetime.now())
        

    def getAdbSession(self):
        subprocess.run(["adb", "kill-server"])
        adbkey = '/home/nils/.android/adbkey'
        with open(adbkey) as f:
            priv = f.read()
        with open(adbkey + '.pub') as f:
            pub = f.read()
        signer = PythonRSASigner(pub, priv)
        device = AdbDeviceUsb()
        device.connect(rsa_keys=[signer], auth_timeout_s=0.1)
        print("got device")
        return device
    
    def setDate(self,newDate):
        #MMDDhhmm[[CC]YY][.ss]
        #device = self.getAdbSession()
        device = self.device
        formatted_date= newDate.strftime("%m%d%H%M%Y.%S")
        print("setting date")
        device.shell(f"su -c toybox date {formatted_date}")
        
        

    def getFile(self,path):
        #device = self.getAdbSession()
        device = self.device
        if not os.path.exists("tmp/"):
            os.makedirs("tmp")
        file_name=path.split('/')[-1]
        tmp_path = f"/sdcard/tmp/{file_name}"
        device.shell(f"su -c cp {path} {tmp_path}")
        device.pull(tmp_path,f"./tmp/{file_name}")
        
        
        #"su -c cp /data/data/com.android.chrome/app_chrome/Default/History /sdcard/tmp/History"
    
    def removeFile(self,path):
        #Be very carefull here
        #device = self.getAdbSession()
        device = self.device
        device.shell(f"su -c rm /data/data/com.android.chrome/app_chrome/Default/History")
        
        
    def closeSession(self):
        self.device.close()   
        #return super().removeFile()
    def createSession(self):
        if self.device.available:
            return
        self.device = self.getAdbSession()