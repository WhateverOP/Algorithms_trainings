def count_pairs_wdgtK(sorted_nums, K):
    pairs_counter = 0
    last_i = 0
    for first_i in range(sorted_nums):
        while last_i < len(sorted_nums) and sorted_nums[last_i] <= sorted_nums[first_i]:
            last_i += 1
        pairs_counter += len(sorted_nums) - last_i
    return pairs_counter