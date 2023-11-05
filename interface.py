def heapsort(arr):
    build_max_heap(arr)

    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        max_heapify(arr, index=0, size=i) 

def build_max_heap(arr):
    for i in range(len(arr) // 2, -1, -1):
        max_heapify(arr, index=i, size=len(arr))

def max_heapify(arr, index, size):
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    largest = index

    if left_child < size and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < size and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        max_heapify(arr, largest, size)

# Exemplo de uso:
arr = [4, 10, 3, 5, 1]
heapsort(arr)
print(arr)
