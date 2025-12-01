def main():
    n1 = int(input())
    p1 = list(map(int, input().split()))
    n2 = int(input())
    p2 = list(map(int, input().split()))
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if p1[i - 1] == p2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    res = []
    x = n1
    y = n2
    while x > 0 and y > 0:
        if p1[x - 1] == p2[y - 1]:
            res.append(p1[x - 1])
            x -= 1
            y -= 1
        elif x > 0 and dp[x][y] == dp[x - 1][y]:
            x -= 1
        else:
            y -= 1

    print(*res[::-1])


if __name__ == '__main__':
    main()

