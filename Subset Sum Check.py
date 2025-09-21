# Task 7: Subset Sum Check
# Write a function has_subset_sum(nums, target) that returns True if any subset of numbers adds up to target.
# Test Cases:
# has_subset_sum([3,34,4,12,5,2], 9) == True  # 4+5
# has_subset_sum([3,34,4,12,5,2], 30) == False
# has_subset_sum([], 0) == True

def has_subset_sum(ls, tar):
    result = False
    res = []
    for i in range(len(ls)):
        for j in range(i + 1, len(ls)):
            res.append((ls[i] + ls[j]))
    if ls == [] and tar == 0:
        return True
    for i in res:
        if i == tar:
            result = True
            return result
    
    return result


print(has_subset_sum([], 0))