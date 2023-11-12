# AED 2 DOGO
# Johnatas Philipe Rodrigues da Silva
# Pedro Henrique Souza dos Santos

# Functions related to Dogo project

# ------- MAX HEAPIFY -------
def max_heapify(arr, n, i):
    largest = i # define the largest as root
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Checks if the left child exists and is larger than the root
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Checks if the right child exists and is larger than root or left child
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # If the largest is not the root, change them
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify flame on the affected subtree
        max_heapify(arr, n, largest)

# ------- MIN HEAPIFY -------
def min_heapify(arr, n, i):
    smallest = i  # Define the smallest as the root
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Checks if the left child exists and is minor than the root
    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child

    # Checks if the right child exists and is the minor than the root
    if right_child < n and arr[right_child] < arr[smallest]:
        smallest = right_child

    # If the smallest is not the root, change them
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  
        # Recursively heapify flame on the affected subtree
        min_heapify(arr, n, smallest)


# ------- Insert Element -------
# The insert_element insert a element into a heap maitaining the heap properties
def insert_element (heap, element):
    heap.append(element) # adds an element at the end of heap
    heap_up(heap, len(heap) - 1)

def heap_up(heap, index):
    while index > 0:
        parent_index = (index - 1) // 2
        if heap[index] >= heap[parent_index]:
            break
        heap[index], heap[parent_index] = heap[parent_index], heap[index]
        index = parent_index

# ------- Remove minor priority (lower cost)-------
def pop_min(heap):
    if len(heap) == 0:
        return None
    if len(heap) == 1:
        return heap.pop()
    
    # Removes the minor priority element (on the top of the heap)
    min_element = heap[0]

    # Replaces the removed element with the last elemento of the heap
    heap[0] = heap.pop()

    # Reorganize the heap to maintain heap properties
    min_heapify(heap, len(heap), 0)

    return min_element





