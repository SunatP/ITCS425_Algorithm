def StepstoReachTarget(default_target, new_target):
    min_move = 0
    i = 0
    while len(new_target) > 0:
        # Find new location
        selected_new_loc = Select_min_move(default_target[0], new_target)
        new_target.remove(selected_new_loc)
        min_move = min_move + abs(default_target[i] - selected_new_loc)
        i += 1
    return min_move

#Select location that result in minimum location move
def Select_min_move(default_target, new_target):
    select_loc = new_target[0]
    for i in range(len(new_target)):
        if abs(default_target - new_target[i]) < abs(default_target - select_loc):
            select_loc = new_target[i]
    return select_loc

n = int(input())
loc = []
new_move = []
for i in range(n):
    loc.append(int(input()))
for i in range(n):
    new_move.append(int(input()))
min_move = StepstoReachTarget(loc, new_move)
print(min_move)