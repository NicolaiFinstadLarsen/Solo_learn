N = int(input())
count = 0

for x in range(0,N+1):   
    if x < N+1:
        count += x
print(count)