from scipy import *
from math import *
from sqlite3 import *

def input_d(tec_id):
    global L1, L2, B1, B2, exentz, malpolz, bolpolz, roz1, x1, y1, z1, roz2, x2, y2, z2
    curs.execute('SELECT B1 FROM Orders WHERE id = '+str(tec_id))
    B1 = int(curs.fetchall()[0][0])
    curs.execute('SELECT B2 FROM Orders WHERE id = '+str(tec_id))
    B2 = int(curs.fetchall()[0][0])
    curs.execute('SELECT L1 FROM Orders WHERE id = '+str(tec_id))
    L1 = int(curs.fetchall()[0][0])
    curs.execute('SELECT L2 FROM Orders WHERE id = '+str(tec_id))
    L2 = int(curs.fetchall()[0][0])

if __name__ == '__main__' :
    input_d(1)
 #   M = E - e * sin(e)
    print(x1,y1,z1,x2,y2,z2)