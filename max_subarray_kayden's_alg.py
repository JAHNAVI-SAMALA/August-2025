#kayden alg for maximum subarray sum
def maxSubarray(nums):
    n = len(nums)
    cs = 0
    ms = float("-inf")
    for i in nums:
        cs += i
        ms = max(ms,cs)
        if cs < 0:
            cs = 0
    return ms
nums = list(map(int,input().split()))
print(maxSubarray(nums))
