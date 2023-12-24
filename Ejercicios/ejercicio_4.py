import threading


def imprimir(letra, siguiente):
    
    print(letra, end="")
    siguiente.release()


orden_impresion = [("A", threading.Semaphore(1)),
                   ("C", threading.Semaphore(1)), 
                   ("E", threading.Semaphore(1)), 
                   ("R", threading.Semaphore(1)), 
                   ("O", threading.Semaphore(1))]

hilos = [threading.Thread(target=imprimir, args=(letra, siguiente)) for letra, siguiente in orden_impresion]


for hilo in hilos:
    hilo.start()


for hilo in hilos:
    hilo.join()
