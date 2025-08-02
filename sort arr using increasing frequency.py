#sort arr based on increasing frequency
nums = list(map(int,input().split()))
def frequencySort(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] =1
    s_d = sorted(d.items(),key = lambda y:(y[1],-y[0]))
    resultList = []
    for key,value in s_d:
        for i in range(value):
            resultList.append(key)
    return resultList
print(frequencySort(nums))
