a={1,2,3,4,5,6,55,66,23,45}
prime=set()
nprime=set()
for i in a:
    if i>=1:
        for j in range(2,i):
            if i%j==0:
                nprime.add(i)
                break
        else:
            prime.add(i)
print("prime set : ",prime)
print("not prime set : ",nprime)