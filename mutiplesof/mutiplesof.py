def mutiplesof():
    arr = []
    for i  in range(1000,1,-1):
        if  i % 3 == 0 or i % 5 == 0 and i < 1000:
            arr.append(i)
    return sum(arr)

print('The sum of all the multiples of 3 or 5 below 1000 is: ', mutiplesof())

