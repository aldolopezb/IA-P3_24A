#Aldo López Barrios
#21310106
#Ordenamiento por mezcla

def merge_sort(arr):
    
    if len(arr) > 1:
        # Encuentra el punto medio de la lista
        mid = len(arr) // 2

        # Divide la lista en dos mitades
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Llama recursivamente a merge_sort en cada mitad
        merge_sort(left_half)
        merge_sort(right_half)

        # Inicializa los índices para recorrer las dos mitades
        i = 0  # Índice para left_half
        j = 0  # Índice para right_half
        k = 0  # Índice para la lista arr

        # Junta las dos mitades de nuevo, comparando elemento por elemento
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:                #---------------------------------
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Comprueba si quedan elementos en left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Comprueba si quedan elementos en right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Ejemplo de uso
if __name__ == "__main__":
    # Definir una lista desordenada
    unsorted_list = [6, 2678, 1, 98, 24, 567]
    
    # Llamar a la función de Merge Sort
    sorted_list = merge_sort(unsorted_list)
    
    # Imprimir la lista ordenada
    print("Lista ordenada:", sorted_list)


'''Es un algoritmo de ordenamiento recursivo que divide 
la lista en dos mitades, las ordena recursivamente y 
luego las fusiona para producir una lista ordenada'''
