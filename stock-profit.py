account_balance = input("What is your account balance: ")
stock_price = input("What is the current price of the stock: ")
# Calculate the amount allowed per trade based off of the account_balance
allowed_per_trade = account_balance / 4

# Calculate the amount of shares allowed to be traded with allowed_per_trade
allowed_shares = int(allowed_per_trade/stock_price)

# Calculate limit exit price at 3% above entry
limit_price = (stock_price * .03) + stock_price

# Calculate stop exit price at 1% below entry
target_stop = stock_price - (stock_price * .01)

# Calculate the amount of profit from the trade
possible_profit = (limit_price - stock_price) * allowed_shares

# Calculate the amount of the possible loss from the trade
possible_loss = (stock_price - target_stop ) * allowed_shares

print("Amount allowed per trade: $" + str(allowed_per_trade))
print("Shares allowed per trade: " + str(allowed_shares))
print("Projected Limit Exit Price: $" + str(limit_price))
print("Projected Stop Price: $" + str(target_stop))
print("Possible Profit: $" + str(possible_profit))
print("Possible Loss: $" + str(possible_loss))

