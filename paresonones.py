#!/home/paco/ubuntu/py3/bin/python

print(f"¿Qué número estás pensando? \n>>>>" ,end=" ")
var_input = int(input())
if (var_input % 2) == 0:
    print(f'----> {var_input} Es número par')
else:
    print(f'----> {var_input} Es número non')