def fizzBuzz(n):
    l1=[]
    for i in range(1,n+1):
        if i%3 == 0 and i>=3:
            l1.append("Fizz")
        else:
            l1.append(i)
    return l1
