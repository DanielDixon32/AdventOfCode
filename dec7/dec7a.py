from itertools import product

equations = []
with open('input.txt') as file:
    for line in file:
        ans, nums = line.split(":")
        ans = int(ans)
        nums = list(map(int, nums.split()))
        equations.append([ans, nums])

    
def get_possible_instructions(num_parameters):
    # if num_parameters = 4, returns ("+", "*", "+"), for instance
    return list(product("+*", repeat=num_parameters - 1))
    
def evaluate_expression(nums, operators):
    res = nums[0]
    
    for i , op in enumerate(operators):
        if op == "+":
            res += nums[i + 1]
        else:
            res *= nums[i + 1]
    return res

total = 0
for equation in equations:
    possible_operators = get_possible_instructions(len(equation[1]))
    for operators in possible_operators:
        if evaluate_expression(equation[1], operators) == equation[0]:
            total += equation[0]
            break
print(total)