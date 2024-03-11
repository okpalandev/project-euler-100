from itertools import combinations, permutations,accumulate
from functools import reduce

def fact(n):
    if n <=1: return 1
    return n * fact(n-1)

def partition(n):
    combinator = [x for x in combinations(range(n),n-1)]
    permuter = [x for x in permutations(range(n),n-1)]
    joined =  set()
    for i,j in zip(permuter,combinator):
        joined.add(i)
        joined.add(j)
        joined.difference()
        yield (len(joined),i )


for n, p in combinations([x for x in partition(10)]):  
    counter = int(reduce(lambda a,b:a+b, [x for x in p]))
    acc = 0
    for data in p:
        if data %  int(1e6) == 0:
           acc+=data
    print(acc)