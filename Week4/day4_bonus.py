from random import randint

def find_pairs(lst, target):
    total = 0
    # pairs = []

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                total += 1
                # pairs.append((lst[i], lst[j]))

    print(total)
    # return pairs

numlist = [randint(0, 10000) for _ in range(20000)]
target = 3728

find_pairs(numlist, target)