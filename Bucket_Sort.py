#Aldo López Barrios
#21310106
#Ordenamiento por cubetas
def insertion_sort(arr):
    
    # Recorre la lista desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        # Guarda el elemento actual en una variable
        key = arr[i]
        
        # Inicializa j con el índice del elemento anterior
        j = i - 1
        
        # Mueve los elementos de arr[0..i-1], que son mayores que key, una posición hacia adelante
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Coloca el elemento key en su posición correcta
        arr[j + 1] = key

    return arr

def bucket_sort(arr):
    """
    Implementa el algoritmo de Bucket Sort para ordenar una lista de elementos.

    Parámetros:
    arr (list): La lista de elementos a ordenar.

    Retorna:
    list: La lista ordenada.
    """
    # Encuentra el número máximo y mínimo en la lista
    max_val = max(arr)
    min_val = min(arr)
    num_buckets = 10  # Número de buckets

    # Calcula el tamaño de cada bucket
    bucket_range = (max_val - min_val + 1) / num_buckets

    # Inicializa los buckets como listas vacías
    buckets = [[] for _ in range(num_buckets)]

    # Distribuye los elementos en los buckets
    for num in arr:
        index = min(num_buckets - 1, int((num - min_val) / bucket_range))
        buckets[index].append(num)

    # Ordena cada bucket usando Insertion Sort
    for i in range(num_buckets):
        insertion_sort(buckets[i])

    # Concatena los buckets ordenados
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

# Ejemplo de uso
if __name__ == "__main__":
    # Definir una lista desordenada
    unsorted_list = [64, 34, 25, 12, 22, 11, 90, 5, 78, 98, 55]
    
    # Llamar a la función de Bucket Sort
    sorted_list = bucket_sort(unsorted_list)
    
    # Imprimir la lista ordenada
    print("Lista ordenada:", sorted_list)


'''Divide los elementos en un número finito de "cubetas" y 
luego ordena cada cubeta individualmente, ya sea utilizando 
un algoritmo diferente o aplicando el ordenamiento recursivo'''