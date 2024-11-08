 #Helper function to maintain the max-heap property
def max_heapify(A, n, i):
    largest = i      # Initializing largest as root
    left = 2 * i + 1  
    right = 2 * i + 2 

    #If the left child is larger than root
    if left < n and A[left] > A[largest]:
        largest = left

    #If the right child is larger than the largest so far
    if right < n and A[right] > A[largest]:
        largest = right

    #If the largest is not root, swap and then continue
    if largest != i:
        A[i], A[largest] = A[largest], A[i] 
        max_heapify(A, n, largest)

#Function to build a max-heap
def build_max_heap(A, n):
    # Start from the last node and then going upwards
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(A, n, i)

#Main heapsort function
def heapsort(A):
    n = len(A)

    #Building a max heap
    build_max_heap(A, n)

    #One by one extracting the maximum element from the heap.
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        A[i], A[0] = A[0], A[i]
        # Call max_heapify on the reduced heap
        max_heapify(A, i, 0)

#example
A = [13, 17, 15, 4, 6, 7]
print("Original array:", A)
heapsort(A)
print("Sorted array:", A)
