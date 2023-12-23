import threading #Este módulo nos permite trabajar con hilos
import time #Este módulo nos permite crear tiempos de espera
import random #Este módulo nos permite generar números aleatorios

n = threading.Semaphore(0)  # Inicialmente no hay elementos en el buffer
s = threading.Semaphore(1)  # Semáforo para controlar el acceso al buffer

buffer = [] #Creamos un buffer que va a contener los distintos elementos

def productor(): #Creamos la función del productor 
    while True:
        item = random.randint(1, 100)  # Producimos un elemento
        s.acquire()  # Iniciamos la sesión crítica del recurso compartido 
        buffer.append(item)  # Añadimos elemento al buffer
        print(f"Productor produjo: {item}")
        s.release() #Finalizamos la sección crítica del recurso compartido
        n.release()  # Indicamos que hay un nuevo elemento en el buffer
        time.sleep(random.random())  #Generamos un tiempo de espera aleatorio

def consumidor(): #Creamos la función del consumidor
    while True:
        n.acquire()  # Esperamos si no hay elementos en el buffer
        s.acquire()  # Esperamos si otro hilo está accediendo al buffer
        item = buffer.pop(0)  # Extraeremos un elemento del buffer
        print(f"Consumidor consumió: {item}")
        s.release()#Finalizamos la sección crítica del recurso compartido
        time.sleep(random.random())  # Generamos un tiempo de espera aleatorio


def main():# Creación y ejecución de hilos para el productor y el consumidor
    productor_thread = threading.Thread(target=productor) #Creamos un hilo para la función productor
    consumidor_thread = threading.Thread(target=consumidor) #Creamos un hilo para la función consumidor

    productor_thread.start() #Empezamos la ejecución de ambos hilos
    consumidor_thread.start()

    productor_thread.join() #Esperamos a que los hilos terminen
    consumidor_thread.join()

if __name__ == "__main__":
    main()
