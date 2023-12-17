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
    while(machineName in vboxGetRunningVMs()):
        #print(vboxCommands.vboxGetRunningVMs())    
        print("waiting for full shutdown",end="\r")
        time.sleep(0.500)
    print()
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
        #wait for guest execution service
        print("waiting for complete startup")
        time.sleep(20)
    
    return output.returncode

def vboxGetFile(machineName, guestPath, hostPath,username, password):
    command = ["VBoxManage", "guestcontrol" , machineName, "copyfrom", guestPath,hostPath, f"--username={username}", f"--password={password}"]
    output = subprocess.run(command,capture_output=True)
    if "guest execution service is not ready" in output.stderr.decode("utf-8"):
        print("Machine not fully on retrying in 5 sec")
        time.sleep(5)
        output = vboxGetFile(machineName,guestPath,hostPath, username, password)
        return output
    if debug:
        printOutput(output)
    return output.returncode

def vboxRemoveFile(machineName, guestPath,username, password):
    command = ["VBoxManage", "guestcontrol" , machineName, "rm", guestPath, f"--username={username}", f"--password={password}"]
    output = subprocess.run(command,capture_output=True)
    if "guest execution service is not ready" in output.stderr.decode("utf-8"):
        print("Machine not fully on retrying in 5 sec")
        time.sleep(5)
        output = vboxGetFile(machineName,guestPath, username, password)
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
def vboxRunCommand(machineName, commandPath, args, username, password, timeout=0):
    command = ["VBoxManage", "guestcontrol" , machineName, "run", f"--exe={commandPath}", f"--username={username}", f"--password={password}", f"--timeout={timeout}", "--"] + args
    output = subprocess.run(command,capture_output=True)
    if debug:
        print(output)
    return output
    

if __name__=="__main__":
    debug=1
    vboxShutDownMachine("Windows10")
    vboxTimeOffset("Windows10",0)
    #vboxTimeOffset("Windows 10")
    vboxStartMachine("Windows10")
    vboxGetRunningVMs()
    #vboxGetFile("Windows10","/Users/User/AppData/Local/Google/Chrome/User Data/Default/History", "./","user","user123")
    
    
    #vboxShutDownMachine("Windows10")
