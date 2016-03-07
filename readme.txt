Starting the app at localhost:port/ or localhost:port/sample-list
- example : http://127.0.0.1:8000/ or http://127.0.0.1:8000/sample-list

Validation:
- Sample name: mandatory
- Sample chemical: mandatory
- Sample notes: no validation

Database:
- SQLite 3
- Sample Table Structure:
    ID             INTEGER PRIMARY KEY ,
    Name           CHAR(50)     NOT NULL,
    Chemical       CHAR(50)     NOT NULL,
    Notes          CHAR(100)

