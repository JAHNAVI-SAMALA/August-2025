s = input()
vowels = "aeiou"
vowel_count = consonant_count = 0
for i in s:
    if i in vowels:
        vowel_count += 1
    else:
        consonant_count += 1
print ("No.of vowels:",vowel_count)
print("No.of consonants:",consonant_count)
