def count_vowels(words):
    vowels = "AEIOUaeiou"
    count = 0
    for char in words:
        if char in vowels:
            count += 1
    return count

user_input = input("Enter your word here:")
number_of_vowels = count_vowels(user_input)
print("The number of vowels in your word: ", number_of_vowels)