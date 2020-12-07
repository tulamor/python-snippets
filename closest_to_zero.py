#   Takes list of temperature values and returns temperature closest to zero, 
# for equal absolute numbers, positive - has higher priority 

def min_temp(temp):    
    abs_values = [abs(x) for x in temp]
    min_temp = min(abs_values)
    if min_temp in temp: 
        return min_temp
    else:
        return -min_temp


temp = [-1.1, 2, -3, 6, -5, 1.3]