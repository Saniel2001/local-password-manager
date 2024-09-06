# Logic required to connect to database
import mysql.connector 

from rich import print as printc
from rich.console import Console
console = Console()

def dbconfig():
    try:
        db = mysql.connector.connect(
            host = "127.0.0.1",
            user = "pm",   # pm -> password manager
            passwd = "your_password",
        )
    except Exception as e:  # Handling the exception if connection to database fails
        console.print_exception(show_locals=True)  # Prints the error message with the traceback and shows it in a more formatted way
    
    return db