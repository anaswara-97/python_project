
def prime(n):
    sum=0
    for i in range(2, n):
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i,end=" ")
            sum+=i
    print("\nsum of prime numbers between 1-50 : ")
    return sum
print(prime(50))