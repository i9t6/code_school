#!/home/paco/ubuntu/py3/bin/python
from t1_w7_passwords_module import *

n = 0
while n <=1:
    var_orden = "primer" if n == 0 else "segundo"
    var_username = input(f'\n{var_orden} username:')

    var_match = var_valido = False

    while not (var_valido and var_match):
        var_password = input('escriba el nuevo password:')
        if not (var_valido := valida_password(var_password)):
            print('Incorrecto, tienen . o -')
        else:
            var_password_2 = input('escriba el nuevo password nuevamente:')
            if not (var_match := compara_passwords(var_password, var_password_2)):
                print('No son iguales, intenta de nuevo')
    n += 1


