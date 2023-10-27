from math import *
from sqlite3 import *

#connection = connect('testDB2.db')
#curs = connection.cursor()
def input_d(tec_id):
    global L, B, H, exentz, malpolz, bolpolz, roz1, x, y, z, Amplitude, nachfiz, chast, period, t0, ugolcam
#    curs.execute('SELECT B1 FROM Orders WHERE id = '+str(tec_id))
    B = float(input())#'curs.fetchall()[0][0]'
 #   curs.execute('SELECT L1 FROM Orders WHERE id = '+str(tec_id))
    L = float(input())#curs.fetchall()[0][0]
#    curs.execute('SELECT B1 FROM Orders WHERE id = '+str(tec_id))
    H = float(input())  # 'curs.fetchall()[0][0]'
 #   curs.execute('SELECT L1 FROM Orders WHERE id = ' + str(tec_id))
    nachfiz = float(input())#curs.fetchall()[0][0]
  #  curs.execute('SELECT L1 FROM Orders WHERE id = ' + str(tec_id))
    t0 = float(input())  # curs.fetchall()[0][0]
    #  curs.execute('SELECT L1 FROM Orders WHERE id = ' + str(tec_id))
    ugolcam = float(input())  # curs.fetchall()[0][0]
    bolpolz = 6378.160 + H
    ugspid = float(input())/(bolpolz)#curs.fetchall()[0][0]
    malpolz = 6356.777 + H
    exentz = 0.0167
    Amplitude = 10001.965
    roz1 = malpolz / ( 1 - exentz ** 2 * sin(B) ** 2 )
    x = roz1*cos(B)*cos(L)
    y = roz1*cos(B)*sin(L)
    z = (bolpolz**2/malpolz**2)*roz1*sin(B)
    chast = ugspid/(2*pi)
    period = 1 / chast
    t0 %= 40075.017
    y_s = Amplitude*sin(chast*t0+nachfiz)
    obl = tan(ugolcam) * H * 2
    if t0<20037.5085:
        B=(t0-20037.5085)/111.31949166666666
    else:
        t0-=20037.5085
        B = t0 / 111.31949166666666
    L = y_s / 111.13294444444445
    
input_d(1)