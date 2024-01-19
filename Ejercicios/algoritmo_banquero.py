import numpy as np #Importamos numpy para el manejo de matrices


def leer_archivo(archivo): # esta funcion lee un archivo que contiene bloques de matrices y con numpy las transforma en matrices
    with open(archivo) as file:
        raw_data = file.read().split('----------------------------\n')
    return [np.array([list(map(int, row.split())) for row in matrix.split('\n') if row]) for matrix in raw_data]

def es_estado_seguro(need, allocation, available): #esta función determina si el sistema está en un estado seguro ejecutando procesos de manera secuencial
                                                    # hasta que todos los procesos estén finalizados o se detecte un estado inseguro. Es la clave del ejercicio
    work = available.copy() #creamos una copia de vector de recursos
    finish = [False] * len(need) #vemos si el cada proceso ha terminado
    sequence = []

    while False in finish:
        for i, (n, a, f) in enumerate(zip(need, allocation, finish)): #hacemos un bucle que va examinando todos los procesos que no han terminado
            if f == False and all(n <= work):
                work += a
                finish[i] = True
                sequence.append(i)
                break
        else:
            return False, []

    return True, sequence


#Vamos a definir una funcion que nos diga si hay valores negativos,congruencias, que las matrices no tengan valores negativos o que no haya mas recursos asignados
def validar_matrices(need, allocation, resources, available): 
    # Verificamos la congruencia de las matrices
    if len(need) != len(allocation) or len(need[0]) != len(allocation[0]):
        raise ValueError("Las matrices de Necesidad y Asignación no son congruentes.")

    # Verificamos que no haya valores negativos en las matrices
    if np.any(need < 0) or np.any(allocation < 0) or np.any(resources < 0) or np.any(available < 0):
        raise ValueError("Las matrices y vectores no pueden contener valores negativos.")

    # Verificamos que no haya más recursos asignados o necesitados que los que existen en total
    if np.any(allocation > resources) or np.any(need > resources):
        raise ValueError("Hay más recursos asignados o necesitados que los disponibles en total.")

def algoritmo_banquero(archivo): #ahora aplicamos loa tres funciones ya explicadas.
    need, allocation, resources, available = leer_archivo(archivo) #leemos las matrices

    try:
        validar_matrices(need, allocation, resources, available) #ver si tiene algun problema como valores negativos
    except ValueError as e:
        print(f"Error de validación: {e}")
        return
# ahora el sistema imprime el numero de procesos recursos la matriz de asignacion de necesidad
# el vector de recursos y el vector de disponibles ademas de decirnos si el estado es seguro o no
    print("Número total de procesos:", len(need))
    print("Número total de recursos:", len(resources))
    
    print("Matriz de Necesidad:")
    print(need)
    
    print("Matriz de Asignación:")
    print(allocation)
    
    print("Vector de Recursos:")
    print(resources)
    
    print("Vector de Disponibles:")
    print(available[0])

    estado_seguro, secuencia_ejecucion = es_estado_seguro(need, allocation, available[0])

    if not estado_seguro:
        print("El estado no es seguro.")
    else:
        print("El estado es seguro.")
        print("Secuencia de ejecución segura:", secuencia_ejecucion)

# Por ultimo llamamos al algoritmo del banquero 

algoritmo_banquero('C:\\Users\\pablo\\OneDrive\\Escritorio\\sistemas operativos\\matrices.txt')
