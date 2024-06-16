#Aldo López Barrios
#21310106
#Ordenamiento por selección

def selection_sort(arr):
   
    n = len(arr)  # Longitud de la lista
    for i in range(n):
        # Asume que el elemento actual es el mínimo
        min_index = i

        # Recorre la sublista arr[i+1:] para encontrar el menor elemento
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Si el índice del mínimo no es el índice actual, intercambiar los elementos
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Ejemplo de uso
if __name__ == "__main__":
    # Definir una lista desordenada
    unsorted_list = [123, 56, 8, 24, 12, 984, 1]
    
    # Llamar a la función de Selection Sort
    sorted_list = selection_sort(unsorted_list)
    
    # Imprimir la lista ordenada
    print("Lista ordenada:", sorted_list)


'''El Algoritmo divide la lista en dos partes, una parte ordenada 
y otra no ordenada, y selecciona el elemento más pequeño de la parte 
no ordenada y lo intercambia con el primer elemento no ordenado, 
y así sucesivamente'''