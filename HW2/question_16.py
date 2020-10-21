# Algorithm for question number 16
answer = 0
n = 1
m = 10
while m > n :
    if m % 2 != 0:
        m -= 1
        answer = answer + 1
    else: 
        m : int = m / 2
        answer = answer + 1
print(int(answer + n - m))
