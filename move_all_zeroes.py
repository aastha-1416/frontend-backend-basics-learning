array1 = [0, 1, 0, 3, 12]
array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]
print ("array1",array1)
print("array2",array2)
def move_zeroes(arr):
    result = []
    zero_count = 0

    for num in arr:
        if num == 0:
            zero_count += 1
        else:
            result.append(num)

    result.extend([0] * zero_count)
    return result
print("Updated array1:", move_zeroes(array1))
print("Updated array2:", move_zeroes(array2))
