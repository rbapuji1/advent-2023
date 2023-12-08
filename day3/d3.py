from collections import defaultdict

file = open("input.txt", "r")

schematic = [line.strip() for line in file.readlines()]
gears = defaultdict(list)
ans = 0

def checkSymbol(numLen, col, row):
    m = len(schematic)
    n = len(schematic[0])
    # check above
    if row != 0:
        left = max(col - numLen - 1, 0)
        right = min(col + 1, n - 1)
        top = schematic[row - 1][left:right]
        
        for s in top:
            if not s.isnumeric() and s != '.':
                return True
    
    # check left
    if (col - numLen) != 0:
        left = schematic[row][col - numLen - 1]
        if not left.isnumeric() and left != '.':
            return True
    
    # check right
    if col != n:
        right = schematic[row][col]
        if not right.isnumeric() and right != '.':
            return True
    
    # check below
    if row != (m - 1):
        left = max(col - numLen - 1, 0)
        right = min(col + 1, n - 1)
        bottom = schematic[row + 1][left:right]
        
        for s in bottom:
            if not s.isnumeric() and s != '.':
                return True
            
    return False

def checkGears(num, row, col, numLen):
    global ans
    m = len(schematic)
    n = len(schematic[0])
    # check above
    if row != 0:
        left = max(col - numLen - 1, 0)
        right = min(col + 1, n - 1)
        
        for j in range(left, right):
            s = schematic[row - 1][j]
            if s == "*":
                # gear not active
                if len(gears.get((row - 1, j), [])) == 0:
                    gears[(row - 1, j)].append(num)
                elif len(gears.get((row - 1, j), [])) == 1:
                    # print("top", gears, num)
                    ans += num * gears[(row - 1, j)][0]
                    del gears[(row - 1, j)]
    
    # check left
    if (col - numLen) != 0:
        left = schematic[row][col - numLen - 1]
        if left == "*":
            # gear not active
            if len(gears.get((row, col - numLen - 1), [])) == 0:
                gears[(row, col - numLen - 1)].append(num)
            elif len(gears.get((row, col - numLen - 1), [])) == 1:
                # print("left", gears, num)
                ans += num * gears[(row, col - numLen - 1)][0]
                del gears[(row, col - numLen - 1)]
    
    # check right
    if col != n:
        right = schematic[row][col]
        if right == "*":
            # gear not active
            if len(gears.get((row, col), [])) == 0:
                gears[(row, col)].append(num)
            elif len(gears.get((row, col), [])) == 1:
                # print("right", gears, num)
                ans += num * gears[(row, col)][0]
                del gears[(row, col)]
    
    # check below
    if row != (m - 1):
        left = max(col - numLen - 1, 0)
        right = min(col + 1, n - 1)
        
        for j in range(left, right):
            s = schematic[row + 1][j]
            if s == "*":
                # gear not active
                if len(gears.get((row + 1, j), [])) == 0:
                    gears[(row + 1, j)].append(num)
                elif len(gears.get((row + 1, j), [])) == 1:
                    # print("bottom", gears, num)
                    ans += num * gears[(row + 1, j)][0]
                    del gears[(row + 1, j)]
    
    # print(gears)



def sumPartNumbers():
    m = len(schematic)
    n = len(schematic[0])
    
    for i in range(m):
        line = schematic[i]
        # collect number
        j = 0
        tempNum = ''
        while j < n:
            if line[j].isnumeric():
                tempNum += line[j]
            else:
                if tempNum != '':
                    x = int(tempNum)
                    # print(x)
                    checkGears(x, i, j, len(tempNum))
                        
                    tempNum = ''
                
            j += 1
                
        if tempNum != '':
            x = int(tempNum)
            checkGears(x, i, j, len(tempNum))
    
    
sumPartNumbers()
print(ans)