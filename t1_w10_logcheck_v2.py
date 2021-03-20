#!/home/paco/ubuntu/py3/bin/python
import re
import datetime

"""
m = re.search(r"(?P<employee>\w+)@cisco\.com","cisco123@cisco.com")
m.group("employee")
re.search(r"(?P<employee>\w+)@cisco\.com","cisco123@cisco.com").group("employee")
re.search(r"\w+[_\-,](\w+)_(\w+)","CD1_Song_Artist")
re.search(r"(?P<employee>\w+)@(?P<dominio>\w+)\.com","cisco123@cisco.com")
re.split(r"\s*[+\-=/*]\s*","57 + 23 *46-53+2i")
re.split(r"\s*[+\-=/*]\s*","57 + 23 *46-53+2i")
re.findall(r"NX\d+","NX920 and NX723 are NX874")
re.findall(r"(NX\d+)","NX920 and NX723 are NX874")
re.sub(r"\w+[_\-,](\w+)_(\w+)",r"\2-\1","CD1_Song_Artist")
re.sub(r"(NX\d+)",r"XXX","NX920 and NX723 are NX874")
"""

var_patron = r"(\d+/\d+/\d+ \d+:\d+:\d+) \[(\w+)\] (.*)"
datos = {"warning":datetime.datetime(2121, 12, 31, 23, 59, 59),"error":[],"alarmas":{}}
print(datos)
with open("log_sample.log","r") as file:
    for line in file:
        try:
            var_info = re.search(var_patron,line).groups()
        except:
            datos["error"].append(line)
        else:
            var_fecha = datetime.datetime.strptime(var_info[0],"%m/%d/%Y %H:%M:%S")
        
            #if var_info[1] == "WARNING":
            datos["warning"] = var_fecha if ((var_fecha < datos["warning"]) and (var_info[1] == "WARNING")) else datos["warning"]

            """if not var_info[1] in datos["alarmas"].keys():
            datos["alarmas"][var_info[1]] = 1
            else:
            datos["alarmas"][var_info[1]] += 1"""
        
            datos["alarmas"][var_info[1]] = 1 if not (var_info[1] in datos["alarmas"].keys()) else datos["alarmas"][var_info[1]] + 1
            print(datos["alarmas"])
print(f"\nPrimer warning: {datos['warning']:%m/%d/%Y %H:%M:%S}\n")
print(f"logs mal formados:")
for i in datos["error"]:
    print(f"> > {i}",end="")
print(f"\nSeveridades y cantidades:")
for i in datos["alarmas"].keys():
    print(f"> > {i} > > {datos['alarmas'][i]} ")


    
    
