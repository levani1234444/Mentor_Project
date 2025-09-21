# Task 5: Remove Consecutive Duplicates
# Write a function remove_consecutive_duplicates(s) that removes consecutive duplicate characters from a string.
# Test Cases:
# remove_consecutive_duplicates("aaabbcddd") == "abcd"
# remove_consecutive_duplicates("hellooo") == "helo"
# remove_consecutive_duplicates("abc") == "abc"


def remove_consecutive_duplicates(st):
    resutl = []
    for i in range(len(st)):
        if st[i] != st[i - 1]:
            resutl.append(st[i])
        else:
            continue
    
    return ''.join(resutl)

print(remove_consecutive_duplicates("aaabbcddd"))