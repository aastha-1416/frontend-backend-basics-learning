def areAnagrams(s1, s2, use_sorted=True):
    if len(s1) != len(s2):
        return False

    if use_sorted:
        return sorted(s1) == sorted(s2)
    else:
        freq1 = {}
        freq2 = {}

        for item in s1:
            freq1[item] = freq1.get(item, 0) + 1
        for item in s2:
            freq2[item] = freq2.get(item, 0) + 1

        return freq1 == freq2

if __name__ == "__main__":
    s1 = [1, 2, 3, 2]
    s2 = [2, 1, 3, 2]
    
    print("true" if areAnagrams(s1, s2, use_sorted=True) else "false")  # Using sorted
    print("true" if areAnagrams(s1, s2, use_sorted=False) else "false")  # Without using sorted
