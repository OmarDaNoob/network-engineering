import pexpect
ip_address = "192.168.56.101"
username = "cisco"
password = "cisco123!"
# Create the SSH session
session = pexpect.spawn('ssh ' + username + '@' + ip_address,encoding='utf-8', timeout=20)
result = session.expect(['[password:', pexpect.TIMEOUT, pexpect.EOF])
# Check for error, if exists then display error and exit
if result !=0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()
session.sendline(password)
result=session.expect('#',pexpect.TIMEOUT,pexpect.EOF)
# Check for error, if exists then display error and exit
if result !=0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()
#change host name
session.sendline('conf t')
result=session.expect('\(config\)',pexpect.TIMEOUT,pexpect.EOF)
# Check for error, if exists then display error and exit
if result !=0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()

session.sendline('hostname R1')
result=session.expect('R1',pexpect.TIMEOUT,pexpect.EOF)
# Check for error, if exists then display error and exit
if result !=0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()
#exit config
session.sendline('exit')
result=session.expect('#',pexpect.TIMEOUT,pexpect.EOF)
# Check for error, if exists then display error and exit
if result !=0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()
#copy running conf and startup conf
session.sendline('terminal length 0')
result=session.expect('#',pexpect.TIMEOUT,pexpect.EOF)
# Check for error, if exists then display error and exit
if result !=0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()
session.sendline('show run')
running_conf=session.before.splitlines()
result=session.expect('#',pexpect.TIMEOUT,pexpect.EOF)
# Check for error, if exists then display error and exit
if result !=0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()
session.sendline('show start')
start_conf=sesion.before.splitlines()
result=session.expect('#',pexpect.TIMEOUT,pexpect.EOF)
# Check for error, if exists then display error and exit
if result !=0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()
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