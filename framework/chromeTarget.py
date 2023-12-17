import baseClasses
import time
import history

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

    def getArtifact(self):

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
        self.environment.getFile(self.historyPath)
        return history.parseHistory("./tmp/History")

    def createArtifact(self,timeout):
        driver = self.environment.getAutomationDriver(args="user-data-dir=/Users/user/AppData/Local/Google/Chrome/User Data/")
        driver.get("http://example.com")
        time.sleep(timeout)
        driver.close() 
        driver.quit()
        time.sleep(0.1)
    
    def cleanArtifacts(self):
        print(f"removing history database")
        self.environment.removeFile(self.historyPath)

    def setupArtifacts(self):
        print(f"setting up artifacts")
        driver = self.environment.getAutomationDriver(args="user-data-dir=/Users/user/AppData/Local/Google/Chrome/User Data/")
        try:
            driver.get("https://facebook.com")
            time.sleep(1)
            driver.get("https://reddit.com")
            time.sleep(1)
            driver.get("https://google.com")
            time.sleep(1)
            driver.get("https://kuleuven.be")
            time.sleep(1)
        except Exception as e:
            print(f"error occured {e}")
            driver.close()
            exit(1)
        driver.close()
        driver.quit()

