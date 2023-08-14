from cryptography.fernet import Fernet
import os

# Generar una clave secreta
clave_secreta = Fernet.generate_key()

# Crear un objeto Fernet con la clave secreta
fernet = Fernet(clave_secreta)

# Encriptar y borrar el archivo original
def encriptar_y_borrar(nombre_archivo, clave):
    with open(nombre_archivo, 'rb') as archivo:
        contenido = archivo.read()
        contenido_encriptado = fernet.encrypt(contenido)

    nombre_archivo_enc = nombre_archivo + '.enc'
    with open(nombre_archivo_enc, 'wb') as archivo_encriptado:
        archivo_encriptado.write(contenido_encriptado)

    os.remove(nombre_archivo)
    print('Archivo encriptado y original borrado.')

# Desencriptar el archivo utilizando la clave
def desencriptar_archivo(nombre_archivo_enc, clave):
    with open(nombre_archivo_enc, 'rb') as archivo_encriptado:
        contenido_encriptado = archivo_encriptado.read()
        contenido_desencriptado = fernet.decrypt(contenido_encriptado)

    nombre_archivo_original = nombre_archivo_enc[:-4]  # Eliminar '.enc' del nombre
    with open(nombre_archivo_original, 'wb') as archivo_original:
        archivo_original.write(contenido_desencriptado)
    
    print('Archivo desencriptado.')

# Ejemplo de uso
nombre_archivo = 'archivo.txt'
encriptar_y_borrar(nombre_archivo, clave_secreta)

nombre_archivo_enc = 'archivo.txt.enc'
desencriptar_archivo(nombre_archivo_enc, clave_secreta)




archivo_a_borrar = "archivo.txt" # Reemplaza esto con la ruta de tu archivo

try:
    os.remove(archivo_a_borrar)
    print(f"El archivo '{archivo_a_borrar}' ha sido borrado exitosamente.")
except FileNotFoundError:
    print(f"El archivo '{archivo_a_borrar}' no fue encontrado.")
except Exception as e:
    print(f"No se pudo borrar el archivo '{archivo_a_borrar}': {e}")



def borrar_directorio(ruta):
    try:
        # Borra el directorio y su contenido de manera recursiva
        os.rmdir(ruta)
        print(f"Directorio {ruta} borrado exitosamente.")
    except OSError as e:
        print(f"Error al borrar el directorio {ruta}: {e}")

# Ruta del directorio que quieres borrar
ruta_del_directorio = "hack"

borrar_directorio(ruta_del_directorio)
