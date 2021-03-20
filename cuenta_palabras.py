#!/home/paco/ubuntu/py3/bin/python

print(f"¿Qué estás pensando? \n>>>>" ,end=" ")
var_input = input().split()
var_cuenta = 0
for algo in var_input:
    var_cuenta +=1
print(f"----> fueron {var_cuenta} palabras")
