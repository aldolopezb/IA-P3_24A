#Aldo López Barrios
#21310106
#Ordenamiento aleatorio

import random

def random_sort_desc(arr):
 
    # Genera una permutación aleatoria de la lista
    random.shuffle(arr)
    
    # Invierte el orden de la lista
    arr.sort(reverse=True)              #-----------------
    
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    # Definir una lista desordenada
    unsorted_list = [65, 14, 456, 4, 22, 76, 90]

    # Llamar a la función de ordenamiento aleatorio de mayor a menor
    sorted_list = random_sort_desc(unsorted_list)

    # Imprimir la lista ordenada de forma aleatoria de mayor a menor
    print("Lista ordenada de forma aleatoria de mayor a menor:", sorted_list)
