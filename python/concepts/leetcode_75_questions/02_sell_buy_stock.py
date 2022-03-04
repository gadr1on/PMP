# buy low sell high 
# gadrion - 03/04/2022

def maxProfit(prices):
    l, r = 0, 1 # left=buy, right=sell
    maxP = 0

    while r < len(prices):
        # profitable ?
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            if profit > maxP:
                maxP = profit
        else:
            l = r
        r += 1
    return maxP


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))
