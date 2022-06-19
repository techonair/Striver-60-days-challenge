def findMajorityElement(arr, n):
	# Write your code here.
    cnt = tmp = 1
    major = arr[0]
    
    for i in range(1, n):
        if arr[i] == major:
            tmp += 1
        else:
            tmp -= 1
        if tmp == 0:
            cnt = max(cnt, tmp)
            tmp = 1
            major = arr[i]
    cnt = 0 
    for num in arr:
        if num == major:
            cnt+= 1
    if cnt > floor(n/2):
        return major
    else:
        return -1