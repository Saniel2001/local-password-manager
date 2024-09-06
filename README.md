# Python Password Manager

Welcome to the **Python Password Manager** — your personal vault for securely managing passwords, powered by the robust combination of **Python** and **MariaDB**. Whether you're tired of forgetting passwords or juggling dozens of them, this tool simplifies your digital life with cutting-edge security built right in.

At its core, the password manager leverages **PBKDF2** (Password-Based Key Derivation Function 2) to transform your **MASTER PASSWORD** and a **DEVICE SECRET** (a unique code tied to your device) into a powerful 256-bit encryption key. This key acts as the ultimate lock-and-key system, ensuring that your passwords are safely encrypted using **AES-256**, one of the most trusted encryption standards today.

With this password manager, your sensitive information is locked away in a local database that only you can access — no cloud storage, no third-party access — just **you and your securely encrypted data**.

Plus, with a command-line interface that’s easy to use and lightning-fast, managing your passwords is not only secure but also fun and efficient. Take control of your digital security while exploring the exciting world of encryption and databases!

---

## Features
- Strong AES-256 encryption for password security.
- User-friendly command-line interface for adding, retrieving, and generating passwords.
- Secure storage of credentials in a local MariaDB database.
- Copy passwords directly to the clipboard using [Pyperclip](https://pypi.org/project/pyperclip/).
  
---

## Table of Contents
- [Installation](#installation)
  - [Linux](#linux)
  - [Windows](#windows)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Adding Entries](#adding-entries)
  - [Retrieving Entries](#retrieving-entries)
  - [Generating Passwords](#generating-passwords)

---

## Installation

### Requirements:
- **Python 3.x**
- **MariaDB**
- [Pyperclip](https://pypi.org/project/pyperclip/) (for clipboard functionality)

### Linux

1. **Install Python Requirements:**
   ```bash
   sudo apt install python3-pip
   pip install -r requirements.txt
   ```

2. **Install MariaDB:**
   ```bash
   sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db
   sudo add-apt-repository 'deb http://ftp.osuosl.org/pub/mariadb/repo/5.5/ubuntuprecise main'
   sudo apt-get update
   sudo apt-get install mariadb-server
   ```

3. **Create MariaDB User:**
   - Login as root:
     ```bash
     sudo mysql -u root
     ```
   - Create a user:
     ```sql
     CREATE USER 'pm'@localhost IDENTIFIED BY 'password';
     ```
   - Grant necessary privileges:
     ```sql
     GRANT ALL PRIVILEGES ON *.* TO 'pm'@localhost IDENTIFIED BY 'password';
     ```

4. **Pyperclip Fix (if needed):**
   If you encounter a "not implemented error", follow [this guide](https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error).

### Windows

1. **Install Python Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install MariaDB:**
   Follow [this guide](https://www.mariadbtutorial.com/getting-started/install-mariadb/) for installation on Windows.

3. **Create MariaDB User:**
   - Navigate to the MariaDB bin directory:
     ```bash
     C:\Program Files\MariaDB\bin
     ```
   - Login as root:
     ```bash
     mysql.exe -u root -p
     ```
   - Create a user:
     ```sql
     CREATE USER 'pm'@localhost IDENTIFIED BY 'password';
     ```
   - Grant privileges:
     ```sql
     GRANT ALL PRIVILEGES ON *.* TO 'pm'@localhost IDENTIFIED BY 'password';
     ```

---

## Configuration

Before using the password manager, you need to configure it by setting up a **MASTER PASSWORD**.

1. **Create Configuration:**
   Run the following command to set up the MASTER PASSWORD and generate the DEVICE SECRET. This also creates the necessary database and tables.
   ```bash
   python config.py make
   ```

2. **Delete Configuration:**
   Warning: This will permanently delete all saved passwords.
   ```bash
   python config.py delete
   ```

3. **Remake Configuration:**
   This will delete the existing setup and create a new configuration.
   ```bash
   python config.py remake
   ```

---

## Usage

After configuration, you can use the password manager to add, retrieve, or generate passwords. Below are the common commands:

### Command Help
```bash
python pm.py -h
```
This displays all available options for adding, retrieving, and generating passwords.

### Adding Entries
To add a new entry for a site:
```bash
python pm.py add -s mysite -u mysite.com -e hello@email.com -l myusername
```

### Retrieving Entries
- Retrieve all entries:
  ```bash
  python pm.py extract
  ```
- Retrieve entries by site name:
  ```bash
  python pm.py e -s mysite
  ```
- Retrieve a specific entry by site name and username:
  ```bash
  python pm.py e -s mysite -l myusername
  ```
- Copy the password of a specific entry to the clipboard:
  ```bash
  python pm.py e -s mysite -l myusername --copy
  ```

### Generating Passwords
To generate a random password and copy it to the clipboard:
```bash
python pm.py g --length 15
```

---

## License
This project is licensed under the [MIT License](LICENSE.md).

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you'd like to improve the code or documentation.
