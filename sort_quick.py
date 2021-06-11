import random

def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choise(nums)
    l_nums = [n for n in nums if n <q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if h > q]
    return quicksort(l_nums) + e_nums +quicksort(b_nums)

x = [1, 4, 2, -1, -52, 64, 32, 43]
quicksort(x)
print(x)