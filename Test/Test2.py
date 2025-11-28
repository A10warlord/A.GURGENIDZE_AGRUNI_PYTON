def merge_lists(a, b, reverse=False):
    i, j = 0, 0
    merged = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    while i < len(a):
        merged.append(a[i])
        i += 1

    while j < len(b):
        merged.append(b[j])
        j += 1

    if reverse:
        reversed_list = []
        for k in range(len(merged) - 1, -1, -1):
            reversed_list.append(merged[k])
        return reversed_list
    return merged