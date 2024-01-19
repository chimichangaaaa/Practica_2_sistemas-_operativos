import threading 
import random

# definimos dos semaforos para que bloqueen ciertas letras
semA = threading.Semaphore(0)
semC = threading.Semaphore(0)

# creamos una variable que decide si las letras "E" y "R" se imprimen en un orden específico o de manera intercalada.
alternate = random.choice([True, False])

# Hilo H1
def hilo_H1():
    semA.acquire()  #imprime la letra C después de que hilo 2 imprime la letra A.
    print("C")
    semC.release()  

# Hilo H2
def hilo_H2():
    print("A")
    semA.release()  # imprime la letra A, luego espera a que el hilo h1 imprima la letra C  Después de eso, imprime la letra "O".
    semC.acquire()  
    if alternate:
        print("E")
        print("R") #imprime E o R 
    else:
        print("R")
        print("E")
    print("O") #imprime la letra O.
        
# Ccreamos e iniciamos los hilos
thread1 = threading.Thread(target=hilo_H1)
thread2 = threading.Thread(target=hilo_H2)

thread1.start() #se inician los hilos
thread2.start()

thread1.join() #terminan los hilos
thread2.join()

