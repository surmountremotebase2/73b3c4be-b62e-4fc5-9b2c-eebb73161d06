from surmount.base_class import Strategy, TargetAllocation

class TradingStrategy(Strategy):
    def __init__(self):
        # Define the tickers of interest - Apple and Microsoft
        self.tickers = ["AAPL", "MSFT"]

    @property
    def interval(self):
        # Define the trading interval (e.g., daily)
        return "1day"

    @property
    def assets(self):
        # Return the list of assets this strategy is interested in
        return self.tickers

    @property
    def data(self):
        # Define the data required for the strategy
        # In this simple example, no additional data is required
        return []

    def run(self, data):
        # Define the trading logic
        # In this case, evenly allocate between AAPL and MSFT

        # Create an allocation dictionary with each asset allocated 50%
        allocation_dict = {ticker: 0.5 for ticker in self.tickers}

        # Return the target allocation
        return TargetAllocation(allocation_dict)