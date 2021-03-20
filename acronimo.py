#!/home/paco/ubuntu/py3/bin/python

print(f"Entrada por favor \n>>>>" ,end=" ")
var_input = input().split()
print(" El acronimo es: ",end=" ")

for i in var_input:
    var_temp=i[0]
    print(var_temp.capitalize(),end="")

print(f"\n Hasta luego")

