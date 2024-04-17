import socket
import mysql.connector
import json

ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
port = 80
ser.bind(('0.0.0.0', port))

ser.listen(1)

print('Escuchando en',port)

def obtenerPersonaPorTelefono(phone):
    conexion1=mysql.connector.connect(host="db_sist_dist", user="root", passwd="sist_dist_poligran",database="sist_dist_poligran")
    cursor1=conexion1.cursor()

    sqlString = "SELECT dir_nombre,dir_direccion,c.ciud_nombre FROM personas p INNER JOIN ciudades c ON p.dir_ciud_id=c.ciud_id WHERE p.dir_tel='"+str(phone)+"' LIMIT 1"
    cursor1.execute( sqlString )

    persona = cursor1.fetchall()
    
    conexion1.close()
    if len(persona) == 0:
        return {
            'error' : 'Persona dueña de ese número telefónico no existe.'
        }
        
    
    return {
        'nombre' : persona[0][0],
        'direccion' : persona[0][1],
        'ciudad' : persona[0][2],
    }
 
cli, addr = ser.accept()

while True:
    phoneRaw = cli.recv(1024)
    phone = phoneRaw.decode()
    
    if len(phone) == 0:
        continue

    print("Recibo conexion de la IP: " + str(addr[0]) + " Puerto: " + str(addr[1]) + " Teléfono recibido: " + phone)
    
    searchResult = obtenerPersonaPorTelefono( phone )
    
    cli.send(json.dumps( searchResult ).encode())
