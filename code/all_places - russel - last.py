# function
def find_array_will_be_remove(minimum_array_extract):
    identities = []
    old_identities = []
    for first_minimum_array in minimum_array_extract:
        new_identity = first_minimum_array[1]
        if new_identity in old_identities:
            # identities.remove(new_identity)
            if new_identity in identities:
                identities.remove(new_identity)
        else:
            identities.append(new_identity)
            old_identities.append(new_identity)
    return identities

def delete_row(receive_new_fuzzy_val, receive_array_remove_with_index):
    minus = 0
    for remove_row in receive_array_remove_with_index:
        row = remove_row[1] - minus
        receive_new_fuzzy_val.pop(row)
        minus = minus + 1
    return receive_new_fuzzy_val

def get_col(receive_new_fuzzy_val, receive_array_remove_with_index):
    index = receive_array_remove_with_index[0][1]
    row = receive_new_fuzzy_val[index]
    len_row = len(row)
    if((len_row == 1) and ( row[0] == 0)):
        col_min_value = 0
    else:
        col_min_value = min([i for i in row if i != 0])
    col_min_index = row.index(col_min_value)
    col_min_index = [col_min_index]
    return col_min_index

def find_array_will_be_remove_smallest_value(receive_smallest_result):
    smallest_array_will_remove_with_keys = []
    i = 0
    for array_will_remove in receive_smallest_result:
        data = [[[array_will_remove], i]]
        smallest_array_will_remove_with_keys.append(data)
        i = i + 1
    smallest_array_will_remove_with_keys.sort()
    smallest_array_will_remove_with_key = smallest_array_will_remove_with_keys[0]
    return smallest_array_will_remove_with_key

def find_minimum_array(receive_fuzzy_val_transpose):
    minimum_array = []
    for first_min_array in receive_fuzzy_val_transpose:
        minimum_value = min([i for i in first_min_array if i != 0])
        key_minimum = first_min_array.index(minimum_value)
        data = [minimum_value, key_minimum]
        minimum_array.append(data)
    return minimum_array

def find_array_remove_with_index(receive_minimum_array):
    array_remove_with_index = []
    index_key = 0
    for index_array_remove in receive_minimum_array:
        for value_array_remove in array_remove:
            if (value_array_remove == index_array_remove[1]):
                data = [index_array_remove, index_key]
                array_remove_with_index.append(data)
        index_key = index_key + 1
    return array_remove_with_index

def delete_col(receive_fuzzy_val_transpose_col, receive_array_remove_col):
    min = 0
    if(len(receive_fuzzy_val_transpose_col) > 0):
        for remove_col in receive_array_remove_col:
            rcol = remove_col
            col = rcol - min
            receive_fuzzy_val_transpose_col.pop(col)
            min = min + 1
    else:
        receive_fuzzy_val_transpose_col = receive_fuzzy_val_transpose_col
    return receive_fuzzy_val_transpose_col

def delete_column_small_value(receive_fuzzy_val_transpose_col, receive_array_remove_col):
    if(len(receive_fuzzy_val_transpose_col) > 0):
        row = receive_array_remove_col[0]
        array = receive_fuzzy_val_transpose_col.pop(row)
        return receive_fuzzy_val_transpose_col

def find_smallest_value(receive_new_fuzzy_val):
    smallest_results = []
    for first_array_smallest in receive_new_fuzzy_val:
        first_array_smallest.sort()
        if(first_array_smallest[0] == 0):
            if(len(fuzzy_val[0]) > 2):
                smallest_result = first_array_smallest[2] - first_array_smallest[1]
            elif(len(fuzzy_val[0]) > 1):
                smallest_result = first_array_smallest[1]
            else:
                smallest_result = first_array_smallest[0]
        else:
            if(len(fuzzy_val[0]) > 1):
                smallest_result = first_array_smallest[1] - first_array_smallest[0]
            else:
                smallest_result = first_array_smallest[0]
        smallest_results.append(smallest_result)
    return smallest_results

def find_index_row(receive_row, receive_sort):
    key = []
    i = 0
    for keys in receive_row:  
        if(len(receive_sort) > 1):
            if receive_sort[1] == keys:
                key.append(i)
            i = i + 1
        else:
             key.append(i)
    return key

def push_total(receive_fuzzy_val, receive_array_small_to_remove):
    row = receive_array_small_to_remove[0][1]
    receive_fuzzy_val[row].sort()
    ss = receive_fuzzy_val[row]
    len_row = len(ss)
    if((len_row == 1) and ( ss[0] == 0)):
        value = 0
    else:
        value = min([i for i in ss if i != 0])
    total.append(value)

def sort_array(receive_tsp_route):
    final_tsp_route = []
    first_array = ''
    second_array = ''
    n = len(receive_tsp_route)
    for i in range(n):
        j = 0
        for first_arr in receive_tsp_route:
            if(first_arr[0] == 0):
                first_array = first_arr[0]
                second_array = first_arr[1]
                valuess = [first_array, second_array]
                final_tsp_route.append(valuess)
                receive_tsp_route.pop(j)
                first_array = second_array
                break
            else:
                if(first_arr[0] == first_array):
                    first_array = first_arr[0]
                    second_array = first_arr[1]
                    valuess = [first_array, second_array]
                    valuess = [first_array, second_array]
                    final_tsp_route.append(valuess)
                    receive_tsp_route.pop(j)
                    first_array = second_array
                    break
            j = j + 1
    return final_tsp_route

