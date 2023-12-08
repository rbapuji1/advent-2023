import numpy as np

def part1(data):

    dirDict = {} # ex. AAA: (BBB, CCC)
    leftRight = data[0].strip()
    
    for i in range(2, len(data)):
        key, valTuple = data[i].strip().split("=")
        left, right = valTuple.strip("() ").split(",")
        dirDict[key.strip()] = (left.strip(), right.strip())
        
    # print(dirDict)
    curPos = "AAA"
    dirIdx = 0
    steps = 0
    
    while curPos != "ZZZ":
        dir = leftRight[dirIdx]
        
        if dir == "L":
            curPos = dirDict[curPos][0]
        else:
            curPos = dirDict[curPos][1]
            
        steps += 1
        dirIdx += 1
        
        if dirIdx == len(leftRight):
            dirIdx = 0
            
    return steps

def part2(data):

    dirDict = {} # ex. AAA: (BBB, CCC)
    leftRight = data[0].strip()
    starts = []
    
    for i in range(2, len(data)):
        key, valTuple = data[i].strip().split("=")
        left, right = valTuple.strip("() ").split(",")
        dirDict[key.strip()] = (left.strip(), right.strip())
        if key.strip()[2] == "A":
            starts.append(key.strip())
    
    allSteps = []
    
    for start in starts:   
        curPos = start
        steps = 0
        dirIdx = 0
        while curPos[2] != "Z":
            dir = 0 if leftRight[dirIdx] == "L" else 1
            curPos = dirDict[curPos][dir]
            
            steps += 1
            dirIdx += 1
            
            if dirIdx == len(leftRight):
                dirIdx = 0
                
        allSteps.append(steps)
            
    return np.lcm.reduce(allSteps)
    
    
    
    
    
file = open("input.txt", "r")
# print(part1(file.readlines()))
print(part2(file.readlines()))