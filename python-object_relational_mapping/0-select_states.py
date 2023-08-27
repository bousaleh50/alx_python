"""
 this script lists all states from the database 
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    access to the database and get the statesfrom the db

    """

    db_connect = MySQLdb.connect(host = "localhost",user = argv[1],port = 3306,passwd = argv[2],db = argv[3])
    db_cursor = db_connect.cursor()
    
    db_cursor.execute("SELECT * FROM states")
    
    states = db_cursor.fetchall()
    
    for s in states:
        print(s)
        
    