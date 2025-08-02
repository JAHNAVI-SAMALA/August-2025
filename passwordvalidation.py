s = input()
upper=0
lower=0
number = 0
special = 0
for i in s:
    if i.isupper():
        upper += 1
    elif  i.islower():
        lower += 1
    elif i.isdigit():
        number += 1
    else:
        special += 1
if len(s) >= 8:
    if upper >=1 and lower >= 1 and number >= 1 and special >= 1:
        print("Strong password")
else:
    if len(s) == 0:
        print("Please enter the password")
    else:
        print("Weak password")
