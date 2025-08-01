def majorityElement(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans =[]
    for i,j in d.items():
        if j > len(nums)//3:
            ans.append(i)
    return ans
nums = list(map(int,input().split()))
print(majorityElement(nums))
