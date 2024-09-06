# Program to add new entries into the Password Manager
from getpass import getpass 
from utils.dbconfig import dbconfig
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import utils.aesutil 

from rich import print as printc

# First step would be to enter the password (not the master password)
# When the user wants to add a new entry, the user has to specify the site name, site url, email and username
# After specifying the site name, site url, email and username and then when the user runs the script,
# its going to dynamically run that script and ask for the password

def computeMasterKey(mp, ds):
    password = mp.encode()
    salt = ds.encode()
    key = PBKDF2(password, salt, 32, count=1000000, hmac_hash_module=SHA512)  # count = 1000000 specifies the number of rounds
    return key


def addEntry(mp, ds, sitename, siteurl, email, username):
    # get the password
    password = getpass("Password: ")

    # To encrypt this password and save it to the database we need the Master key which is derived from the Master Password and Device Secret(aka salt)
    mk = computeMasterKey(mp, ds)   # mk --> Master Key

    # Inorder to encrypt the password we are going to use AES-256
    encrypted = utils.aesutil.encode(key=mk, source=password, keyType="bytes") # returns the password in base64 encoded format


    # Adding it to the database
    db = dbconfig()
    cursor = db.cursor()

    query = "INSERT INTO pm.entries (sitename, siteurl, email, username, password) values(%s, %s, %s, %s, %s)"
    val = (sitename, siteurl, username, encrypted)
    cursor.execute(query, val)
    db.commit()

    printc("[green][+][/green] ADDED ENTRIES")


