# TODO здесь писать код
def qsort(arr):
    if len(arr) <= 1:
        return arr
    sep = arr[-1]
    left = []
    mid = []
    right = []
    for a in arr:
        if a < sep:
            left.append(a)
        elif a == sep:
            mid.append(a)
        else:
            right.append(a)
    return qsort(left)+mid+qsort(right)


list_sort = [5, 8, 9, 4, 2, 9, 1, 8]
print(qsort(list_sort))
