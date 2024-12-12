from itertools import product

equations = []
with open('input.txt') as file:
    for line in file:
        ans, nums = line.split(":")
        ans = int(ans)
        nums = list(map(int, nums.split()))
        equations.append([ans, nums])

    
def get_possible_instructions(operator_list, num_parameters):
    return list(product(operator_list, repeat=num_parameters - 1))
    
def faster_evaluate_expression(target, nums, operators):
    res = nums[0]
    
    for i , op in enumerate(operators):
        if res > target:
            break
        if op == "+":
            res += nums[i + 1]
        elif op == "*":
            res *= nums[i + 1]
        elif op == "||":
            res = int(str(res) + str(nums[i + 1]))
    return res == target

total = 0
for equation in equations:
    possible_operators = get_possible_instructions(["+", "*", "||"], len(equation[1]))
    for operators in possible_operators:
        if faster_evaluate_expression(equation[0], equation[1], operators):
            total += equation[0]
            break

print(total)
