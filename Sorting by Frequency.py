# Task 1: Sorting by Frequency
# Write a function sort_by_frequency(lst) that returns the list sorted by frequency of elements
# (most frequent first). If two numbers have the same frequency, keep the smaller number first.
# Test Cases:
# sort_by_frequency([4,4,1,2,2,3,3,3]) == [3,3,3,2,2,4,4,1]
# sort_by_frequency([10,20,10,30,20,10]) == [10,10,10,20,20,30]
# sort_by_frequency([]) == []



def sort_by_frequency(lst):
    count = {}
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    
    sorted_lst = sorted(lst, key=lambda x: (-count[x], x))
    
    return sorted_lst


print(sort_by_frequency([4,4,1,2,2,3,3,3]))  
print(sort_by_frequency([10,20,10,30,20,10])) 
print(sort_by_frequency([]))                  
