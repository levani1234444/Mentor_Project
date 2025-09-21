# Task 10: Longest Consecutive Characters
# Write a function longest_consecutive_char(s) that returns the longest run of the same character.
# Test Cases:
# longest_consecutive_char("aaabbbaaac") == ("a",3)
# longest_consecutive_char("bbbbb") == ("b",5)
# longest_consecutive_char("") == ("",0)


def longest_consecutive_char(st):
    result = []

    for i in st:
        if st.count(i) > 1:
            