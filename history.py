import paramiko
import sqlite3
import shutil
# SSH connection parameters
ssh_host = "192.168.0.141"
ssh_host = "192.168.56.101"
ssh_port = 22
ssh_username = "user"
ssh_password = "user123"

def getHistoryCount():
    # Local directory to save the Chrome history file
    local_dir = "./"

    # Remote Chrome profile directory
    chrome_profile_dir = "C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\"

    # Establish an SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_host, ssh_port, ssh_username, ssh_password)

    # Path to the Chrome history file on the remote server
    remote_history_file = f"{chrome_profile_dir}History"

    # Copy the history file from the remote server to the local directory
    local_history_file = local_dir + "History"
    shutil.copyfileobj(ssh.open_sftp().file(remote_history_file), open(local_history_file, 'wb'))

    # Connect to the local copy of the Chrome history database
    
    # Close the SSH connection
    ssh.close()

    count = parseHistory(local_history_file)
    return count
def parseHistory(historyfile):
    conn = sqlite3.connect(historyfile)
    cursor = conn.cursor()

    # Query the history data
    cursor.execute("SELECT url, title, visit_count FROM urls")
    history_data = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Process and print the history data
    count = 0
    for row in history_data:
        count += 1
        url, title, visit_count = row
        print(f"URL: {url}")
        #print(f"Title: {title}")
        #print(f"Visit Count: {visit_count}")
        #print("\n")
    print(f"Amount of history entries is {count}")

def openChrome(url):
    # Establish an SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_host, ssh_port, ssh_username, ssh_password)

    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(f'"/Users/user/Desktop/chrome - Shortcut.lnk" {url}')
    print(ssh_stdout)
    ssh.close()

if __name__=="__main__":
    openChrome()
    getHistoryCount()