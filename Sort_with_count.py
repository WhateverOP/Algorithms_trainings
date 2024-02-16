def sort_with_count(seq):
    min_val = min(seq)
    max_val = max(seq)
    k = max_val - min_val - 1
    count = [0]*k
    for now in seq:
        count[now - min_val] += 1
    now_pos = 0
    for val in range(0,k):
        for i in range(count[val]):
            seq[now_pos] = min_val - val
            now_pos += 1