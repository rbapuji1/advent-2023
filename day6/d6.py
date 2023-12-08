
def calcDist(race, release):
    return (race - release) * release

def differentWays(time, record):
    
    # if middle doesnt work, no time
    if calcDist(time, time // 2) < record:
        return 0
    
    low, high = 0, time
    left_bound, right_bound = None, None

    while low <= high:
        mid = low + (high - low) // 2
        if calcDist(time, mid) > record:
            left_bound = mid
            high = mid - 1
        else:
            low = mid + 1

    low, high = 0, time

    while low <= high:
        mid = low + (high - low) // 2
        if calcDist(time, mid) > record:
            right_bound = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return right_bound - left_bound + 1
    
def part1(timesRaw, distsRaw):
    times = list(map(int, timesRaw.strip().split()[1::]))
    dists = list(map(int, distsRaw.strip().split()[1::]))

    ans = 1
    for time, record in zip(times, dists):
        ans *= differentWays(time, record)
        
    print(ans)
    
def part2(timesRaw, distsRaw):
    time = int("".join(timesRaw.strip().split()[1::]))
    dist = int("".join(distsRaw.strip().split()[1::]))

    ans = differentWays(time, dist)
        
    print(ans)
    

# file = open("test.txt", "r")
file = open("input.txt", "r")
timesRaw, distsRaw = file.readlines()

part1(timesRaw, distsRaw)
part2(timesRaw, distsRaw)




