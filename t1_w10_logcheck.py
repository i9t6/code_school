#!/home/paco/ubuntu/py3/bin/python
import re
import datetime

var_patron = r"(\d+/\d+/\d+ \d+:\d+:\d+) \[(\w+)\] (.*)"
datos = {"warning":datetime.datetime(2121, 12, 31, 23, 59, 59),"error":[],"alarmas":{}}

with open("log_sample.log","r") as file:
    for line in file:
        try:
            var_info = re.search(var_patron,line).groups()
        except:
            datos["error"].append(line)
        else:
            var_fecha = datetime.datetime.strptime(var_info[0],"%m/%d/%Y %H:%M:%S")
            datos["warning"] = var_fecha if var_fecha < datos["warning"] and var_info[1] == "WARNING" else datos["warning"]     
            datos["alarmas"][var_info[1]] = 1 if not var_info[1] in datos["alarmas"].keys() else datos["alarmas"][var_info[1]] + 1
            
print(f"\nPrimer warning: {datos['warning']:%m/%d/%Y %H:%M:%S}\n\nlogs mal formados:")
for i in datos["error"]:
    mensaje = i if len(i) >1 else " --- vacio ---\n"
    print(f"> > {mensaje}",end="")
print(f"\nSeveridades y cantidades:")
for i in datos["alarmas"].keys():
    print(f"> > {i} > > {datos['alarmas'][i]} ")


    
    
