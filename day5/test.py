import copy

InputList = []
with open("input.txt", "r") as data:
    for t in data:
        Line = t.strip()
        InputList.append(Line)

MapList = []
SeedList = InputList[0].split()
del SeedList[0]
SeedList = list(map(int, SeedList))
del InputList[0:2]

CurrentTupleList = []
for i in InputList:
    if "map" in i:
        continue
    elif i == "":
        CurrentTupleList.sort()
        NewTuple = tuple(CurrentTupleList)
        MapList.append(NewTuple)
        CurrentTupleList = []
        continue
    A, B, C = i.split()
    NewTuple = (int(B), int(A), int(C))
    CurrentTupleList.append(NewTuple)

CurrentTupleList.sort()
NewTuple = tuple(CurrentTupleList)
MapList.append(NewTuple)

def Mapping(InValue, Map):
    for SourceStart, DestStart, Range in Map:
        SourceEnd = SourceStart + Range - 1
        if SourceStart <= InValue <= SourceEnd:
            Offset = InValue - SourceStart
            FinalDestination = DestStart + Offset
            return FinalDestination
    return InValue

SeedLocationValues = []
for Seed in SeedList:
    CurrentValue = Seed
    for m in MapList:
        NextValue = Mapping(CurrentValue, m)
        CurrentValue = NextValue
    SeedLocationValues.append(NextValue)

Part1Answer = min(SeedLocationValues)

def MappingP2(Start, Range, Map):
    End = Start + Range - 1
    NewStart = Start
    ReturnList = []
    for SourceStart, DestStart, MRange in Map:
        SourceEnd = SourceStart + MRange - 1
        if NewStart > SourceEnd:
            continue
        elif End < SourceStart:
            NewRange = End - NewStart + 1
            if NewRange >= 1:
                ReturnList.append((NewStart, NewRange))
            break
        elif NewStart >= SourceStart and End <= SourceEnd:
            Offset = NewStart - SourceStart
            ReturnStart = DestStart + Offset
            ReturnRange = End - NewStart + 1
            ReturnList.append((ReturnStart, ReturnRange))
            break
        elif NewStart >= SourceStart and End > SourceEnd:
            Offset = NewStart - SourceStart
            ReturnStart = DestStart + Offset
            ReturnRange = SourceEnd - NewStart + 1
            ReturnList.append((ReturnStart, ReturnRange))
            NewStart = SourceEnd + 1
        elif NewStart < SourceStart and End <= SourceEnd:
            FirstRange = SourceStart - NewStart
            ReturnList.append((NewStart, FirstRange))
            SecondRange = End - SourceStart + 1
            ReturnList.append((DestStart, SecondRange))
            break
        elif NewStart < SourceStart and End > SourceEnd:
            FirstRange = SourceStart - NewStart
            ReturnList.append((NewStart, FirstRange))
            ReturnList.append((DestStart, MRange))
            NewStart = SourceEnd + 1
    if SourceEnd < NewStart:
        NewRange = End - NewStart + 1
        ReturnList.append((NewStart, NewRange))

    ReturnList.sort()
    ReturnTuple = tuple(ReturnList)
    return ReturnTuple

SeedListP2 = []
SeedNum = len(SeedList)
for t in range(SeedNum//2):
    A, B = SeedList[t*2], SeedList[t*2+1]
    SeedListP2.append((A,B))

Part2Answer = 10**15
for s in SeedListP2:
    TraveralList = [s]
    for m in MapList:
        NextList = []
        for A, B in TraveralList:
            NextValues = MappingP2(A,B,m)
            for v in NextValues:
                NextList.append(v)
        NextList.sort()
        TraveralList = copy.deepcopy(NextList)
    LowestLocation = NextList[0][0]
    if LowestLocation < Part2Answer:
        Part2Answer = LowestLocation

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")