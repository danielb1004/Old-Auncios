import os
import shutil

from datetime import date
from datetime import datetime


today = date.today()
day = str(today.day)
month = str(today.month)
today = str(day + "-" + month)
contenido = os.listdir('E:/Users/multi/Desktop/anucios')
name = []
files = []
name_files = []
file_deleted = []
for i in contenido:
    control = False
    for y in i:
        if y == "%":
            control = True
    if control:
        name.append(i)
        name_files.append(i)
for i in name:
    a = i[1:5]
    files.append(a)
for i in files:
    m=i[3:]
    d=i[:2]
    mt=today[3:]
    dt=today[:2]
    if d <= dt or m <= mt:
        for y in name_files:
            if d in y:
                shutil.move('E:/Users/multi/Desktop/anucios/' + y,
                            'E:/Users/multi/Desktop/anucios/historia/' + y)
                file_deleted.append(y)
                print(y)

        print("DELETE")
# print(files)
print(today)
record_old = []        
for i in file_deleted:    
    word = ".\n- Se movio el archivo en la  fecha: {} archivo: {}.\n".format(today,i)
    try: 
        try:      
            f = open ('record.txt',"r")  
            for x in f:
                record_old.append(x)
            f.close()
            f = open ('record.txt',"w") 
            for i in record_old:
                f.write(i)
            f.write(word)
        except:
            f = open ('record.txt',"w")
            f.write(word)
        
    except:
        print("is no working")
