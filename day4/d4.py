
def pointsInCard(card):
    
    winning, yours = card.split('|')
    
    winningNums = set(winning.strip().split())
    yourNums = yours.strip().split()
    
    exp = 0
    
    for num in yourNums:
        if num in winningNums:
            exp += 1
                    
    return exp
    
    

file = open("input.txt", "r")
copies = {}
data = file.readlines()

for i in range(1, len(data) + 1):
    copies[i] = 1

for i in range(1, len(data) + 1):
    cardNo, allNums = data[i-1].strip().split(':')
    points = pointsInCard(allNums)
    
    # add multiples to the cards in front
    for j in range(i+1, i + points + 1):
        copies[j] += copies[i]
        
    # print(copies)
    
ans = sum(list(copies.values()))
print(ans)
    
    