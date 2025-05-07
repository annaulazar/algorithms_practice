n = int(input())
nails = list(map(int, input().split()))
nails.sort()
dp = [0] * n
dp[0] = nails[1] - nails[0]
