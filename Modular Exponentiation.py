def modularExponentiation(x, n, m):
	# Write your code here.
    if n == 0:
        return 1
    ans = modularExponentiation(x, n//2, m)
    if n%2 == 0:
        return (ans % m * ans % m)%m
    else:
        return (((ans % m * ans % m)%m )* x % m)%m

# Main.
t = int(input())
while (t > 0):
	lst = list(map(int,input().split()))
	x,n,m = lst[0], lst[1], lst[2]
	print(modularExponentiation(x, n, m))
	t -= 1