def longest_word(sentence):
    words = sentence.split()

    longest = ""
    longest_length = 0

    for word in words:
        word_length = len(word)

        if word_length > longest_length:
            longest = word
            longest_length = word_length

    return longest

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))  
