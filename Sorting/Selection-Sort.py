def selection_sort(my_list):

    n = len(my_list)
    for i in range(n - 1):
        min_idx = i  # record the index of the smallest value,
                     # initialized with where the smallest value may be found
        for j in range(i + 1, n):              # go through list, 
            if my_list[j] < my_list[min_idx]:  # and every time we find a smaller value,
                min_idx = j                    # record its index (note how nothing has moved at this point.)


        if min_idx != i:
            my_list[min_idx], my_list[i] = my_list[i], my_list[min_idx]
