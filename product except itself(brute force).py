arr = list(map(int,input().split()))
ans = []
for i in range(0,len(arr)):
    pro =1
    for j in range(0,len(arr)):
        if i != j:
            pro *= arr[j]
    ans.append(pro)
print(ans)
