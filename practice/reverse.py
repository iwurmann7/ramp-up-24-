def reverse(my_string):
    return ''.join(reversed(my_string))

def vowels(my_string):
    return sum(1 for char in my_string if char.lower() in 'aeiou')

word = input("Enter a word: ")
print ("Reversed word:", reverse(word))
print ("Amount of vowels:", vowels(word))