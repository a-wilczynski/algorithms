# Quicksort Algorithm

def quicksort(arr: list, start: int, end: int) -> int: 
    """Execute paritioning and recursivly executes itself on partioned sublists"""
    if start < end:
        pivot_index = partition(arr, start, end)    
        quicksort(arr, start, pivot_index - 1)
        quicksort(arr,pivot_index + 1, end)

def partition(arr, start, end):
    """Finds place for a pivot and returns it"""
    pivot = arr[end]
    i = start - 1

    for j in range(start,end):
        if arr[j] < pivot:
            i += 1
            swap(arr, j, i)
    i += 1
    swap(arr, i, end) 

    return i

def swap(arr,x,y):
    """swaping x with y index values in array"""
    arr[x], arr[y] = arr[y], arr[x]
