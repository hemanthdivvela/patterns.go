import os
from main import create_network_path, create_empty_file, delete_file
import pytest

# Fixture to provide a temporary folder for the test files
@pytest.fixture
def temp_folder(tmp_path):
    return tmp_path

def test_create_network_path(temp_folder):
    # Arrange
    drive_letter = "Z"
    server_share = r'192.168.1.100\pc1'
    username = "YourUsername"

    # Act
    create_network_path(drive_letter, server_share, username)

    # Assert (Check if the network path is created)
    assert os.path.exists(drive_letter + ":")
    # You might need to add more assertions here based on the expected outcome

def test_create_empty_file(temp_folder):
    # Arrange
    file_path = os.path.join(temp_folder, "test_file.txt")

    # Act
    create_empty_file(file_path)

    # Assert (Check if the file is created)
    assert os.path.exists(file_path)
    assert os.path.isfile(file_path)

def test_delete_file(temp_folder):
    # Arrange
    file_path = os.path.join(temp_folder, "test_file.txt")
    create_empty_file(file_path)

    # Act
    delete_file(file_path)

    # Assert (Check if the file is deleted)
    assert not os.path.exists(file_path)

# You can add more tests for different scenarios and edge cases

