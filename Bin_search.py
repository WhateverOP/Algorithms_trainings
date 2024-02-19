def l_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r) // 2
        if check(m, check_params):
            r = m
        else:
            l = m + 1
    return l

def r_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, check_params):
            l = m
        else:
            r = m - 1
    return l

def check_is_ge(index, params):
    seq, x = params
    return seq[index] >= x

def find_first_ge(seq, x):
    ans = l_bin_search(0, len(seq) - 1, check_is_ge, (seq, x))
    if seq[ans] < x:
        return len(seq)
    return ans