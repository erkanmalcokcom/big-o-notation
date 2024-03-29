# Constant Time O(1) Example: Function to check if a number is even.
def is_even(number):
    return number % 2 == 0

# Linear Time O(n) Example: Function to sum all elements in a list.
def sum_elements(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Quadratic Time O(n^2) Example: Function to compute a multiplication table up to n.
def multiplication_table(n):
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table

# Let's create some input data and run these functions to illustrate.
test_number = 4
test_list = [1, 2, 3, 4, 5]
test_n = 3

# Running the functions
is_even_result = is_even(test_number)
sum_elements_result = sum_elements(test_list)
multiplication_table_result = multiplication_table(test_n)

print(is_even_result, sum_elements_result, multiplication_table_result)

'''
* Constant Time - O(1): The function is_even checks if a number is even. This operation takes constant time because it involves only one operation regardless of the size of the input. For the number 4, the result is True, indicating that 4 is even.
* Linear Time - O(n): The function sum_elements takes a list of numbers and returns their sum. It runs in linear time because it involves a single loop through the list, so the time it takes will increase linearly with the number of elements in the list. The sum of the list [1, 2, 3, 4, 5] is 15.
* Quadratic Time - O(n^2): The function multiplication_table generates a multiplication table up to a given number n. It runs in quadratic time because it uses two nested loops: one to iterate through the numbers and another to multiply each number by the others. For n = 3, the multiplication table is a 3x3 matrix: [[1, 2, 3], [2, 4, 6], [3, 6, 9]].
'''