#Aldo López Barrios
#21310106
#Ordenamiento Rápido

def quick_sort(arr):
    # Realizar el ordenamiento Quick Sort
    if len(arr) <= 1:
        return arr
    else:
        # Seleccionamos el pivote, que en este caso es el último elemento del arreglo
        pivot = arr[len(arr) // 2]
        # Dividimos el arreglo en tres partes: menores, iguales y mayores que el pivote
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        # Ordenamos recursivamente las partes de menores y mayores
        return quick_sort(less) + equal + quick_sort(greater)

# Ejemplo de uso:
arr = [3, 6, 8, 10, 1, 2, 12]
print("Arreglo original:", arr)
print("Arreglo ordenado:", quick_sort(arr))


'''Es un Algoritmo recursivo que selecciona un "pivote" y 
reordena la lista de modo que todos los elementos menores 
que el pivote queden antes y los mayores después, y luego aplica 
recursivamente el mismo proceso a las sublistas'''