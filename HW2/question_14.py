V = 1234 # Tarsget number
coins = [1,5,10,25,50,100]
coins_all_types = len(coins)
print("We have coins",coins_all_types,"types")
answer = []
traversal = coins_all_types - 1 # Do a traversal all of coin types
while traversal >= 0 :
    while V >= coins[traversal]: # Find the minimum coins 
        V = V - coins[traversal]
        answer.append(coins[traversal])
    traversal = traversal - 1
for traversal in range(len(answer)):
    print("Coins ",traversal,"equal to",answer[traversal])
print("Total coins is : ",len(answer))
