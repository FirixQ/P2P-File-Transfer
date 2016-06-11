#p2p file sender
#listen on 12334
#talk on 12344
import socket
from threading import Thread

def sender():
    #client socket - for talking

    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket for talking

    hostt = input('Receiver IP: ')
    portt = 12344
    
    try:
        remoteIP = socket.gethostbyname(hostt) #convert url to ip

    except socket.gaierror:
        print('Could not be resolved. Try again') #deal with error
        sys.exit()

    c.connect((remoteIP, portt)) #connect

    file = input('File location: ')
     
    title = file.split('/')[-1]
    c.send(title)

def listener():
    #server socket - for listening

    HOSTl = ''
    PORTl = 12334

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket to listen to

    try:
        s.bind((HOSTl, PORTl))
    except socket.error:
        print('Bind failed.')
        
    while 1:
        s.listen(10)
        conn, addr = s.accept()
        name = conn.recv(1024)
        accept = input('Accept file ' + name + ' from ' + addr[0])

Thread(target=listener).start()

sender()
