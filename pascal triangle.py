row = int(input())
ans =1
result = [ans]
for col in range(1,row):
    ans = ans*(row-col)
    ans = ans//col
    result.append(ans)
print(result)
    
