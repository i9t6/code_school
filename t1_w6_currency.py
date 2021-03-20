#!/home/paco/ubuntu/py3/bin/python

import requests 
import json


print(f'Seleccionar código de moneda (tres letras):\
\n  MXN - Mexican Peso\
\n  ARS - Argentinan Peso\
\n  PEN - Sol Peruano\n')

var_moneda = input(">>> ")
json_data = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
json_rate = 1 / json_data['rates'][var_moneda]
print(f'Tipo de cambio : 1 {var_moneda} es {round(json_rate,4)} USD')

var_otro = "Yes"
var_indice = 1
var_lista_gastos = []
print("lista de compras \n\n")
while var_otro == "Yes":
    var_concepto = input(f'Concepto {var_indice} : ')
    var_gasto = round(float(input(f'Cantidad {var_indice} ({var_moneda}) : ')),2)
    var_lista_gastos.append({"item":var_concepto,"monto":var_gasto})
    var_indice += 1
    var_otro = input(f'Agregar otro? (Yes/No) :')

#print(var_lista_gastos)
print(f'Reporte de gastos\n*****************')

print(f'Concepto\t\tCantidad ({var_moneda})\t\tCantidad (USD)\n===================================')
var_total =  0
for gasto in var_lista_gastos:
    print(f'{gasto["item"]}\t\t\t{gasto["monto"]}\t\t\t{round(json_rate * gasto["monto"],4)}')
    var_total += gasto['monto']

print(f'-------------------------------------------\
\nTotal : {var_total} {var_moneda} ..... {round(json_rate * var_total,4)} USD')