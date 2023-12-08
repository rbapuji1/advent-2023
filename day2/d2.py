def checkLimit(seq):
    cubeSet = seq.split(",")
    
    for cubes in cubeSet:
        num, color = cubes.split()
        
        if color == "blue" and int(num) > 14:
            return False
        elif color == "green" and int(num) > 13:
            return False
        elif color == "red" and int(num) > 12:
            return False
    
    return True

def getPower(seq):
    red = 0
    green = 0
    blue = 0
    
    for seq in seqs.split(";"):
        cubeSet = seq.split(",")
        for cubes in cubeSet:
            num, color = cubes.split()
            num = int(num)
            
            if color == "blue":
                blue = max(blue, num)
            elif color == "green":
                green = max(green, num)
            elif color == "red":
                red = max(red, num)
    
    return red * blue * green

file = open("input.txt", "r")

ans = 0

for line in file.readlines():
    game, seqs = line.split(":")

    ans += getPower(line)

        
print(ans)