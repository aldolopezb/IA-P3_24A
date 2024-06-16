#Aldo López Barrios
#21310106
#Ordenamiento por inserción

def insertion_sort(arr):
   
    # Recorre la lista desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        # Guarda el elemento actual en una variable
        key = arr[i]
        
        # Inicializa j con el índice del elemento anterior
        j = i - 1
        
        # Mueve los elementos de arr[0..i-1], que son mayores que key, una posición hacia adelante
        while j >= 0 and key > arr[j]:                      #---------
            arr[j + 1] = arr[j]
            j -= 1
        
        # Coloca el elemento key en su posición correcta
        arr[j + 1] = key

    return arr

# Ejemplo de uso
if __name__ == "__main__":
    # Definir una lista desordenada
    unsorted_list = [45, 3, 76, 0.02, 34, 5, 905]
    
    # Llamar a la función de Insertion Sort
    sorted_list = insertion_sort(unsorted_list)
    
    # Imprimir la lista ordenada
    print("Lista ordenada:", sorted_list)


'''El Algoritmo construye la lista ordenada de uno en uno, 
tomando cada elemento y colocándolo en la posición correcta 
respecto a los elementos ya ordenado'''
