memoFib = {}

def fib(n):
    if n in memoFib:
        return memoFib[n]

    if n < 2:
        return n

    memoFib[n] = fib(n - 1) + fib(n - 2)
    return memoFib[n]