def get_two_after_comma(bil):
    fuzzification_to_string = str(bil)
    fuzzification_split = fuzzification_to_string.split(".")
    fuzz_s_1 = fuzzification_split[0]
    fuzz_s_2 = fuzzification_split[1]
    fuzz_s_2_cut = fuzz_s_2[:2]
    fuzz_bil = (fuzz_s_1, fuzz_s_2_cut)
    new_bils = ".".join(fuzz_bil)
    new_bil = float(new_bils)
    return new_bil

# main program
# 1. Matriks biaya tsp
total = []

## first
# data = [
#     [[0, 0], [6, 13], [16, 23], [23, 30], [10, 17], [14, 21]],
#     [[4, 11], [0,0], [8, 15], [12, 19], [1, 8], [22, 29]],
#     [[11, 18], [5, 12], [0,0], [18, 25], [7, 14], [10,17]],
#     [[7, 14], [3, 10], [27, 34], [0,0], [9, 16], [13, 20]],
#     [[15, 22], [13, 20], [17, 24], [4, 11], [0,0], [20, 27]],
#     [[3, 10], [2, 9], [9, 16], [7, 14], [6, 13], [0,0]]
# ]

## 4 Places
# data = [
#     [[0, 0], [3, 17], [8, 15], [5, 12]],
#     [[14, 21], [0,0], [19, 33], [20, 27]],
#     [[18, 25], [15, 29], [0,0], [26, 40]],
#     [[23, 30], [27, 34], [25, 39], [0,0]]
# ]

## 5 Places
# data = [
#     [[0, 0], [4, 18], [6, 20], [5, 12], [10, 17]],
#     [[3, 10], [0,0], [14, 21], [8, 22], [17, 24]],
#     [[11, 18], [10, 24], [0,0], [14, 28], [25, 32]],
#     [[16, 30], [15, 22], [20, 34], [0,0], [26, 40]],
#     [[22, 29], [10, 17], [23, 30], [25, 39], [0,0]]
# ]

# # 6 Places
# data = [
#     [[0, 0], [4, 11], [20, 27], [10, 24], [6, 20], [9, 23]],
#     [[13, 27], [0,0], [7, 21], [14, 21], [11, 25], [13, 20]],
#     [[9, 16], [8, 22], [0,0], [16, 30], [17, 24], [22, 29]],
#     [[18, 32], [20, 34], [12, 26], [0,0], [11, 18], [16, 23]],
#     [[23, 30], [14, 28], [15, 22], [13, 27], [0,0], [17, 31]],
#     [[5, 19], [10, 17], [21, 35], [18, 25], [15, 29], [0,0]]
# ]

# # 7 Places
data = [
    [[0, 0], [12, 15], [7, 12], [10, 12], [12, 13], [12, 17], [15, 20]],
    [[12, 16], [0, 0], [14, 15], [15, 16], [15, 17], [16, 17], [19, 20]],
    [[7, 13], [14, 16], [0, 0], [9, 10], [9, 11], [10, 11], [13, 14]],
    [[11, 12], [15, 17], [9, 11], [0, 0], [1, 2], [2, 3], [4, 5]],
    [[12, 14], [15, 18], [9, 12], [2, 3], [0, 0], [1, 2], [6, 8]],
    [[12, 16], [16, 18], [10, 12], [1, 3], [2, 3], [0, 0], [7, 8]],
    [[15, 19], [19, 21], [13, 15], [4, 6], [6, 9], [7, 9], [0, 0]],
]

data_transpose = [list(i) for i in zip(*data)]
len_arr = len(data_transpose)

tsp_route = []

# 2. Konversi dalam bilangan fuzzy
fuzzy_value = []
relevant_value = []
for first_array in data_transpose:
    second_array_pushed = []
    fuzzy_value_pushed = []
    for second_array in first_array:
        first_value = second_array[0] # 12
        second_value = second_array[1] # 16
        expand_value = []
        fuzzifications = (second_value - first_value) / 7 # 16 - 12 / 7 = 0.57
        fuzzification = get_two_after_comma(fuzzifications)
        if(fuzzification == 0):
            for i in range(first_value, second_value+1):
                expand_value.append(i)
        else:
            initial = 0
            value = 0
            while value < second_value:
                if (initial == 0):
                    expand_value.append(first_value) # insert first value # 12
                    new_value_range = first_value + fuzzification # 12.571428571428571
                    value = new_value_range
                else:
                    value = value + fuzzification
                if(value < second_value):
                    value_cut = "%.2f" % value
                    value_pushed = float(value_cut)
                    expand_value.append(value_pushed)
                initial = initial + 1
        data = [second_array, expand_value]
        fuzzy_value_pushed.append(data)
        second_array_pushed.append(second_array)
    fuzzy_value.append(fuzzy_value_pushed)
    relevant_value.append(second_array_pushed)

