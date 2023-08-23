import subprocess

def ping(host):
    try:
        # Ejecutar el comando ping en la línea de comandos
        result = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True, check=True)
        
        # Capturar la salida del comando y mostrarla
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar el ping:", e)

if __name__ == "__main__":
    host_to_ping = "google.com"  # Cambia esto al host que quieras pinguear
    ping(host_to_ping)





def ping_1(host):
    try:
        # Ejecutar el comando ping en la línea de comandos
        result = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True, check=True)
        
        # Capturar la salida del comando y mostrarla
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar el ping:", e)

if __name__ == "__main__":
    host_to_ping = "amazon.com"  # Cambia esto al host que quieras pinguear
    ping_1(host_to_ping)
