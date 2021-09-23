def max_sequence(arr):
    i = 0
    b_sum = 0
    while i < len(arr):
        a_sum = 0
        p_sum = 0
        for x in arr[i:]:
            a_sum += x
            if a_sum > p_sum:
                p_sum = a_sum
        i += 1
        if p_sum >  b_sum:
            b_sum = p_sum
    return b_sum