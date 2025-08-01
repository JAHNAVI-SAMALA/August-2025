#maximum subarray sum

nums = list(map(int,input().split()))
n = len(nums)
ans = []
for i in range(0,n):
    for j in range(i,n):
        ans.append(nums[i:j+1])
Max = float("-inf")
for lst in ans:
    if sum(lst) > Max:
        Max = sum(lst)
print(Max)
