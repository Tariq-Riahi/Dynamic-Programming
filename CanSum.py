memoSum = {}

def canSum(target, numbs):
    res = []

    if target in memoSum.keys():
        return memoSum[target]

    for num in numbs:
        if target - num == 0:
            res.append(True)
        if target - num > 0:
            res.append(canSum(target - num, numbs))

    memoSum[target] = (True in res)
    return memoSum[target]