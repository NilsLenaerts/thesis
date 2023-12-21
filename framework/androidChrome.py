import baseClasses
import windowsEnv
import chromeTargetAndroid
import androidEnv
import datetime
import time

def main():
    env = androidEnv.AndroidEnvironment()
    target = chromeTargetAndroid.Chrome(env)

    target.cleanArtifacts()

    #populate the database with artifacts so that the program has something to detect getting removed
    target.setupArtifacts()
    time.sleep(10)

    currentCount = target.getArtifactCount()
    currentDate = datetime.datetime.now()

    print(f"Currently {currentCount} entries in the database")
    print(f"Current date: {currentDate}")

    #starting x days from now, 
    for i in range(90,200,1):
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
