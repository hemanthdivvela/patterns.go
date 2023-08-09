import os
import subprocess

j = r'192.168.1.100\pc1'



def create_network_path(drive_letter, server_share, username,):
    command = f"net use {drive_letter}: {server_share} /user:{username} "
    subprocess.run(command, shell=True)


def create_empty_file(file_path):
    with open(file_path, "w") as f:
        pass


def delete_file(file_path):
    if os.path.exists(file_path) and os.path.isfile(file_path):
        os.remove(file_path)
        print(f"Deleted file: {file_path}")
    else:
        print(f"File does not exist: {file_path}")


if __name__ == "__main__":
    network_drive_letter = "Z"  # Use a different drive letter
    network_server_share = j
    network_username = "YourUsername"

    file_to_create = f'{network_drive_letter}:\\ping 192.168.1.100'

    try:
        create_network_path(network_drive_letter, network_server_share, network_username, )
        print("Network path created.")

        file_to_create = f'{network_drive_letter}:\\ping 192.168.1.100'
        create_empty_file(file_to_create)
        print("Empty file created.")

        delete_file(file_to_create)
        print("File deleted.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Disconnect the network drive after the operations

        disconnect_command = f"net use {network_drive_letter}: /delete"
        subprocess.run(disconnect_command, shell=True)
