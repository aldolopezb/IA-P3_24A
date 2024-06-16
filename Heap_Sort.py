#Aldo López Barrios
#21310106
#Ordenamiento por monticulos

def heapify(arr, n, i):
    # Función para convertir un subarreglo en un montículo (heap)
    largest = i  # Inicializamos el mayor como raíz
    l = 2 * i + 1  # izquierda = 2*i + 1
    r = 2 * i + 2  # derecha = 2*i + 2

    # Ver si el hijo izquierdo de la raíz existe y es mayor que la raíz
    if l < n and arr[i] < arr[l]:                           #------------
        largest = l

    # Ver si el hijo derecho de la raíz existe y es mayor que la raíz
    if r < n and arr[largest] < arr[r]:                     #------------
        largest = r

    # Cambiar la raíz si es necesario
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Aplicar heapify a la raíz
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Construir un maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos uno por uno
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)

# Código para probar el algoritmo
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Arreglo ordenado es")
for i in range(n):
    print("%d" %arr[i]),


'''Construye un montículo a partir de la lista y luego extrae 
repetidamente el elemento máximo (o mínimo) y lo coloca en su posición final'''