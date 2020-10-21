import sys
p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k: int = 1
btime = 0
bt:int = []
at: int = []
wt: int = []
tt: int = []
ta: int = 0
sum: int = 0
wavg: float = 0
tavg: float = 0
tsum: float = 0
wsum: float = 0
print(" -------Shortest Job First Scheduling ( NP )-------\n")
n = int(input("Enter the No. of processes : "))

for i in range(n):
    # print("\tEnter the burst time of %d process :",i+1)
    a = int(input("Enter the burst time of %d process :"%(i+1)))
    bt.append(a)
    b= int(input("Enter the arrival time of %d process :"%(i+1)))
    # print("\tEnter the arrival time of %d process :",i+1)
    at.append(b)
    # print("burst time : ",bt[i])
    # print("Arrival time : ",bt[i])
for i in range(n):
    for j in range(n):
        if at[i] < at[j]:
            p[j],p[i] = p[i],p[j]``
            at[j],at[i] = at[i],at[j]
            bt[j],bt[i] = bt[i],bt[j]

for j in range(n):
    btime = btime + bt[j]
    min:int = bt[k]
    i = k
    for i in range(n):
        if (btime >= at[i] and bt[i] < min):
            p[k],p[i] = p[i],p[k]
            at[k],at[i] = at[i],at[k]
            bt[k],bt[i] = bt[i],bt[k]

k += 1
wt[0] = wt.append(0)
i = 1
for i in range(n):
    wt.append(i)
    bt.append(i)
    at.append(i)
    sum = sum + bt[i - 1]
    wt[i] = sum - at[i]
    wsum = wsum + wt[i]

wavg = wsum / n

i = 0
for i in range(n):
    bt.append(i)
    tt.append(i)
    at.append(i)
    ta = ta + bt[i]
    tt[i] = ta - at[i]
    tsum = tsum + tt[i]

tavg = tsum / n
print("************************")
print("\n RESULT:-")
print("\nProcess\t Burst\t Arrival\t Waiting\t Turn-around")
for i in range(n):
    print("\n p%d\t" %(p[i]), "%d\t"%(bt[i]), "%d\t\t"%(at[i]), "%d\t"%(wt[i]), "\t\t%d"%(tt[i]))

print("\n\nAVERAGE WAITING TIME : %.2f"%(wavg))
print("\nAVERAGE TURN AROUND TIME : %.2f"%(tavg))

