def merge_sorted_lists(a, b, reverse=False):
    i, j = 0, 0
    result = []

    #  დალაგებული სიის გაერთიანება
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # ნაშთების დამატება
    while i < len(a):
        result.append(a[i])
        i += 1

    while j < len(b):
        result.append(b[j])
        j += 1

    # თუ reverse=True → ხელით ვაბრუნებთ სიას
    if reverse:
        reversed_result = []
        for k in range(len(result) - 1, -1, -1):
            reversed_result.append(result[k])
        return reversed_result

    return result
print(merge_sorted_lists([0,5,12],[2,3,6,15],reverse=True))