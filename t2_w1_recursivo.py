#!/home/paco/ubuntu/py3/bin/python
"""
import sys
sys.setrecursionlimit(3000)
from functools import lru_cache
@lru_cache()
"""

def factorial(n):
    #caso base
    if n == 1:
        return 1
    #caso recursivo
    else:
        return n*factorial(n-1)

def fibonacci(n):
    print(f"Calculando Fibonacci for: {str(n)}")
    if n == 0:
        x = 0
    elif n == 1:
        x = 1
    else:
        x = fibonacci(n-1) + fibonacci (n-2)
    return x


network = {
    'RA' : ['R_Nextengo','R_SantaFe'],
    'R_Nextengo' : ['SW_Tlalnepantla', 'SW_Toluca'],
    'R_SantaFe' : ['SW_Cuajimalpa'],
    'SW_Tlalnepantla' : ['Terminal_Naucalpan'],
    'SW_Toluca' : ['Terminal_Metepec'],
    'SW_Cuajimalpa' : ['Terminal_DesiertoLeones'],
    'Terminal_Naucalpan' : [],
    'Terminal_Metepec' : [],
    'Terminal_DesiertoLeones' : []
}

def arbol(var_nodo):
    if network[var_nodo] == []:
        return "END"
    else:
        for i in network[var_nodo]:
            print(f"{var_nodo} >> {i}")
        for i in network[var_nodo]:
            arbol(i)

lista = [1,2,3,4,5,6,7,8,9,10,11,12]
def crea_arbol(arbol,lista_nodos,*nodo):
    if lista_nodos == []:
        final = {}
        [final.update( {i:t} ) for i in arbol if not ( t := arbol[i]) == ["",""]]
        return final
    if arbol == {}:
        nodo = lista_nodos.pop(0)
        arbol[nodo] = ["",""]
        return crea_arbol(arbol,lista_nodos,nodo)
    if arbol[nodo[0]][0] == "":
        arbol[lista_nodos[0]] = ["",""]
        arbol[nodo[0]][0] = lista_nodos.pop(0)
        return crea_arbol(arbol,lista_nodos,nodo[0])
    if arbol[nodo[0]][1] == "":
        arbol[lista_nodos[0]] = ["",""]
        arbol[nodo[0]][1] = lista_nodos.pop(0)    
        """for i in arbol:
            if arbol[i][0] == "" and arbol[i][1] == "":
                return crea_arbol(arbol,lista_nodos,i)"""
        x = (crea_arbol(arbol,lista_nodos,i) for i in arbol if (arbol[i][0] == "") and (arbol[i][1] == "") )
        return next(x)

lista = [1,2,3,4,5,6,7,8,9,10,11,12]
crea_arbol({},lista)
{1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [8, 9], 5: [10, 11], 6: [12, '']}
{1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [8, 9], 5: [10, 11], 6: [12, '']}
{1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [8, 9], 5: [10, 11], 6: [12, '']}
    

[l.update({i:a[i]}) for i in a if not a[i] == ["",""]]