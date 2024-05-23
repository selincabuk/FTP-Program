# FTP Client Application

This is a simple FTP client application with basic functions such as login, file upload/download, directory creation/deletion, file name change, and local/remote directory and file listing, using the Python programming language and PyQt5 for the GUI.

## Features

- Connect to an FTP server with a specified hostname, port, username, and password.
- Upload files to the server.
- Download files from the server.
- Delete files from the server.
- Rename files on the server.
- List files in the current directory on the server.

## Getting Started

### Prerequisites

- Python 3.x: Download and install from [python.org](https://www.python.org/).
- PyQt5: Install via pip.
    ```bash
    pip install pyqt5
    ```

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    ```
2. Navigate to the project directory:
    ```bash
    cd your-repo-name
    ```

### Running the Application

1. Open a command prompt or terminal window.
2. Navigate to the project directory if not already there.
3. Run the application script:
    ```bash
    python ftp_client.py
    ```

### Usage

1. **Connect to FTP Server**:
    - Enter the FTP server address, port, username, and password.
    - Click the "Connect" button to connect to the server.
2. **Upload File**:
    - Click the "Upload" button and choose a file to upload to the server.
3. **Download File**:
    - Double-click on a file in the list to download it.
4. **Delete File**:
    - Select a file from the list and click the "Delete" button to remove it from the server.
5. **Rename File**:
    - Select a file from the list.
    - Enter the new name in the "New Name" field and click the "Rename" button to rename the file on the server.
6. **Refresh File List**:
    - The file list is automatically updated after any operation. To manually refresh, reconnect to the server.

### Example

#### Starting the Application

```bash
python ftp_client.py

Connecting to the Server
Default server details are pre-filled for testing (ftp.dlptest.com with username dlpuser and password rNrKYTX9g7z3RgJRmxWuGHbeu).
Modify these details as needed and click "Connect".
Uploading a File
Click "Upload".
Select a file from your local machine to upload to the FTP server.
Downloading a File
Double-click on any file in the list to download it to your local machine.
Deleting a File
Select a file from the list.
Click the "Delete" button to remove the file from the FTP server.
Renaming a File
Select a file from the list.
Enter the new name in the "New Name" field.
Click "Rename" to rename the file on the FTP server
