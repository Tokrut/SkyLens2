from math import *
from scipy import *
from sqlite3 import *

connection = connect('testDB2.db')
curs = connection.cursor()
def input_d(tec_id):
    global L, B, H, exentz, malpolz, bolpolz, roz1, x, y, z, A, fi, chast
    curs.execute('SELECT B1 FROM Orders WHERE id = '+str(tec_id))
    B1 = int(curs.fetchall()[0][0])
    curs.execute('SELECT L1 FROM Orders WHERE id = '+str(tec_id))
    L1 = int(curs.fetchall()[0][0])
    curs.execute('SELECT L1 FROM Orders WHERE id = ' + str(tec_id))
    A = int(curs.fetchall()[0][0])
    curs.execute('SELECT L1 FROM Orders WHERE id = ' + str(tec_id))
    fi = int(curs.fetchall()[0][0])
    curs.execute('SELECT L1 FROM Orders WHERE id = ' + str(tec_id))
    ugspid = int(curs.fetchall()[0][0])
    malpolz = 6356.777+H
    bolpolz = 6378.160+H
    exentz = 0.0167
    roz1 = malpolz/(1-exentz**2*sin(B1)**2)
    x = roz1*cos(B1)*cos(L1)
    y = roz1*cos(B1)*sin(L1)
    z = (bolpolz**2/malpolz**2)*roz1*sin(B1)
    chast = ugspid/(2*pi)
    period = 1 / chast
    A*sin(chast*t+fi)