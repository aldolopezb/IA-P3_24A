#Aldo López Barrios 
#21310106
#Ordenamiento por conteo
def counting_sort(arr):
    
    # Encuentra el rango de valores en la lista
    max_val = max(arr)
    min_val = min(arr)
    range_vals = max_val - min_val + 1

    # Inicializa la lista de conteo con ceros
    count = [0] * range_vals

    # Contar la frecuencia de cada elemento en la lista
    for num in arr:
        count[num - min_val] += 1

    # Reconstruye la lista ordenada
    sorted_arr = []
    for i in range(range_vals):
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr

# Ejemplo de uso
if __name__ == "__main__":
    # Definir una lista desordenada
    unsorted_list = [4, 2, 5, 8, 11, 13, 16]
    
    # Llamar a la función de Counting Sort
    sorted_list = counting_sort(unsorted_list)
    
    # Imprimir la lista ordenada
    print("Lista ordenada:", sorted_list)


'''Algoritmo no comparativo que cuenta el número 
de ocurrencias de cada valor distinto en la lista 
y usa esta información para colocar cada valor en 
su posición correcta en la lista ordenada'''
