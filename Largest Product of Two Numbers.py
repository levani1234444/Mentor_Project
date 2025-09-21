# Task 8: Largest Product of Two Numbers
# Write a function max_product(nums) that returns the largest product of any two numbers in the list.
# Test Cases:
# max_product([1,2,3,4]) == 12


def max_product(ls):
    nums_prod = ls[0] * ls[1]

    for i in range(len(ls)):
        for j in range(i + 1, len(ls)):
            product = ls[i] * ls[j]
        if product > nums_prod:
            nums_prod = product
        
    
    return nums_prod

print(max_product([-10,-20,5,3]))
