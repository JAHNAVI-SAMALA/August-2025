#group anagrams
from collections import defaultdict
def groupAnagram(strs):
    anagrams = defaultdict(list)
    for s in strs:
        s1 = "".join(sorted(s))
        anagrams[s1].append(s)
    return list(anagrams.values())
strs =list(map(str,input().split()))
print(groupAnagram(strs))

