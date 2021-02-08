# Takes list of temperature values and returns temperature closest to zero,
# for equal numbers with different sign, positive - has higher priority

def min_temp(temp):
    abs_values = [abs(x) for x in temp]
    min_temp = min(abs_values)
    # if min_temp in temp:
    #     return min_temp
    # else:
    #     return -min_temp
    return min_temp if min_temp in temp else -min_temp


temp = [-1.1, 2, -3, 6, -5, 1.3, 1.1, -0.7, 0.7]

print(min_temp(temp))