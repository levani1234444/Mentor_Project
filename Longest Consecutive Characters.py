# Task 10: Longest Consecutive Characters
# Write a function longest_consecutive_char(s) that returns the longest run of the same character.
# Test Cases:
# longest_consecutive_char("aaabbbaaac") == ("a",3)
# longest_consecutive_char("bbbbb") == ("b",5)
# longest_consecutive_char("") == ("",0)

def longest_consecutive_char(st):
    if st == '':
        return ('', 0)
    
    thing = st[0]
    number = 1
    count = 1

    for i in range(1, len(st)):
        if st[i] == st[i - 1]:
            count += 1
        else:
            if count > number:
                number = count
                thing = st[i - 1]
            count = 1

    if count > number:
        number = count
        thing = st[-1]

    return (thing, number)


print(longest_consecutive_char("aaabbbaaac"))