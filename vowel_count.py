# Find vowels count from string

str = input('Enter a string: ')
print(str)

vowel_count = 0

for letter in str:
    if letter in 'aeiou' or letter in 'AEIOU':
        vowel_count += 1

print(vowel_count)
