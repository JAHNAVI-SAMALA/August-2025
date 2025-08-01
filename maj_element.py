def majorityElement(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i] += d[i]+1
        else:
            d[i] = 1
    ans = []
    for key,val in d.items():
        if val > len(nums)//2:
            ans.append(key)
    return ans
nums = list(map(int,input().split()))
print(majorityElement(nums))
