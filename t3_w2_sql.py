#!/home/paco/py3/bin/python
from time import time

def read_line(var_archivo):
    with open(var_archivo,"r") as file:
        for line in file:
            yield line
        
def get_even(var_linea):
    lista = [ i for i in var_linea if i in ["2","4","6","8"]]
    yield lista
    
csvfile = input(f"Nombre del archivo : ")
start = time()

total = 0
line_gen = read_line(csvfile)
for line in line_gen:
    for i in next(get_even(line)):
        total += int(i)

end = time()
print(f"Funciones  total : {total}  en {start-end}'s")

#Segunda funcion
"""start = time()

total = 0
with open(csvfile,"r") as file:
    for line in file:
        for i in line:
            if i in ["2","4","6","8"]:
                total += int(i)

end = time()
print(f"BAU        total : {total}  en {start-end}'s")"""


#Tercer funcion
start = time()

lista = []
with open(csvfile,"r") as file:
    for line in file:
        l = [ i for i in line if i in ["2","4","6","8"]]
        lista += l
                    
total = 0
for i in lista:
    total += int(i)

end = time()
print(f"BAU Lista  total : {total}  en {start-end}'s")



# Cuarto funcion
"""start = time()

total = 0
with open(csvfile,"r") as file:
    for line in (line for line in file):
        for i in ( i for i in line if i in ["2","4","6","8"]):
            total += int(i)

end = time()
print(f"Gen & for  total : {total}  en {start-end}'s")"""


# Quinta funcion
start = time()

total = 0

with open(csvfile,"r") as file:
    algo_1 = (line for line in file)
    for line in algo_1:
        algo_2 = (i for i in line if i in ["2","4","6","8"])
        for i in algo_2:
            total += int(i)

end = time()
print(f"Gen en for total : {total}  en {start-end}'s")
