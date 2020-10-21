# define let M = building Material 
# define let W = max capacity of elevator
# define let w = weights
W = max(capacity_of_elevator)
w = weight
M = {1,2,3,4,5,6}
    
i:int = 1
Result = {}
while not M:
    Material = Rule(M,W)
    Result.append(Material)
    M.remove(Material)

def Rule (M:int , Max_capacity:int):
    selected = []
    current_weight = w[i]
    while (current_weight <= Max_capacity):
        selected.append(M[i])
        i += 1 
        current_weight += w[i]
    return selected
