import os
import shutil

from datetime import date
from datetime import datetime


today = date.today()
day = str(today.day)
month = str(today.month)
today = str(day + "-" + month)
contenido = os.listdir('C:/Users/danyb/Documents/PROYECTOS/PERSONAL/anuncios')
name = []
files = []
name_files = []
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
    if i <= today:
        for y in name_files:
            if i in y:
                shutil.move('C:/Users/danyb/Documents/PROYECTOS/PERSONAL/anuncios/' + y,
                            'C:/Users/danyb/Documents/PROYECTOS/PERSONAL/anuncios/historia/' + y)
                print(y)
        print("DELETE")

print(files)
print(today)