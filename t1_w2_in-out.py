#!/home/paco/ubuntu/py3/bin/python

var_numero_1 = float(input(f"Entrada por favor \n>>>>"))
var_numero_2 = float(input(f"otro por favor \n>>>>"))
var_suma = round((var_numero_1 + var_numero_2),4)
print(f"{var_numero_1} + {var_numero_2} = {var_suma}\
\n Hasta luego")

var_palabra_1 = input(f"palabra por favor \n>>>>")
var_palabra_2 = input(f"otra palabra por favor \n>>>>")
print(f'{var_palabra_1} es igual a {var_palabra_2} ? {var_palabra_1 == var_palabra_2} \
\n va el loop')

n = 0
while n < 8:
    print(f'{"*" * n}')
    n += 1

print("\n Bye")