# Constructor Class that creates and maintains the trader's portfolio
class Portfolio:

    def __init__(self, holdings, cash, market):

        self.holdings = holdings
        self.cash = cash
        self.market = market

    # Method to buy a stock if they have the necessary funds
    def buy(self, stock_name, quantity):

        stock = self.market.pick_stock(stock_name)

        if (stock):

            total_cost = stock.price * quantity

            if (0 < total_cost <= self.cash):

                self.cash -= total_cost
                self.holdings.append((stock_name, quantity))
                return True
        print("Sorry, it also seems that you lack the necessary funds to complete this order.")
        print("Please acquire more funds for this order to proceed.")
        return False

    # Method to sell a stock if they have any shares of that stock
    def sell(self, stock_name, quantity):

        for x in enumerate(self.holdings):

            index = x[0]
            holding = x[1]

            if stock_name in holding:

                new_quantity = holding[1] - quantity
                total_cost = self.market.pick_stock(stock_name).price * quantity

                if new_quantity >= 0:

                    if (new_quantity == 0):

                        self.holdings.pop(index)

                    else:

                        self.holdings[index] = (stock_name, new_quantity)

                    self.cash += total_cost
                    return True
        print("Sorry, this order is not possible as you either do not own any shares of this stock or inputted the wrong amount.")
        return False

    # Method that shows all the basic info about a trader's portfolio
    def __repr__(self):

        market_balance = 0
        print("Your Portfolio")
        print("--------------")
        print("Your holdings:")

        for stock in self.holdings:

            stock_name = stock[0]
            quantity = stock[1]
            price = self.market.pick_stock(stock_name).price
            market_balance += price * quantity

            if quantity == 1:

                print(quantity, "share of", stock_name, "at", price)

            else:

                print(quantity, "shares of", stock_name, "at", price)

        print()
        print("Your portfolio's balance:", market_balance)
        print()
        print("Your uninvested cash balance:", self.cash)
        print("--------------")
        print()
