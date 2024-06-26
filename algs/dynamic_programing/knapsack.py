memo = {}

# runtime: O(nW)
# based on the size of the memo table


def knapsack(i, W):
    if (i, W) in memo:
        return memo[(i, W)]

    sol = 0
    if i == 0 or W == 0:
        sol = 0
    elif weights[i] > W:
        sol = knapsack(i - 1, W)
    else:
        sol = max(values[i] + knapsack(i - 1, W -
                  weights[i]), knapsack(i-1, W))

    memo[(i, W)] = sol
    return sol


weights = [0, 1, 2, 3]
values = [0, 6, 10, 12]
n = len(weights)
W = 5

# Calling the function
max_value = knapsack(n - 1, W)
print("Maximum value:", max_value)


def backtrack(i, W):
    if i == 0 or W == 0:
        return []
    elif memo[(i, W)] == memo[(i-1, W)]:
        return backtrack(i - 1, W)
    else:
        return [i] + backtrack(i-1, W-weights[i])


print(backtrack(n-1, W))
