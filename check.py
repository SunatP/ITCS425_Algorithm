T = []

T.append(1)
T.append(2)
T.append(3)
# T.append(4)
I = []

while T is not None: 
    if not T:
        break
    else : 
        next = max(T)
        I.append(next)
        T.remove(next)
        
print("I value is ", I)
print("T value is ",T)
