def ncr(n,r):
    ans =1
    for i in range(r):
        ans = ans*(n-i)
        ans = ans//(i+1)
    return ans
row = int(input())
result = []
for col in range(1,row+1):
    result.append(ncr(row-1,col-1))
print(result)
