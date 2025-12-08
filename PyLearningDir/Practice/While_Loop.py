# While Loop

i=1
while i <= 10:
    print(i,sep=',',end="")
    i = i + 1

print("===============================")

k=0
while k<6:
    l=0
    while l < k:
        print(l+1,sep=',',end=" ")
        l = l + 1
    print(" ")
    k = k + 1

print("===============================")

m=5
while m>=1:
    n=1
    while m>n:
        print(n,end=" ")
        n=n+1
    print(" ")
    m = m - 1
