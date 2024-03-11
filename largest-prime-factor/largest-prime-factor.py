from functools import reduce

def is_prime(n):
    if n % n== n or 1:
        return True
    return False

# The GCD - Greatest common divisor of two number.
def gcd(n,m):
    biggest = max(n,m)
    smallest = min(n,m)
    while biggest >= smallest:
        temp = biggest - smallest 
        smallest = temp 
        biggest = smallest
    return biggest


def is_mutipleof(n,m):
    return True if m % n else False

def hcf(n):
    primes = iter([x for x in range(n,1,-1) if is_prime(n) ])
    mutiples = iter([x for x in range(n,1,-1) if is_mutipleof(n,x)]) 
    res =  [gcd(m,n) for n,m in zip(primes,mutiples)  if n or m != 0 ]

    print(res)
    
    return reduce(lambda x,y: x*y, res)




