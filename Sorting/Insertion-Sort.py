def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        curr = my_list[i]  # store the first number in the unsorted part of
                           # of array into curr
        j = i
        while j > 0 and my_list[j - 1] > curr:       # this loop shifts value within sorted part of array
            my_list[j] = my_list[j - 1]              # to open a spot for curr
            j -= 1
        my_list[j] = curr
