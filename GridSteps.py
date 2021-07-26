memo = {}

def gridP(h, w):
    if h==0 or w==0: return 0
    if h==1 & w==1: return 1
    if (h,w) in memo.keys(): return memo[(h ,w)]

    memo[(h ,w)] = gridP(h-1, w) + gridP(h, w-1)
    return memo[(h ,w)]