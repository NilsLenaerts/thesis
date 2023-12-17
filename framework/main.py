#import vboxCommands
#import selenium
import baseClasses
import windowsEnv
import chromeTarget
import datetime


#vmName = "Windows10"
#vmUser = "user"
#vmPass = "user123"
#
#def test():
#    env = windowsEnv.WindowsEnvironment()
#    target = chromeTarget.Chrome(env)
#    env.printName()
#    target.printName()
#    target.createArtifacts()
#    target.getArtifact()


def main():
    #setup targets
    env = windowsEnv.WindowsEnvironment()
    target = chromeTarget.Chrome(env)

    #clean up target
    target.cleanArtifacts()

    #populate the database with artifacts so that the program has something to detect getting removed
    target.setupArtifacts()


    currentCount = target.getArtifactCount()
    currentDate = datetime.datetime.now().date()

    print(f"Currently {currentCount} entries in the database")
    print(f"Current date: {currentDate}")

    #starting x days from now, 
    for i in range(80,200,1):
        newDate= currentDate + datetime.timedelta(days=i)
        env.setDate(newDate)
        print(f"Current set date is {newDate}, {i} days from now")
        target.createArtifact(40)
        newCount = target.getArtifactCount()

        if newCount < currentCount:
            print(f"After {i} days the history count changed from {currentCount} to {newCount}")
            break
    print("Done") 
    


if __name__=="__main__":
    main()