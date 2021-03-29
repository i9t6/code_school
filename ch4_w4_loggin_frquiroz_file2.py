from netmiko import ConnectHandler as cn
from datetime import datetime as dt
import logging


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


console_formartter = logging.Formatter('%(asctime)s-::-%(levelname)s-::-%(message)s')
logfile_formartter = logging.Formatter('%(levelname)s~%(asctime)s~message:%(message)s~module:%(module)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(console_formartter)

logfile_handler = logging.FileHandler(f"my_logs_{date}.log",mode ="w")
logfile_handler.setLevel(logging.DEBUG)
logfile_handler.setFormatter(logfile_formartter)

my_logger = logging.getLogger()
my_logger.addHandler(console_handler)
my_logger.addHandler(logfile_handler)
my_logger.setLevel(logging.DEBUG)

for d in devices:
    hostname = d['host']
    try: 
        my_logger.warning(f"Initiate connection: {hostname}")
        net_connect = cn(**d)
    except:
        my_logger.warning(f"Failed Connection -------> {hostname}")
    else:
        my_logger.warning(f"Success")
        f = open(f'{hostname}_{date}.txt','w')
        my_logger.warning(f"Create a file {hostname}_{date}.txt")
        my_logger.warning(f"Inititate sending commands")
        f.write(f'\nDevice: {hostname}')
        for c in shows:
            output = net_connect.send_command("show "+c)
            f.write(f'\n\n=========================== show {c}: ===========================\n\n')
            #f.write(f' show {c} '.center(20, '='))
            f.write(output)
            my_logger.warning(f"Show {c} --> OK")
        f.close()
    my_logger.warning(f"Close connection:{hostname}")
