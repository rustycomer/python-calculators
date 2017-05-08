response = input("What is your account balance: ")


def calculate(account):
    for week in range(1, 53):
        account = account + (account * .03)
    return account


def tax(account):
    amount_kept = account * .6
    return amount_kept


def main(account):
    for year in range(1, 11):
        account = calculate(account)
        account = tax(account)
    print("At the end of Year " + str(year) + " you will have: $" + str(account))