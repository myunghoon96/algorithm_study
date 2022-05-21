from bisect import bisect_left, bisect_right

# or use set() o(1)

def search(arr, target):
    l_idx = bisect_left(arr, target)
    r_idx = bisect_right(arr, target)

    return 'yes' if r_idx - l_idx else 'no'

n = 5
have_items = [8,3,7,9,2]
m = 3
need_items = [5,7,9]

have_items.sort()
for need_item in need_items:
    result = search(have_items, need_item)
    print(result, end = ' ')
