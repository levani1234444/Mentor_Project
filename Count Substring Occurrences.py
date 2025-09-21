# Task 6: Count Substring Occurrences
# Write a function count_substring(text, sub) that returns how many times a 
# substring sub occurs in text (overlaps allowed).
# Test Cases:
# count_substring("aaaa", "aa") == 3
# count_substring("hello hello", "lo") == 2
# count_substring("banana", "ana") == 2


def count_substring(text, sub):
    count = 0
    for i in range(len(text) - len(sub) + 1):
        if text[i:i + len(sub)] == sub:
            count = count + 1
    
    return count

print(count_substring("hello hello", "lo"))