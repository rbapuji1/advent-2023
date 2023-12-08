# Day 1: Trebuchet

def getCalibration1(line):
    nums = [x for x in line if x.isnumeric()]

    return int(nums[0] + nums[-1])

def getCalibration2(line):
    nums = []
    n = len(line)
    words = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    
    for i in range(n):
        # print(i, line[i])
        if line[i].isnumeric():
            nums.append(line[i])
        else:
            # five letter numbers: 3, 7, 8
            if (n - i) >= 5 and line[i:(i+5)] in words:
                # print(line[i:(i+5)])
                nums.append(words[line[i:(i+5)]])
            # four letter numbers: 4, 5, 9
            if (n - i) >= 4 and line[i:(i+4)] in words:
                # print(line[i:(i+4)])
                nums.append(words[line[i:(i+4)]])
            # three letter numbers: 1, 2, 6
            if (n - i) >= 3 and line[i:(i+3)] in words:
                # print(line[i:(i+3)])
                nums.append(words[line[i:(i+3)]])
    print(nums)
    return int(nums[0] + nums[-1])

file = open("t1.txt", "r")

ans = 0
for line in file.readlines():
    # print(line)
    num = getCalibration2(line)
    # print(num)
    ans += num
    
print(ans)
