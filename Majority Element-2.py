def majorityElementII(arr):
	# Write your code here.
    n = len(arr)
    d = {}
    for i in range(n):
        if arr[i] in d:
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1
         
    major = []
    for key in d.keys():
        if d[key] > floor(n/3):
            major.append(key)

    return major