# 3. fuzzy Ranking
fuzzys_value = []
for fuzzy_first_array in fuzzy_value:
    fuzzys = []
    for fuzzy_second_array in fuzzy_first_array:
        second_array = fuzzy_second_array[1]
        total_sum_array = sum(second_array)
        fuzzy_to_split = round(1/8 * total_sum_array, 2)
        fuzzy = fuzzy_to_split
        fuzzys.append(fuzzy)
    fuzzys_value.append(fuzzys)
fuzzy_val_transpose = [list(i) for i in zip(*fuzzys_value)]

datas = []
row_index = 0
for position in fuzzy_val_transpose:
    row_col = 0
    datas_each_row = []
    for each_posisition in position:
        data_reindex = row_index, row_col
        row_col = row_col + 1
        datas_each_row.append(data_reindex)
    datas_row = datas_each_row
    datas.append(datas_row)
    row_index = row_index + 1


# 4. Alternate method
## a. Find minimum value for each row
minimum_array = find_minimum_array(fuzzy_val_transpose)

## b. Delete row & col
### Delete row
array_remove = find_array_will_be_remove(minimum_array)
array_remove_with_index = find_array_remove_with_index(minimum_array)

for push in array_remove_with_index:
    value = push[0][0]
    total.append(value)

for tsp_route_loop in array_remove_with_index:
    tsp_route_data = tsp_route_loop[1], tsp_route_loop[0][1]
    tsp_route.append(tsp_route_data)

delete_row(fuzzy_val_transpose, array_remove_with_index) # delete rows
delete_row(datas, array_remove_with_index)

### Delete col
fuzzy_val_transpose_col = [list(i) for i in zip(*fuzzy_val_transpose)]
datas_transpose_col = [list(i) for i in zip(*datas)]

array_remove_col = find_array_will_be_remove(minimum_array)
array_remove_col.sort()

fuzzy_val_transpose_col = delete_col(fuzzy_val_transpose_col, array_remove_col) #delete col
delete_col(datas_transpose_col, array_remove_col) #delete col

fuzzy_val = [list(i) for i in zip(*fuzzy_val_transpose_col)]
datas = [list(i) for i in zip(*datas_transpose_col)]

len_fuzzy_val = len(fuzzy_val)

count = 0
while (count < len_fuzzy_val):
    ## c. Selection the small values
    index_row_has_value = [list(i) for i in zip(*fuzzy_val_transpose_col)]
    index_row_has_value_sort = [list(i) for i in zip(*fuzzy_val_transpose_col)]

    smallest_results = find_smallest_value(fuzzy_val)
    array_small_to_remove = find_array_will_be_remove_smallest_value(smallest_results) 

    ## d. Delete row & col
    ### Delete row
    fuzzy_val = [list(i) for i in zip(*fuzzy_val_transpose_col)]
    datas_value = [list(i) for i in zip(*datas_transpose_col)]    
    route_row = array_small_to_remove[0][1]

    del_col = get_col(fuzzy_val, array_small_to_remove)
    key_row = array_small_to_remove[0][1]
    key_col = del_col[0]
    row_col_return = datas_value[key_row][key_col]
    tsp_route.append(row_col_return)

    push_total(fuzzy_val, array_small_to_remove)
    delete_row(fuzzy_val, array_small_to_remove) # delete rows
    delete_row(datas_value, array_small_to_remove) # delete rows

    ### Delete col
    fuzzy_val_transpose_col = [list(i) for i in zip(*fuzzy_val)]
    datas_transpose_col = [list(i) for i in zip(*datas_value)]
    
    array_small_to_remove = find_array_will_be_remove_smallest_value(smallest_results)

    array_adjust = array_small_to_remove[0][1]
    row = index_row_has_value[array_adjust]
    # sorted
    fuzzy_val_transpose_col_sort = [list(i) for i in zip(*fuzzy_val)]
    array_small_to_remove_sort = find_array_will_be_remove_smallest_value(smallest_results)
    array_adjust_sort = array_small_to_remove_sort[0][1]
    sort = index_row_has_value_sort[array_adjust_sort]
    sort.sort()
    index_row = find_index_row(row, sort)
    
    route_col = index_row[0]
    tsp_route_row_col = [route_row, route_col]

    delete_column_small_value(fuzzy_val_transpose_col, del_col) #delete 
    delete_column_small_value(datas_transpose_col, del_col) #delete col
    fuzzy_val = [list(i) for i in zip(*fuzzy_val_transpose_col)]
    datas_value = [list(i) for i in zip(*datas_transpose_col)]
    count = count + 1
    
print("Rute [Row, Column]: ", tsp_route)
print("Value: ", total)
print("")

sorted_array_tsp = sort_array(tsp_route)
print("Rute Sorted [Row, Column]: ", sorted_array_tsp)
print("Total waktu minimal metode alternate adalah: ", round(sum(total), 2)," Menit")