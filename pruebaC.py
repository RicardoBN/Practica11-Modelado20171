import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:1')
print(s.ping())  
print(s.yo_juego())
print(s.cambia_direccion(0,4))
print(s.estado_del_juego())  

