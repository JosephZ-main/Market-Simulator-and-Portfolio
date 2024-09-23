import random
from stocks import Stocks

# Constructor Class that sets up the market and the database of stocks that are available to buy/sell
class Market:

    def __init__(self):

        # Database of Stocks (can be easily adjusted to one's preference)
        self.stocks = [
            Stocks("TSLA", 168.69),
            Stocks("GOOGL", 94),
            Stocks("AAPL", 145),
            Stocks("META", 115),
            Stocks("IBM", 149),
            Stocks("AMZN", 91),
            Stocks("COKE", 538),
            Stocks("BAC", 33),
        ]

    # Method to pick one of the stocks that's in the list otherwise
    def pick_stock(self, stock_name):

        for stock in self.stocks:

            if stock.name == stock_name:

                return stock
        print("Sorry, this stock is unavailable. Please pick a stock that's currently on the list.")
        return False

    # Method that updates the stock prices consistently to simulate the randomness of a market
    def update(self):

        for x in enumerate(self.stocks):

            index = x[0]
            stock = x[1]
            stock_name = stock.name
            original_price = stock.price
            new_price = round((original_price * (random.normalvariate(1.07, 0.14))), 2)
            self.stocks[index] = Stocks(stock_name, new_price)

    def __repr__(self):

        for stock in self.stocks:

            print(stock.name, stock.price)
