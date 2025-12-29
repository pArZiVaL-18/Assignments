def min_cost_path(cost, m, n):
    rows = len(cost)
    cols = len(cost[0])

    dp = [[0] * cols for _ in range(rows)]
    parent = [[None] * cols for _ in range(rows)]

    dp[0][0] = cost[0][0]
    parent[0][0] = None

    # First row
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + cost[0][j]
        parent[0][j] = (0, j - 1)

    # First column
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + cost[i][0]
        parent[i][0] = (i - 1, 0)

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            choices = [
                (dp[i - 1][j], (i - 1, j)),      # top
                (dp[i][j - 1], (i, j - 1)),      # left
                (dp[i - 1][j - 1], (i - 1, j - 1))  # diagonal
            ]

            min_cost, prev = min(choices, key=lambda x: x[0])
            dp[i][j] = cost[i][j] + min_cost
            parent[i][j] = prev

    # Backtrack to get path
    path = []
    i, j = m, n
    while (i, j) is not None:
        path.append((i, j))
        if parent[i][j] is None:
            break
        i, j = parent[i][j]

    path.reverse()

    return dp[m][n], path


cost = [[1, 2, 3],
        [4, 8, 2]]

m = 1
n = 2

min_cost, path = min_cost_path(cost, m, n)
print("Minimum cost:", min_cost)
print("Path:", path)
