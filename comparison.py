import pexpect
ip_address = "192.168.56.101"
username = "cisco"
password = "cisco123!"
# Create the SSH session
session = pexpect.spawn('ssh ' + username + '@' + ip_address,encoding='utf-8', timeout=20)
result = session.expect(['[password:', pexpect.TIMEOUT, pexpect.EOF])

session.sendline(password)
result=session.expect('#')

#change host name
session.sendline('conf t')
result=session.expect('\(config\)')

session.sendline('hostname R1')
result=session.expect('R1')

#exit config
session.sendline('exit')
result=session.expect('#')

#copy running conf and startup conf
session.sendline('terminal length 0')
result=session.expect('#')

session.sendline('show run')
running_conf=session.before.splitlines()
result=session.expect('#')

session.sendline('show start')
start_conf=sesion.before.splitlines()
result=session.expect('#')
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

print(start_conf)
print('')
print(running_conf)
exit()