import threading#Este módulo nos permite trabajar con hilos


semaforo_1 = threading.Semaphore(0) #Creamos los dos semáforos necesarios
semaforo_2 = threading.Semaphore(0)

def hilo_H1(): #Creamos la función para el primer hilo
    print("1") #Imprimimos cada uno de los números en el orden indicado
    semaforo_1.release()  # Señal para permitir que H2 imprima "5"
    semaforo_2.acquire()  # Espera hasta que H2 imprima "6"
    print("3")
    print("2")


def hilo_H2(): #Creamos la función para el segundo hilo
    semaforo_1.acquire()  # Espera hasta que H1 imprima "1"
    print("5")
    print("4") #Imprimimos cada uno de los números en el orden indicado
    print("6")
    semaforo_2.release()  # Señal para permitir que H1 imprima "3"

H1 = threading.Thread(target=hilo_H1) #Creamos nuestros dos hilos
H2 = threading.Thread(target=hilo_H2)


H1.start() #Inicamos los dos hilos
H2.start()

H1.join() #Esperamos a que los dos hilos terminen
H2.join()
