def minmax1 (x):
    # this function fails if the list length is 0 
    minimum = maximum = x[0]
    for i in x[1:]:
        if i < minimum: 
            minimum = i 
        else: 
            if i > maximum: maximum = i
    return (minimum,maximum)

a = [142,144,44,1112,88,79,2,6,8,4,2,48,645,21,0]
try: 
    print(minmax1(a))
except IndexError:
    print("Error list is empty")