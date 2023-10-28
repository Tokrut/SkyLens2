from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host = 'localhost',
        user = 'root',
        password = 'Jkbvg!18',
        database = 'testmydb',
    ) as connection:
        with connection.cursor() as curs:
#            curs.execute('''
#            CREATE TABLE Sput (
#                id INT PRIMARY KEY,
#                B TEXT,
#                L TEXT,
#                H TEXT,
#                fi0 TEXT,
#                t0 TEXT,
#                Omega TEXT,
#                alf_cam TEXT
#            )
#            ''')
#            curs.execute('''
#            CREATE TABLE Users (
#                id INT AUTO_INCREMENT PRIMARY KEY,
#                login VARCHAR(75),
#                psw VARCHAR(255),
#                email VARCHAR(100),
#                date_podp DATE
#            )
#            ''')
#            curs.execute('''
#            CREATE TABLE Orders (
#                id INT AUTO_INCREMENT PRIMARY KEY,
#                id_user INT,
#                B1 TEXT,
#                L1 TEXT,
#                B2 TEXT,
#                L2 TEXT,
#                FOREIGN KEY (id_user) REFERENCES Users(id)
#            )
#            ''')
            curs.execute('''
            CREATE TABLE Compl_Orders (
                id INT AUTO_INCREMENT PRIMARY KEY,
                id_order INT,
                B1 TEXT,
                L1 TEXT,
                B2 TEXT,
                L2 TEXT,
                Photo BLOB,
                FOREIGN KEY (id_order) REFERENCES Orders(id)
            )
            ''')
            connection.commit()
except Error as e:
    print(e)

