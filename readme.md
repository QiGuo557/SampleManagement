Sample Management
=================

Instruction
-----------
Starting the app at localhost:port/ or localhost:port/sample-list
example : http://127.0.0.1:8000/ or http://127.0.0.1:8000/sample-list

Validation
----------
- Sample name: mandatory, up to 50 characters
- Sample chemical: mandatory, up to 50 characters
- Sample notes: no validation, up to 100 characters

Database
--------
- SQLite 3
- Sample Table Structure:


    |----------|:-------------:|------:|
    | ID|  INTEGER | PRIMARY KEY |
    | Name|    CHAR(50)   |   NOT NULL, |
    | Chemical| CHAR(50) |    NOT NULL, |
    | Notes| CHAR(100) |     |