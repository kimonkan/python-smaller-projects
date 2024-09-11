counter = 0

user_string = input("Enter some text to see how many vowels are in that text: ")

for letter in user_string:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        counter += 1

print(counter)