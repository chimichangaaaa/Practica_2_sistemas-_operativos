import threading

semaforo_A_F = threading.Semaphore(0)  # Controla la relación entre A y F
semaforo_E_H = threading.Semaphore(0)  # Controla la relación entre E y H
semaforo_C_G = threading.Semaphore(0)  # Controla la relación entre C y G
#Tras crear nuestros tres semaforos vamos a crear una función para cada uno de ellos
def hilo_H1(): #Función para nuestro primer hilo 
    while True:
        print("A")
        semaforo_A_F.release()  # Permite imprimir un F
        print("B")
        print("C")
        semaforo_C_G.release()  # Permite imprimir un G
        print("D")

def hilo_H2(): #Función para nuestro segundo hilo 
    while True:
        semaforo_A_F.acquire()  # Espera a que se imprima un A antes de imprimir F
        print("E")
        semaforo_E_H.release()  # Permite imprimir un H
        print("F")
        semaforo_C_G.acquire()  # Espera a que se imprima un C antes de imprimir G
        print("G")       
        
def hilo_H3(): #Función para nuestro tercer hilo 
    while True:
        semaforo_E_H.acquire()  # Espera a que se imprima un E antes de imprimir H
        print("H")
        print("I")

 
H1 = threading.Thread(target=hilo_H1) #Creamos un hilo para cada uno de nuestros semaforos
H2 = threading.Thread(target=hilo_H2)
H3 = threading.Thread(target=hilo_H3)


H1.start() #Inciamos los hilos
H2.start()
H3.start()       