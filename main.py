def memoize(f):

    fDict = {}

    def memo_f(n):
        if n not in fDict.keys():
            fDict[n] = f(n)
        return fDict[n]

    return memo_f


@memoize
def fib(n):
    if n <= 0:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range (1,30):
	print(fib(i))