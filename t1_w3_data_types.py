#!/home/paco/ubuntu/py3/bin/python
print(f'################### Calculadora ##################')
var_ingreso = float(input(f"Ingreso Mensual : "))
var_compras = int(input(f"Cumpras del mes : "))
var_lista_compras = []

n = 1
while n <= var_compras:
    var_item = input(f"Concepto : ")
    var_costo = float(input(f"Costo : "))
    var_lista_compras.append({"item":var_item,"costo":var_costo})
    n += 1

print(f'******************** Reporte *********************')
var_resto = var_ingreso
for compra in var_lista_compras:
    var_resto = var_resto - compra["costo"]
    var_pre = len(compra["item"])
    var_post = len(str(round(compra["costo"],2)))
    var_puntos = 50 - var_pre - var_post
    print(f'{compra["item"]}{"." * var_puntos }{round(compra["costo"],2)}')

var_puntos = 45 - len(str(round(var_resto,2)))
print(f'\n--------------------------------------------------\
\nResta{" " * var_puntos}{round(var_resto,2)}')
