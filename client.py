host = 'python_sist_dist'
port = 80

import socket
import json
 
obj = socket.socket()

obj.settimeout(10)
obj.connect((host, port))
print("Conectado al servidor")
 
control = 1
phoneSuccess = None

while control <= 3:
    mens = phoneSuccess
    
    if phoneSuccess is None:
        mens = input("Teléfono a buscar ")
        
    obj.send(mens.encode('utf-8'))
    
    recibido = obj.recv(1024)
    dataDict = json.loads(recibido)
    
    if dataDict.get('error'):
        print(dataDict['error'])
        continue
        
    print(dataDict)
    phoneSuccess=mens
    control += 1