from math import *
from datatime import datetime
from datatime import timedelta
from sqlite3 import *

#connection = connect('testDB2.db')
#curs = connection.cursor()
def input_d(tec_id):
    global L, B, H, exentz, malpolz, bolpolz, roz1, x, y, z, Amplitude, nachfiz, chast, period, t0, ugolcam, obl
#    curs.execute('SELECT B1 FROM Orders WHERE id = '+str(tec_id))
    B = float(input())#'curs.fetchall()[0][0]'
 #   curs.execute('SELECT L1 FROM Orders WHERE id = '+str(tec_id))
    L = float(input())#curs.fetchall()[0][0]
#    curs.execute('SELECT B1 FROM Orders WHERE id = '+str(tec_id))
    H = float(input())  # 'curs.fetchall()[0][0]'
  #  curs.execute('SELECT L1 FROM Orders WHERE id = ' + str(tec_id))
    t0 = float(input())  # curs.fetchall()[0][0]
    #  curs.execute('SELECT L1 FROM Orders WHERE id = ' + str(tec_id))
    ugolcam = float(input())  # curs.fetchall()[0][0]
    t0 = float(input())  # curs.fetchall()[0][0]
    #  curs.execute('SELECT L1 FROM Orders WHERE id = ' + str(tec_id))
    ugspid = float(input())/(bolpolz)#curs.fetchall()[0][0]
    roz1 = malpolz / ( 1 - exentz ** 2 * sin(B) ** 2 )
    x = roz1*cos(radians(B))*cos(radians(L))
    y = roz1*cos(radians(B))*sin(radians(L))
    nachfiz = asin(y/(x**2+y**2)**0.5)
    chast = ugspid/(2*pi)
    obl = tan(radians(ugolcam)) * H
def progon(B1,L1,B2,L2,time):
    for t in range(0,86400,60):
        t0 = timedelta(time,t0)%40075.017
        y_s = L+ Amplitude * sin(radians(chast * t0 + nachfiz))
        y_s %= 10001.965
        if t0 < 20037.5085:
            B = (t0 - 20037.5085) / 111.31949166666666
        else:
            t0 -= 20037.5085
            B = t0 / 111.31949166666666
        L = y_s / 111.13294444444445
        if (B+obl >= B2 and L+obl >= L2) and (B-obl <= B1 and L-obl <= L1):
            return t
            break
malpolz = 6356.777 + H
exentz = 0.0167
Amplitude = 10001.965
bolpolz = 6378.160 + H
input_d(1)
time = datetime.now()
for i in range():
    progon()