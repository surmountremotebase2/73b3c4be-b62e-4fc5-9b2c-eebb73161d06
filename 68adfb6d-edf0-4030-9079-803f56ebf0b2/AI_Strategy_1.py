from surmount.base_class import Strategy, TargetAllocation
# Assuming that the surmount.base_class is the correct import path for Strategy and TargetAllocation
# This is a simple static allocation strategy for AAPL and MSFT

class TradingStrategy(Strategy):
    def __init__(self):
        # Define the tickers for AAPL and MSFT
        self.tickers = ["AAPL", "MSFT"]

    @property
    def assets(self):
        # Return the list of assets this strategy will trade, AAPL and MSFT
        return self.tickers

    @property
    def interval(self):
        # Define the interval for data fetching, can be adjusted as needed
        return "1day"

    @property
    def data(self):
        # In this simple strategy, we don't need any extra data
        return []

    def run(self, data):
        # Allocate 50% to AAPL and 50% to MSFT irrespective of the data
        allocation_dict = {"AAPL": 0.5, "MSFT": 0.5}
        
        # Return the target allocation
        return TargetAllocation(allocation_dict)