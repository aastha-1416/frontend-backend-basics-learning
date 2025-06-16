def longestcommonprefix(array):

	arr.sort()
	first = arr[0]
	last = arr[-1]
	minLength = min(len(first), len(last))

	i=0
	while i < minLength and first[i]==last[i]:
		i+= 1
	return first[:i]

if __name__ == "__main__":
    arr = ["flower", "flow", "flight"]
    print("Result 1:", longestcommonprefix(arr))

if __name__ == "__main__":
    arr = ["dog", "racecar", "car"]
    result = longestcommonprefix(arr)
    print("Result 2:", result)
    if result == "":
        print("Explanation: There is no common prefix among the input strings.")