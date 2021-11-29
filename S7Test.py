#!/usr/bin/python3
# 时  间：2021-11-29 10:16
import snap7
from snap7.util import *
from snap7.types import *
import datetime
start = datetime.datetime.now()
plc = snap7.client.Client()
plc.connect("192.168.0.3",0,0)
data = plc.db_read(7, 0, 2020)
data3 = plc.db_read(12, 0, 10000)
#print(data3)
print(data)
#data=plc.read_area(snap7.types.Areas.DB, 2, 40, 4)
for i in range(0,10000,2):
    #data1=get_real(data,i)
    data1 = get_word(data3, i)
    print(data1)
end = datetime.datetime.now()
print('Running time: %s Seconds' % (end - start))
plc.disconnect()