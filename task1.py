
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result


def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    track = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                track[i] = coin

    result = {}
    while amount > 0:
        coin = track[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


print(find_coins_greedy(113))
print(find_min_coins(113))
