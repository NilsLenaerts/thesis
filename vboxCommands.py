import virtualbox
import subprocess
import time
debug = 0

def printOutput(output):
    print('###############')
    print('Input:',output.args)
    print('Return code:', output.returncode)
    # use decode function to convert to string
    print('Output:',output.stdout.decode("utf-8"))
    print('Err:',output.stderr.decode("utf-8"))
def vboxTimeOffset(machineName, time):
    command = ["VBoxManage", "modifyvm", machineName, "--biossystemtimeoffset", str(time)]
    output = subprocess.run(command,capture_output=True)
    if debug:
        printOutput(output)
    return output.returncode

def vboxShutDownMachine(machineName):
    command = ["VBoxManage", "controlvm" , machineName, "shutdown"]
    output = subprocess.run(command,capture_output=True)
    if debug:
            printOutput(output)
    return output.returncode

def vboxStartMachine(machineName):
    command = ["VBoxManage", "startvm" , machineName, "--type=headless"]
    if machineName in vboxGetRunningVMs():
        print(f"Machine: {machineName} already running")
        return 0 
    output = subprocess.run(command,capture_output=True)
    if debug:
        printOutput(output)
    if output.returncode == 0:
        print("waiting for complete startup")
        time.sleep(10)
    
    return output.returncode

def vboxGetFile(machineName, guestPath, hostPath,userName, password):
    command = ["VBoxManage", "guestcontrol" , machineName, "copyfrom", guestPath,hostPath, f"--username={userName}", f"--password={password}"]
    output = subprocess.run(command,capture_output=True)
    if "guest execution service is not ready" in output.stderr.decode("utf-8"):
        print("Machine not fully on retrying in 5 sec")
        time.sleep(5)
        output = vboxGetFile(machineName,guestPath,hostPath, userName, password)
        return output
    if debug:
        printOutput(output)
    return output.returncode
def vboxGetRunningVMs():
    command = ["VBoxManage", "list", "runningvms"]
    output = subprocess.run(command,capture_output=True)
    if debug:
        printOutput(output)
    return output.stdout.decode("utf-8")

if __name__=="__main__":
    debug=0
    #vboxTimeOffset("Windows 10")
    vboxStartMachine("Windows10")
    vboxGetRunningVMs()
    vboxGetFile("Windows10","/Users/User/AppData/Local/Google/Chrome/User Data/Default/History", "./","user","user123")
    vboxShutDownMachine("Windows10")
