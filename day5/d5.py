
def rangeDict(key, val, rng):
    newDict = {}
    
    newDict[(key, key + rng)] = (val, val + rng)
        
    return newDict

def propagateVal(num, dict):
    
    for key in dict.keys():
        
        # check if in bounds
        if num <= key[1] and num >= key[0]:
            diff = num - key[0]
            return dict[key][0] + diff
    
    return num

def processSeed(num, maps):
    
    for map in maps:
        num = propagateVal(num, map)
        
    return num

file = open("input.txt", "r")
data = file.readlines()
n = len(data)

seeds = []
seedToSoil = {}
soilToFertilizer = {}
fertilizerToWater = {}
waterToLight = {}
lightToTemp = {}
tempToHumidity = {}
humidityToLocation = {}

i = 0
while i < n:
    line = data[i].strip()
    # print(line)
    
    if i == 0:
        # do seeds
        word, seedNums = line.split(":")
        seeds = list(map(int, seedNums.split()))
    elif line == "seed-to-soil map:":
        i += 1
        # extract data
        line = data[i].strip()
        while line != "":
            dest, src, rng = map(int, line.split())
            seedToSoil.update(rangeDict(src, dest, rng))
            i += 1
            line = data[i].strip()
    elif line == "soil-to-fertilizer map:":
        i += 1
        # extract data
        line = data[i].strip()
        while line != "":
            dest, src, rng = map(int, line.split())
            soilToFertilizer.update(rangeDict(src, dest, rng))
            i += 1
            line = data[i].strip()
    elif line == "fertilizer-to-water map:":
        i += 1
        # extract data
        line = data[i].strip()
        while line != "":
            dest, src, rng = map(int, line.split())
            fertilizerToWater.update(rangeDict(src, dest, rng))
            i += 1
            line = data[i].strip()
    elif line == "water-to-light map:":
        i += 1
        # extract data
        line = data[i].strip()
        while line != "":
            dest, src, rng = map(int, line.split())
            waterToLight.update(rangeDict(src, dest, rng))
            i += 1
            line = data[i].strip()
    elif line == "light-to-temperature map:":
        i += 1
        # extract data
        line = data[i].strip()
        while line != "":
            dest, src, rng = map(int, line.split())
            lightToTemp.update(rangeDict(src, dest, rng))
            i += 1
            line = data[i].strip()
    elif line == "temperature-to-humidity map:":
        i += 1
        # extract data
        line = data[i].strip()
        while line != "":
            dest, src, rng = map(int, line.split())
            tempToHumidity.update(rangeDict(src, dest, rng))
            i += 1
            line = data[i].strip()
    elif line == "humidity-to-location map:":
        i += 1
        # extract data
        line = data[i].strip()
        while line != "":
            dest, src, rng = map(int, line.split())
            humidityToLocation.update(rangeDict(src, dest, rng))
            i += 1
            if i == n:
                break
            line = data[i].strip()
    
    i += 1
    
ans = float("inf")

seedsLen = len(seeds)

maps = [seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemp, tempToHumidity, humidityToLocation]

for i in range(0, seedsLen, 2):
    start = seeds[i]
    rng = seeds[i+1]
    # print(start)
    
    candidateLoc = float("inf")
    candidateStart = start
    for j in range(start, start + rng, 1000):
        seed = j
    
        location = processSeed(seed, maps)
        
        if location < candidateLoc:
            candidateLoc = location
            candidateStart = j
        
    while True:
        candidateStart = candidateStart - 1
        newLoc = processSeed(candidateStart, maps)
        if newLoc > candidateLoc:
            break
        candidateLoc = newLoc
        
    ans = min(candidateLoc, ans, processSeed(candidateStart - 1, maps))
    
    
print(ans)
    

