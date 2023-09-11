import paramiko
import hashlib
import os
import getpass

hostname = '192.168.1.102'
port = 22
username = input('Enter the Windows username: ') or 'sai'
print(f"Username is {username}")
password = getpass(input("Enter the Windows password: "))


network_location = r'\\192.168.1.102\shareDocs'


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, port=port, username=username, password=password)

try:

    create_network_location_command = f'net use Z: {network_location}'
    stdin, stdout, stderr = ssh.exec_command(create_network_location_command)
    print(stdout.read().decode())


    files_to_create = ['file1.txt', 'file2.txt', 'file3.txt']
    for file_name in files_to_create:
        file_path = os.path.join(network_location, file_name)
        with open(file_path, 'w') as f:
            f.write('This is a sample file.')

    print("Files created")


    md5sums = {}
    for file_name in files_to_create:
        file_path = os.path.join(network_location, file_name)
        with open(file_path, 'rb') as f:
            data = f.read()
            md5sum = hashlib.md5(data).hexdigest()
            md5sums[file_name] = md5sum

    print("MD5 sums calculated")

    for file_name, md5sum in md5sums.items():
        print(f"File: {file_name}, MD5: {md5sum}")


    for file_name in files_to_create:
        file_path = os.path.join(network_location, file_name)
        delete_command = f'del /f /q "{file_path}"'
        stdin, stdout, stderr = ssh.exec_command(delete_command)
        print(stdout.read().decode())
        print(f"Deleted file: {file_path}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:

    ssh.close()


