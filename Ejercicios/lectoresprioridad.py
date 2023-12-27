
import threading #lo vamos a necesitar en toda la practica ya que es una libreria que implementa las funcionalidades de los hilos.
import time #lo necesitamos para el tiempo bloqueado de los semaforos

# Necesitamos definir dos funciones una para el lector y una para el escritor


# Definimos una función para el lector
def lector(nombre, semlectores, semescritores): 
    while True:
        with semlectores: #llamamos al semaforo de lectura
            print(f'Lector {nombre} leyendo.')# print que te dice el lector que esta leyendo
            time.sleep(2) #el semáforo permanece bloqueado para otros lectores 2 segundos.

# Definimos una función para el escritor
def escritor(nombre, semlectores, semescritores):
    while True:
        with semescritores: #llamamos al semaforo de escritura
            print(f'Escritor {nombre} escribiendo.') # print que te dice el escritor
            time.sleep(2) #tiempo bloqueado

#Ya definidas las dos funciones con sus semaforos
if __name__ == "__main__": #verificamos si el script se está ejecutando como un programa principal y no siendo importado
    semlectores = threading.Lock() #creamos los bloqueos para los semaforos
    semescritores = threading.Lock()

    lectores = 3 #ponemos 3 lectores y 2 escritores por ejemplo
    escritores =  2

    # Creamos los hilos para lectores y escritores
    hlectores = [threading.Thread(target=lector, args=(i, semlectores, semescritores)) for i in range(lectores)]
    hescritores = [threading.Thread(target=escritor, args=(i, semlectores, semescritores)) for i in range(escritores)]

    # Iniciamos los hilos
    for hilo in hlectores + hescritores:
        hilo.start()

    # Esperamos a que todos los hilos terminen
    for hilo in hlectores + hescritores:
        hilo.join()
