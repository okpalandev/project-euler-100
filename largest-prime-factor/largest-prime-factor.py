def is_prime(n,m):
    if m%  n==1:
        return True
    return False

# The GCD - Greatest common divisor of two number
def gcd(n,m):
    biggest = max(n,m)
    smallest = min(n,m)
    while biggest >= smallest:
        if is_prime(biggest,smallest):
            temp = biggest - smallest 
            biggest = smallest
            smallest = temp 
    return biggest


x= gcd(10,2)
print(x)

