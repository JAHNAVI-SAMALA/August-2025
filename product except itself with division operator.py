#from typing import List
def productExceptSelf(nums):
    n = len(nums)
    no_of_zeroes = 0
    prod =1
    for i in nums:
        if i==0:
            no_of_zeroes +=1
        else:
            prod *= i
    ans  = []
    for i in nums:
        if no_of_zeroes > 1:
            ans.append(0)
        else:
           if  no_of_zeroes  == 1:
                if i == 0:
                    ans.append(prod)
                else:
                    ans.append(0)
           else:
                ans.append(prod//i)
    return ans
nums = list(map(int,input().split()))
print(productExceptSelf(nums))
