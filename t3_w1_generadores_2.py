#!/home/paco/py3/bin/python
from time import time

csvfile = input(f"Nombre del archivo : ")
start = time()

lista = []
with open(csvfile,"r") as file:
    lista += [ a for line in file if (a := int(line)) % 2 == 0 ]           

total = 0
for i in lista:
    total += i

end = time()
print(f"Total-1 : {total}  en {start-end}'s")


