#451
""" lambda functions are anonymous functions
we can use these in place of function definition
Syntax:
            variable = lambda(argument1,argument2:expression)
"""
s = input().strip()
def frequencySort(s):
    d ={}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    s_d = sorted(d.items(),key = lambda y : -y[1])
    resultStr = ""
    for key,value in s_d:
        for i in range(value):
            resultStr += key
    return resultStr
print(frequencySort(s))
