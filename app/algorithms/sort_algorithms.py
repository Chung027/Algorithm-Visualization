def bubble_sort(arr_list):
    # Skapa animator till sort genom yield
    arr_list = arr_list.copy()
    for i in range(len(arr_list)):
        # Jämförs alla element på varv bara fram sista osorterade elementet eftersom de i sista redan ligger rätt.
        for j in range(len(arr_list)-i-1):
            if arr_list[j] > arr_list[j+1]:
                arr_list[j], arr_list[j+1] = arr_list[j+1], arr_list[j]
            yield arr_list.copy()

#list = [5,3,10,2,1]
#
#sort_list = bubble_sort(list)
#print(sort_list)