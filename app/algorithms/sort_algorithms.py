def bubble_sort(arr_list):
    # Skapa animator till sort genom yield
    arr_list = arr_list.copy()
    for i in range(len(arr_list)):
        # Jämförs alla element på varv bara fram sista osorterade elementet eftersom de i sista redan ligger rätt.
        for j in range(len(arr_list)-i-1):
            if arr_list[j] > arr_list[j+1]:
                arr_list[j], arr_list[j+1] = arr_list[j+1], arr_list[j]
            yield arr_list.copy()

def selection_sort(arr_list):
    arr_list = arr_list.copy()
    for i in range(len(arr_list)):
        # Vi kallas första index är minsta index och jämförs med alla index i list
        min_index = i
        # när vi jämför första index med rest index i lista och byta till rätt plats 
        # om första index är större än minsta index på höger list, det ska byta engång bara
        # efter det går vidare till nästa index och jämför med rest index
        for j in range(i+1, len(arr_list)):
            if arr_list[min_index] > arr_list[j]:
                min_index = j
            yield arr_list.copy()
        arr_list[i], arr_list[min_index] = arr_list[min_index], arr_list[i]
        yield arr_list.copy()

def insertion_sort(arr_list):
    """
    Insertion sort fungerar genom att dela listan i 2 delar: en sorterad (vänster)
    och en osorterad (höger).
    För varje steg tas första elementet från den osorterade delen och
    jämförs bakåt i den sorterad delen. Om elementet till vänster större,
    flyttas det ett steg åt höger tills rätt plats hittas.
    Sedan sätts element in på rätta position på sorterade delen.
    """
    arr_list = arr_list.copy()
    for i in range(1, len(arr_list)): # Start list with second element
        sorted_list = arr_list[i] # Parts to 2 list
        j = i - 1 # start comparing backwards
        while j >= 0 and arr_list[j] > sorted_list:
            arr_list[j+1] = arr_list[j] # Slide element to the right
            j -= 1    # proceed backwards
            yield arr_list.copy()
        arr_list[j+1] = sorted_list
        yield arr_list.copy()

def merge(left_list, right_list):
    """
    Detta hjälp funktion för merge sort. Syfte är att sortera 2 list och slå ihop tillbaka sent returnera sorterad array list
    """
    merged = [] # Create new list to store merged list 
    i , j = 0, 0 # i is left size, j is right size
    while i < len(left_list) and j < len(right_list): # Compare to array is element left do it
        if left_list[i] < right_list[j]:  # Compare if index left size smaller right size 
            merged.append(left_list[i]) # add this index to left size
            i += 1
        else:
            merged.append(right_list[j]) # Do same with right size if index right is bigger
            j += 1
    while i < len(left_list): # if element left is stilling on list add this to list
        merged.append(left_list[i])
        i += 1
    while j < len(right_list):
        merged.append(right_list[j])
        j += 1

    return merged

def merge_sort(arr_list):
    """
    Merge sort fungerar genom att dela array list för 2 list tills element av list finns 0 eller 1 kvar.
    Det ska sortera varje små array list och slå ihop tillbaka till sorterad array list.
    """
    if len(arr_list) <= 1:
        return arr_list
    mid = len(arr_list) // 2 # Parts to 2 list
    left_list = arr_list[:mid]  # left array
    right_list = arr_list[mid:] # right array

    # Recursively sort both halves
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    # Merge the sorted halves
    return merge(left_list, right_list)

def merge_sort_visual(arr_list):
    """
    Merge Sort generator for visualization — always yields the full array.
    Each step highlights which elements are being merged.
    """
    arr = arr_list.copy()

    def merge_sort_recursive(arr, start, end, full_array):
        if end - start <= 1:
            yield full_array.copy()
            return

        mid = (start + end) // 2

        # sort left side
        for step in merge_sort_recursive(arr, start, mid, full_array):
            yield step

        # sort right side
        for step in merge_sort_recursive(arr, mid, end, full_array):
            yield step

        # merge two sorted halves into full_array
        left = arr[start:mid]
        right = arr[mid:end]
        i = j = 0
        k = start

        # step through both halves and merge back into arr
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            yield arr.copy()  # yield full array after each merge step

        # copy any remaining elements of left half
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            yield arr.copy()

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            yield arr.copy()

    # starta sorteringen
    yield from merge_sort_recursive(arr, 0, len(arr), arr)

def quick_sort(arr_list):
    """
    Quick sort funkar genom att välja ett pivot element i array list och partitionera listan så att
    alla element mindre än pivot placeras till vänster och alla element större än pivot placeras till höger.
    Sedan sorteras de två delarna rekursivt på samma sätt tills hela listan är sorterad.
    """
    arr_list = arr_list.copy()

    def partition(arr_list, start, end):  # start is first index, end is last index
        # Choose pivot element and place it at right postition in array, it's lomuto partition method(Swich element to right place )
        pivot = arr_list[end]  # definera pivot with last index
        steps = []
        # Initialize the index of the smaller element. We start i one position before 'start' because we will increment it
        # only when we find an element smaller than or equal to the pivot.
        i = start - 1
        # Traverse the array from 'start' to 'end - 1'
        for j in range (start, end):  # j is to compare with pivot element
            if arr_list[j] <= pivot:
                i += 1
                arr_list[i], arr_list[j] = arr_list[j], arr_list[i]
                steps.append(arr_list.copy())
        # Place the pivot element att the correct position        
        arr_list[i+1], arr_list[end] = arr_list[end], arr_list[i+1]
        steps.append(arr_list.copy())
        return i + 1, steps  # Return the index of the pivot element and steps for visualization
    
    def quick_sort_recursive(arr_list, start, end):
        # Continue sorting while the sub-array has more than one element
        if start < end:
            # Partition the array and get the pivot index and steps for visualization
            pi, steps = partition(arr_list, start, end)
            for step in steps:
                yield step
            # Recursively sort elements before and after partition
            yield from quick_sort_recursive(arr_list, start, pi - 1)
            yield from quick_sort_recursive(arr_list, pi + 1, end)
    # Initial call to the recursive quicksort function
    yield from quick_sort_recursive(arr_list, 0, len(arr_list) - 1)
    yield arr_list.copy()

#list = [5,3,10,2,1,6]
#sort_list = merge_sort(list)
#print(sort_list)