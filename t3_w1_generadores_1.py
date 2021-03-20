#!/home/paco/py3/bin/python
from time import time

def read_line(var_archivo):
    with open(var_archivo,"r") as file:
        for line in file:
            yield line 
        
def get_even(var_linea):
    lista_gen = [ a for i in var_linea if ( a := int(i)) % 2 == 0 ]
    yield lista_gen

csvfile = input(f"Nombre del archivo : ")
#csvfile = "Numbers.csv"
start = time()

total = 0
line_gen = read_line(csvfile)
for i in next(get_even(line_gen)):
    total += i

end = time()
print(f"Total-1 : {total}  en {start-end}'s")

#Segunda Opcion
start = time()

total = 0
with open(csvfile,"r") as file:
    generador_1 = ( line for line in file )
    """
    generador_2 = ( [ a for i in generador_1 if ( a := int(i)) % 2 == 0] for number in generador_1 )
    def generador_2_desgranado(gen1):
    lista=[]
    for number in gen1:
        for i in gen1:
            if int(i) % 2 == 0:
                lista.append(int(i))
    yield lista
    """
    generador_2 = ( [ a for i in generador_1 if ( a := int(i)) % 2 == 0] for uno in "1" )
    for i in next(generador_2):
        total += i

end = time()
print(f"Total-2 : {total}  en {start-end}'s")



#Tercera Opcion
start = time()

total = 0

with open(csvfile,"r") as file:
    generador_1 = ( line for line in file )
    generador_2 = ( a for i in generador_1 if ( a := int(i)) % 2 == 0 )
    for i in generador_2:
        total += i

end = time()
print(f"Total-3 : {total}  en {start-end}'s")
