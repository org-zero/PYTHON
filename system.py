import platform
import requests
from datetime import datetime
import time



system_info = platform.uname()
print("Sistema operativo:", system_info.system)
print("Nombre del nodo:", system_info.node)
print("Versión del sistema operativo:", system_info.release)
print("Versión del sistema:", system_info.version)
print("Arquitectura del procesador:", system_info.machine)
print("Tipo de procesador:", system_info.processor)



def get_location():
    response = requests.get('http://ipinfo.io') 
    data = response.json()
    return data

location_info = get_location()
print("Ubicación:")
print("IP:", location_info['ip'])
print("Host:", location_info['hostname'])
print("Ciudad:", location_info['city'])
print("Región:", location_info['region'])
print("País:", location_info['country'])
print("Servicio de Red:", location_info['org'])
print("Ubicación aproximada:", location_info['loc'])
time.sleep(4)




current_time = datetime.now()
print("Hora actual:",  "de todos los datos obtenidos --> ", current_time )
