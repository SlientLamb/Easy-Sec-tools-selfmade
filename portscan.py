import socket
sock = socket.socket()

hosts = ['220.181.38.148']
ports = [22, 445, 80, 443, 3389]

for host in hosts:
    for port in ports:
        try:
            print ( "[+]  Connect to  " +host+":"+str(port) )
            sock.connect((host, port))
            sock.send('Primal Security \n')    
            banner = sock.recv(4096)
            if banner:
                print (" Port "+str(port)+ "open: "+banner)
            sock.close()
        except: pass