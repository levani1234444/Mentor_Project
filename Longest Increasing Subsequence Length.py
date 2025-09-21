# Task 9: Longest Increasing Subsequence Length
# Write a function lis_length(nums) that returns the length of the longest strictly increasing subsequence.
# Test Cases:
# lis_length([10,9,2,5,3,7,101,18]) == 4  # [2,3,7,101]
# lis_length([0,1,0,3,2,3]) == 4
# lis_length([7,7,7,7]) == 1


def lis_length(ls):
    result = len(ls) * [1]
    for i in range(len(ls)):
        for j in range(i):
            if ls[i] > ls[j]:
                result[i] = max(result[i], result[j] + 1)

    return max(result)
print(lis_length([7,7,7,7]))