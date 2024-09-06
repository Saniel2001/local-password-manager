# First step in configuring would be creating a database and creating necessary tables inside
from utils.dbconfig import dbconfig
from getpass import getpass 
import hashlib
import string
import random 
import sys

from rich import print as printc
from rich.console import Console
console = Console()

def generateDeviceSecret(Length = 10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = Length))

def config():
    db = dbconfig()  # getting the database object

    cursor = db.cursor() # creating a cursor from where we can execute queries 

    try:
        cursor.execute("CREATE DATABASE pm") # "CREATE DATABASE" --> query to create a database
    except Exception as e:
        printc("[red][!] An error has occured while creating a database") 
        # with printc we can print stuff in the terminal with colors, we can modify them(bold, italics, etc.) using rich module
        console.print_exception(show_locals=True)
        sys.exit(0)
    printc("[green] [+] [/green] Database 'pm' created")
    # Creation of Database completed 

    # Creating Tables
    # We would have 2 tables in the database:
    # 1. One table stores the hash of the Master password
    # When the user enters the Master password, we will have to validate the Master password.
    # To validate the Master password we need to hash the Master password first and then store it in the database
    # So, this table will store the hash of the Master password and randomly generated 'Device Secret' (aka salt)
    
    # 2. The table where we will be inserting the new entries that the user enters into the password manager

    # 1st table (secrets table)
    query = "CREATE TABLE pm.secrets (masterkey_hash TEXT NOT NULL, device_secret TEXT NOT NULL)"
    res = cursor.execute(query)
    printc("[green] [+] [/green] Table 'secrets' created")

    # 2nd Table (entries table)
    query = "CREATE TABLE pm.entries (sitename TEXT NOT NULL, siteurl TEXT NOT NULL, email Text, username TEXT, password TEXT NOT NULL)"  # password --> encrypted not plain
    res = cursor.execute(query)
    printc("[green] [+] [/green] Table 'entries' created")


    # Final Step is to input the Master password and compute its hash value and then generate a 'device secret' and add these both into the 'secrets' table
    
    # We will be using the 'getpass' module to get the Master password from the user. It doesnt display the password as you are typing it.
    # It just keeps it hidden
    mp = ""
    while 1:
        mp = getpass("Choose a MASTER PASSWORD")
        # Ask the user to re-type the master password to ensure the correct Master Password and also ensure that the Master Password is not empty string
        if mp == getpass('Re-type Password') and mp != "":
            break 
        else:
            printc("[yellow] [-] Please try again. [/yellow]")

    # Hashing the Master Password
    # We will be using the SHA256 algorithm to hash the Master Password
    # We will be using the hashlib module to hash the Master Password
    # We will be using the hexdigest() method to get the hexadecimal representation of the hash
    # We will be using the encode() method to encode the Master Password into bytes
    # We will be using the sha256() method to hash the Master Password

    hashed_mp = hashlib.sha256(mp.encode()).hexdigest()
    printc("[green][+][/green] Generated hash of Master Password")

    # Generating a DEVICE SECRET (aka salt)
    ds = generateDeviceSecret()
    printc("[green][+][/green] Device Secret Generated")

    # Inserting the hashed_mp and device secret into the 'secrets' table
    # Add them to db
    query = "INSERT INTO pm.secrets(masterkey_hash, device_secret) values(%s, %s)"
    val = (hashed_mp, ds)
    cursor.execute(query, val)
    db.commit()

    printc("[green][+][/green] Added to the database")
    printc("[green]Configuration Done[/green] ")
    db.close()

config() #--> calling the config function 