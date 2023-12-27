import threading 
import time #lo necesitamos para el tiempo bloqueado de los semaforos

# Definimos una función para el lector
def lector(nombre, semlectores, semescritores):
    while True:
        with semlectores:  # Adquiere el semáforo de lectura
            print(f'Lector {nombre} leyendo.')
            time.sleep(1)

# Definimos una función para el escritor(en este caso tienen prioridad)
def escritor(nombre, semlectores, semescritores):
    while True:
        with semescritores:  #llamamos al semaforo de escritura
            with semlectores:  # llamamos también el semáforo de lectura
                print(f'Escritor {nombre} escribiendo.')
                time.sleep(1)
#Ya definidas las dos funciones con sus semaforos
if __name__ == "__main__":
    semlectores = threading.Lock()
    semescritores = threading.Lock() #ponemos los bloqueos

    lectores = 1 #definimos el numero de escritores y lectores
    escritores = 2

    # Creamos los hilos para lectores y escritores
    hlectores = [threading.Thread(target=lector, args=(i, semlectores, semescritores)) for i in range(lectores)]
    hescritores = [threading.Thread(target=escritor, args=(i, semlectores, semescritores)) for i in range(escritores)]

    # Iniciamos los hilos
    for hilo in hlectores + hescritores:
        hilo.start()

    # Esperamos a que todos los hilos terminen
    for hilo in hlectores + hescritores:
        hilo.join()
