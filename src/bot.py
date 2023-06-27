import config
import data_manager
import strategies
import time
import numpy as np
import curses
from terminal_view import print_rsi_table

def main(stdscr):
    stdscr.nodelay(True)

    while True:
        tickers = []
        rsis = []

        for ticker in config.TICKERS:
            # Fetch historical price data
            historical_data = data_manager.get_past_30_days(ticker)
            
            if historical_data == None:
                continue

            # Extract closing prices from the fetched data
            closing_prices = np.array([data[4] for data in historical_data])
            
            # Calculate RSI
            rsi = strategies.calculate_rsi(closing_prices)
            
            # Append ticker and rounded RSI to the lists
            tickers.append(ticker)
            rsis.append(rsi)

            time.sleep(config.MIN_REQUEST_WAIT)
        
        # Print the RSI table
        print_rsi_table(stdscr, tickers, rsis)

curses.wrapper(main)