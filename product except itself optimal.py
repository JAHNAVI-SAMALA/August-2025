def ProductExceptItself(nums):
    n = len(nums)
    prod =1
    left = [0]*n
    for i in range(0,n):
        prod = prod*nums[i]
        left[i] = prod
    prod =1
    right = [0] * n
    for i in range(n-1,-1,-1):
        prod = prod * nums[i]
        right[i] = prod
    ans = [0] * n
    ans[0] = right[1]
    for i in range(1,n-1):
        ans[i] = left[i-1]*right[i+1]
    ans[n-1] = left[n-2]
    return ans
nums = list(map(int,input().split()))
print(ProductExceptItself(nums))
