def count_char_occurrences(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

string1 = "Programming is cool!"
char1 = "o"
print("String:", string1)
print("Character:", char1)
print(count_char_occurrences(string1, char1))

string2 = "This is a great example"
char2 = "y"
print("String:", string2)
print("Character:", char2)
print(count_char_occurrences(string2, char2))