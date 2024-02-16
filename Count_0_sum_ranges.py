def count_prefix_sums(nums):
    prefix_sum_by_value = {0: 1}
    now_sum = 0
    for now in nums:
        now_sum += now
        if now_sum not in prefix_sum_by_value:
            prefix_sum_by_value[now_sum] = 0
        prefix_sum_by_value[now_sum] += 1
    return prefix_sum_by_value

def count_0_sum_ranges(prefix_sum_by_value):
    ranges_counter = 0
    for now_sum in prefix_sum_by_value:
        sums_counter = prefix_sum_by_value[now_sum]
        ranges_counter += sums_counter * (sums_counter - 1) // 2
    return ranges_counter