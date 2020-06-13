def max_sub_array_sum(array):
    start_array = 0
    end_array = len(array)
    max_ending_at_i = max_sum = array[start_array]
    max_left_at_i = max_left_so_far = start_array

    max_right_so_far = start_array + 1
    for i in range(start_array + 1, end_array):
        if max_ending_at_i > 0:
            max_ending_at_i += array[i]
        else:
            max_ending_at_i = array[i]
            max_left_at_i = i
        if max_ending_at_i > max_sum:
            max_sum = max_ending_at_i
            max_left_so_far = max_left_at_i
            max_right_so_far = i + 1
    return max_left_so_far, max_right_so_far, max_sum


segment = [12, -34, 40, 6, -10, 56, 12, -1, -15, 10, 4]
start, end, total_sum = max_sub_array_sum(segment)
print('For vector {} start index is {}, end index {} and the sum {}.'.format(
    segment, start, end - 1, total_sum))
