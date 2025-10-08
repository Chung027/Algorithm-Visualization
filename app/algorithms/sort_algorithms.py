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

#list = [5,3,10,2,1]
#
#sort_list = insertion_sort(list)
#print(sort_list)