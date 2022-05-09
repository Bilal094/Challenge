lst = [1,2,3,4,7,8]

def first_non_consecutive(arr):
    x = arr[0]
    for y in range(len(arr)-1):
        x += 1
        if x not in arr:
            return arr[y+1]
    return None

print(first_non_consecutive(lst))