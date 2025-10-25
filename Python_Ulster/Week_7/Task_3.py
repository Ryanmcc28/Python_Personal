numbers = [12, 13, 44, 112, 1, 0, 3]
n = 2

def remove_outlier(numbers, n):
    fixed_nums = []
    for number in numbers:
        fixed_nums.append(number)
    for n in range(n):
        fixed_nums.remove(max(fixed_nums))
        fixed_nums.remove((min(fixed_nums)))
    return fixed_nums
print(remove_outlier(numbers,n))

