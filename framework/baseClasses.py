class BaseEnvironment:
    def __init__(self):
        self.envName="environment"

    def printName(self):
        print(self.envName)

    def getFile(self, path):
        print(f"getting file: {path}")
        raise NotImplementedError()
    
    def setDate(self, date):
        raise NotImplementedError()
    
    def getAutomationDriver():
        raise NotImplementedError()
    
    def removeFile(self):
        raise NotImplementedError

class TargetApplication:
    def __init__(self, environment):
        self.targetName="target application"
        self.environment=environment
    
    def printName(self):
        print(self.targetName)

    def getArtifact(self,timeout):
        print(f"getting {self.targetName} artifact in the {self.environment.envName} env")
        raise NotImplementedError()
    
    def getAutomationDriver(self):
        raise NotImplementedError()
    
    def cleanArtifacts(self):
        raise NotImplementedError()
    
    def setupArtifacts(self):
        raise NotImplementedError()
    
    def getArtifactCount(self):
        raise NotImplementedError()