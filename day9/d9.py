

def allZeros(seq):
    
    for num in seq:
        if num != 0:
            return False
        
    return True

def diffSeq(seq):
    newSeq = []
    
    for i in range(len(seq) - 1):
        newSeq.append(seq[i+1] - seq[i])
        
    return newSeq

def part1(data):
    
    # variables
    ans = 0
    
    # loop through each seq
    for hist in data:
        seq = list(map(int, hist.strip().split()))
        endValue = seq[-1]
        
        while True:
            diff = diffSeq(seq)
            zero = allZeros(diff)
            endValue += diff[-1]
        
            if zero: break
            seq = diff
            
        ans += endValue
        
    return ans

def part2(data):
    # variables
    ans = 0
    
    # loop through each seq
    for hist in data:
        seq = list(map(int, hist.strip().split()))
        startValue = seq[0]
        alternate = True
        
        while True:
            diff = diffSeq(seq)
            zero = allZeros(diff)
            if alternate:
                startValue -= diff[0]
                alternate = False
            else:
                startValue += diff[0]
                alternate = True
            
            if zero: break
            seq = diff
            
        # print(startValue)
        ans += startValue
        
    return ans
    
        
file = open("input.txt", "r")
data = file.readlines()

print(part1(data))
print(part2(data))