from paramiko import SSHClient
import paramiko
import sqlite3
import androidEnv
import datetime



def setDate(newDate):
        #MMDDhhmm[[CC]YY][.ss]
        formatted_date= newDate.strftime("%m%d%H%M%Y.%S")
        print(formatted_date)

android = androidEnv.AndroidEnvironment()
android.setDate(datetime.datetime.now())
android.getFile("/data/data/com.android.chrome/app_chrome/Default/History")



exit(0)
remote_host = '192.168.56.101'
remote_username = 'user'
remote_password = 'user123'
remote_database_path = 'C:\\'
client = SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(remote_host, username=remote_username, password=remote_password)
client.exec_command('start chrome wikipedia.com')

sftp_client = client.open_sftp()
remote_file = sftp_client.open('C:\\Users\\user\\Desktop\\test.txt')
try:
    for line in remote_file:
        # process line
        print(line)
finally:
    remote_file.close()
