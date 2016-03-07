import sqlite3


def create_sample():
    """ Create a sample table with sample ID, Name, Chemical, Notes
        ID is auto-incremented
        Name can't be null or empty
        Chemical can't be null or empty
        Notes can be null or empty
    """
    conn = sqlite3.connect('sample.db')
    conn.execute('''CREATE TABLE sample
           (ID INTEGER PRIMARY KEY ,
           Name           CHAR(50)    NOT NULL,
           Chemical       CHAR(50)     NOT NULL,
           Notes          CHAR(100));''')
    conn.close()
