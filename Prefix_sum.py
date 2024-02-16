def make_prefix_sum(nums):
    prefix_sum = (len(nums) + 1)*[0]
    for i in range(1, len(nums) + 1):
        prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
    return prefix_sum

def rsq(prefix_sum, l, r):
    return prefix_sum[r] - prefix_sum[l]