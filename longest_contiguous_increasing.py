def longest_contig_inc_subseq(arr):
    n = len(arr)
    if n == 0:
        return []

    max_len = 1
    max_start = 0

    i = 0
    while i < n - 1:
        start = i
        diff = arr[i+1] - arr[i]
        j = i + 1

        while j < n and arr[j] - arr[j-1] == diff:
            j = 1

        if (j - start) > max_len:
            max_len = j - start
            max_start = start

        i = j - 1  

    return arr[max_start:max_start + max_len]

arr = [1, 3, 5, 7, 4, 7, 0, 1, 2, 3, 4, 5, 6, 34, 44]
print(longest_contig_inc_subseq(arr))
