import pexpect
ip_address = "192.168.56.101"
username = "cisco"
password = "cisco123!"
# Create the SSH session
session = pexpect.spawn('ssh ' + username + '@' + ip_address,encoding='utf-8', timeout=20)
session.expect('Password:')

session.sendline(password)
session.expect('#')

#change host name
session.sendline('conf t')
session.expect('\(config\)')

session.sendline('hostname R1')
session.expect('R1')

#exit config
session.sendline('exit')
session.expect('#')

#copy running conf and startup conf
session.sendline('terminal length 0')
session.expect('#')

session.sendline('show run')
#no idea why 2 expects are needed, but without it it doesnt work  :p
session.expect('#')
session.expect('#')
running_config=session.before.splitlines()

session.sendline('show start')
session.expect('#')
start_config=session.before.splitlines()
#exit enable mode
session.sendline('exit')
#get a sucess message if works
print('---------------------------------------')
print('')
print('--- Success! connecting to: ', ip_address)
print('---               username: ', username)
print('---               password: ', password)
print('')
print('_______________________________________')
# Terminates SSH
session.close()

with open(ip_address + '_startup_config','w') as file:
    for line in start_config:
        file.write(line+'\n')
print('')
with open(ip_address + '_running_config','w') as file:
    for line in running_config:
        file.write(line+'\n')
exit()