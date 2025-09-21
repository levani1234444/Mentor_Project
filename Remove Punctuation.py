# Task 3: Remove Punctuation
# Write a function remove_punctuation(s) that removes all punctuation characters from a string.
# Test Cases:
# remove_punctuation("Hello, world!") == "Hello world"
# remove_punctuation("Python: easy? Yes!") == "Python easy Yes"



def remove_punctuation(st):
    punctuation = '!?:/;[].'

    result = ''
    for i in st:
        if i in punctuation:
            continue
        else:
            result = result + i

    return result

print(remove_punctuation("Python: easy? Yes!"))