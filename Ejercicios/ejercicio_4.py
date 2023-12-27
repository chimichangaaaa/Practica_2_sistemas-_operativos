import threading #Este módulo nos permite trabajar con hilos


# Semáforos para sincronizar la ejecución de los hilos
sem_a = threading.Semaphore(0)
sem_c = threading.Semaphore(0)

def Hilo1():  # definimos el primer hilo con Las letras C y E
    sem_c.acquire()  # Espera hasta que H2 imprima "A"
    print("C")
    sem_a.release()  # Señal para permitir que H1 imprima "E"
    print("E")
    
def Hilo2():  # definimos el segundo hilo con las letras A R y O
    print("A")
    sem_c.release()  # Señal para permitir que H2 imprima "C"
    sem_a.acquire()  # Espera hasta que H2 imprima "R"
    print("R")
    print("O")



#Una vez con el orden de las letras hecho los metemos en dos variables
H1 = threading.Thread(target=Hilo2)
H2 = threading.Thread(target=Hilo1)

#Iniciamos los hilos 
H1.start()
H2.start()

# Esperar a que ambos hilos terminen
H1.join()
H2.join()
