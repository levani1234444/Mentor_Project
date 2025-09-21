# Task 4: Intersection of Two Dictionaries
# Write a function dict_intersection(d1, d2) that returns a dictionary containing keys 
# that appear in both dictionaries, with their values summed.
# Test Cases:
# dict_intersection({"a":1,"b":2},{"b":3,"c":4}) == {"b":5}
# dict_intersection({"x":10},{"y":5}) == {}


def dict_intersection(a, b):
    result = {}
    for i in b:
        if i in a:
            result[i] = b[i] + a[i]
    

    return result


print(dict_intersection({"x":10},{"y":5}))