from fake_market import Market
from portfolio import Portfolio

# loop for simulator
running = True

# Presets the portfolio to have a cash balance of 10,000 (can be easily adjusted)
NASDAQ = Market()
p = Portfolio([], 5000, NASDAQ)

# Constructor Class for the main menu and provides the trader different options on what to do with their portfolio and the market
class Simulator:

    def __init__(self):

        pass

    def __repr__(self):

        print("Menu:")
        print("1. Buy")
        print("2. Sell")
        print("3. Wait")
        print("4. Exit")
        option = int(input())

        # Method for buying a stock
        if (option == 1):

            print("Which stock would you like to buy?")
            NASDAQ.__repr__()
            stock_name = input()
            print("How many shares would you like to buy?")
            quantity = int(input())
            p.buy(stock_name, quantity)

        # Method for selling a stock
        elif (option == 2):

            print("Which stock would you like to sell?")
            stock_name = input()
            print("How many shares would you like to sell?")
            quantity = int(input())
            p.sell(stock_name, quantity)

        # Quit Method
        elif (option == 4):

            global running
            running = False

        # This method is technically the third option: Wait which updates the stocks with new prices if chosen
        else:

            pass

menu = Simulator()

if __name__ == "__main__":

    # Loop for the stock price updates, main menu, and trader's portfolio, so they are always informed of every movement
    while(running):

        NASDAQ.update()
        p.__repr__()
        menu.__repr__()
