from itertools import permutations

def fact(n):
    if n <=1: return 1
    return n * fact(n-1)

def partition(n):
    permuter = [x for x in permutations(range(n),n-1)]
    

print(partition(1000))
