#Aldo López Barrios
#21310106
#Ordenamiento de Shell

def shell_sort_desc(arr):
    
    n = len(arr)
    gap = n // 2  # Inicializa el tamaño del gap

    # Reduce el gap hasta que sea 0
    while gap > 0:
        # Recorre la lista desde gap hasta el final
        for i in range(gap, n):
            # Guarda el elemento actual en una variable
            temp = arr[i]
            
            # Inicializa j con el índice del elemento anterior en el gap
            j = i
            
            # Mueve los elementos de arr[j-gap] que son menores que temp una posición hacia adelante
            while j >= gap and arr[j - gap] < temp:  # Cambia la condición a <
                arr[j] = arr[j - gap]
                j -= gap
            
            # Coloca el elemento temp en su posición correcta
            arr[j] = temp
        
        gap //= 2  # Reduce el tamaño del gap

    return arr

# Ejemplo de uso
if __name__ == "__main__":
    # Definir una lista desordenada
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    
    # Llamar a la función de Shell Sort en orden descendente
    sorted_list = shell_sort_desc(unsorted_list)
    
    # Imprimir la lista ordenada
    print("Lista ordenada de mayor a menor:", sorted_list)


'''Es una generalización del ordenamiento por inserción que permite 
intercambios de elementos no adyacentes. Utiliza una secuencia de 
intervalos decrecientes para ordenar los elementos'''
