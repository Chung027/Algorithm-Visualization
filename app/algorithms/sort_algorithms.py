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


#list = [5,3,10,2,1]
#
#sort_list = selection_sort(list)
#print(sort_list)