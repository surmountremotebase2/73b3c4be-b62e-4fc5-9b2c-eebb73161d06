from surmount.base_class import Strategy, TargetAllocation
from surmount.data import Asset

class TradingStrategy(Strategy):
    def __init__(self):
        # Define the tickers for Apple and Microsoft
        self.tickers = ["AAPL", "MSFT"]

    @property
    def assets(self):
        # Return the list of tickers this strategy will handle
        return self.tickers

    @property
    def interval(self):
        # Define the interval for which the strategy will be applied. 
        # This is not used in this simple allocation but required by the framework.
        return "2day"

    def run(self, data):
        # Define an equal allocation dictionary for Apple and Microsoft
        # Since it's a 50-50 distribution between the two, each gets a 0.5 allocation
        allocation_dict = {ticker: 0.5 for ticker in self.tickers}

        # Return the target allocation object with the specified allocations
        return TargetAllocation(allocation_dict)