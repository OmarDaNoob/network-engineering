from netmiko import ConnectHandler

R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.56.130',
    'username': 'cisco',
    'password': 'cisco123!',
}

R2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.56.101',
    'username': 'cisco',
    'password': 'cisco123!',
}

with open('base_conf') as f:
    lines = f.read().splitlines()

all_devices = [R1,R2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)