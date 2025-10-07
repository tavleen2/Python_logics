from functools import reduce 
# a =[2,3,1,4,1,5]
#     # [5,1,4,1,5]
#     # [6,4,1,5]
#     # [10,1,5]
#     # [11,5]
#     # [16]]

numbers = [1, 2, 3, 4, 5]

# Calculate the sum of all numbers using reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15

# Calculate the product of all numbers using reduce
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(product_of_numbers)  # Output: 120

#reduce with initializer
empty_list_sum = reduce(lambda x,y: x+y, [], 0)
print(empty_list_sum) # 0

# Without the initializer:
# empty_list_sum = reduce(lambda x,y: x+y, []) # raises TypeError

# Equivalent using a loop (for sum):
total = 0
for x in numbers:
    total += x
print(total)  # 15