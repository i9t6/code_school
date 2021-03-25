#!/home/paco/py3/bin/python

from netmiko import ConnectHandler as cn
from datetime import datetime as dt

devices = [
    {'device_type' : 'cisco_ios',
    'host' : 'sandbox-iosxe-latest-1.cisco.com',
    'username' : 'developer',
    'password' : 'C1sco12345'},

    {'device_type' : 'cisco_xr',
    'host' : 'sbx-iosxr-mgmt.cisco.com',
    'port' : 8181,
    'username' : 'admin',
    'password' : 'C1sco12345'},

    {'device_type' : 'cisco_nxos',
    'host' : 'sbx-nxos-mgmt.cisco.com',
    'port':8181,
    'username' : 'admin',
    'password' : 'Admin_1234!'}]

shows = ['clock','int description','ip interface brief','ip route','inventory','run']
date = dt.now().date().strftime('%Y-%d-%m')

for d in devices:
    hostname = d['host']
    try: 
        net_connect = cn(**d)
    except:
        print(f'FAILED CONNECTION ----> {hostname}')
    else:
        f = open(f'{hostname}_{date}.txt','w')
        f.write(f'\nDevice: {hostname}')
        for c in shows:
            output = net_connect.send_command("show "+c)
            f.write(f'\n\n=========================== show {c}: ===========================\n\n')
            f.write(output)
        f.close()
        print(f'SUCCESS ----------> {hostname}')
