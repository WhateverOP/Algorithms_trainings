s = input()
l = list(map(int, s.split(' ')))
x = int(input())

print(l)
print(x)

def two_terms_with_sum_x(nums, x):
    prev_nums = set()
    for now_num in nums:
        if x - now_num in prev_nums:
            return now_num, x - now_num
        prev_nums.add(now_num)
    return 0, 0

print(two_terms_with_sum_x(l, x))