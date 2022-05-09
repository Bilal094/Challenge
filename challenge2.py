lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]

def count_positives_sum_negatives(arr):
    positive = 0
    negative = 0
    for x in arr:
        if x < 0:
            negative += x
        elif x > 0:
            positive += 1
    arr.clear()
    arr.append(positive)
    arr.append(negative)
    return arr
print(count_positives_sum_negatives(lst))