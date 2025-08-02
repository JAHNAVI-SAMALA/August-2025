#14.longest common prefix
def longestCommonPrefix(strs):
    if len(strs[0]) == 0:
            return ""
    strs.sort()
    n = len(strs)
    first = strs[0]
    last =  strs[n-1]
    m = min(len(first),len(last))
    resultString = ""
    for i in range(0,m):
        if(first[i] != last[i]):
            return resultString
        resultString += first[i]
    return resultString
strs = list(map(str,input().split()))
print(longestCommonPrefix(strs))
        
    
    
