from collections import defaultdict

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if not sortRank(arr[j], arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def calculateRank(hand):
    # get counter
    counter = {}
    for c in hand:
        counter[c] = counter.get(c, 0) + 1
        
    # handle jokers (comment out block for part 1)
    if "J" in counter and len(counter) > 1:
        # find highest occ
        card, occ = sorted([[card, occ] for card, occ in counter.items() if card != "J"], key = lambda x: x[1], reverse = True)[0]
        # print(card, occ)
        counter[card] += counter["J"]
        del counter["J"]
    
    occs = sorted(list(counter.values()))
    # five of a kind
    if occs == [5]:
        return 7
    elif occs == [1, 4]: #four of a kind
        return 6
    elif occs == [2, 3]:
        return 5
    elif occs == [1, 1, 3]:
        return 4
    elif occs == [1, 2, 2]:
        return 3
    elif occs == [1, 1, 1, 2]:
        return 2
    else:
        return 1
    
def sortRank(low, high):
    handVals = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    
    for i in range(5):
        if low[i] == high[i]:
            continue
        
        if handVals[low[i]] > handVals[high[i]]:
            return False
        else:
            return True
        
    return True

def part1(data):
    # vars
    
    ans = 0
    handBids = {}
    handRanks = defaultdict(list) # 1: high card, 2: one pair, 3: two pair, 4: three of a kind, 5: full house, 6: four of a kind, 7: five of a kind
    n = len(data)
    
    # parse data
    for line in data:
        hand, bid = line.strip().split()
        handBids[hand] = int(bid)
        handRanks[calculateRank(hand)].append(hand)
    
    # sort ranking and concatenate
    curRank = 1
    for i in range(1, 8):
        sortedRange = bubble_sort(handRanks[i])
        if sortedRange is None:
            continue
        for hand in sortedRange:
            ans += handBids[hand] * curRank
            curRank += 1
    
    return ans

def part2(data):
    # vars
    
    ans = 0
    handBids = {}
    handRanks = defaultdict(list) # 1: high card, 2: one pair, 3: two pair, 4: three of a kind, 5: full house, 6: four of a kind, 7: five of a kind
    n = len(data)
    
    # parse data
    for line in data:
        hand, bid = line.strip().split()
        handBids[hand] = int(bid)
        handRanks[calculateRank(hand)].append(hand)
    
    # sort ranking and concatenate
    curRank = 1
    for i in range(1, 8):
        sortedRange = bubble_sort(handRanks[i])
        if sortedRange is None:
            continue
        for hand in sortedRange:
            ans += handBids[hand] * curRank
            curRank += 1
    
    return ans

file = open("input.txt", "r")
# print(f"Part 1 Answer: {part1(file.readlines())}")
print(f"Part 2 Answer: {part2(file.readlines())}")