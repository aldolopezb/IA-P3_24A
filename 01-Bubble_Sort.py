#Aldo López Barrios
#21310106
#Ordenamiento de Burbuja
"""
Implementa el algoritmo de Bubble Sort para ordenar una lista de elementos.

Parámetros:
arr (list): La lista de elementos a ordenar.

Nos retorna:
list: La lista ordenada.
"""

def bubble_sort(arr):
    
    n = len(arr)  # Longitud de la lista
    for i in range(n):
        # La variable `already_sorted` sirve para optimizar el algoritmo.
        # Si no se realizan intercambios en una pasada, la lista ya está ordenada.
        already_sorted = True

        # Realiza un pase a través de la lista desde el inicio hasta n-i-1.
        # Después de cada pasada, el siguiente mayor elemento estará en su lugar correcto.
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambia los elementos si están en el orden incorrecto.
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False  # Hubo un intercambio, por lo que la lista aún puede no estar ordenada

        # Si no se realizaron intercambios durante una pasada, la lista está ordenada y podemos salir del bucle.
        if already_sorted:
            break

    return arr

# Ejemplo de uso
if __name__ == "__main__":
    # Definir una lista desordenada
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    
    # Llamar a la función de Bubble Sort
    sorted_list = bubble_sort(unsorted_list)
    
    # Imprimir la lista ordenada
    print("Lista ordenada:", sorted_list)


'''Algoritmo que recorre repetidamente la lista, compara elementos
adyacentes y los intercambia si están en el orden incorrecto'''
