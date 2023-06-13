import config
import curses
import strategies
from tabulate import tabulate
import time
import numpy as np

# import datetime
# for data in historical_data:
#     timestamp = data[0]
#     open = data[1]
#     high = data[2]
#     low = data[3]
#     close = data[4]
#     volume = data[5]
    
#     printable_time = datetime.datetime.fromtimestamp(timestamp / 1000)
#     print(f"Timestamp: {printable_time}")
#     print(f"Open: {open}")
#     print(f"High: {high}")
#     print(f"Low: {low}")
#     print(f"Close: {close}")
#     print(f"Volume: {volume}")
#     print("-----------------------\n")


def print_rsi_table(stdscr, tickers, rsis):
    stdscr.clear()
    
    table_data = []
    for ticker, rsi in zip(tickers, rsis):
        table_data.append([ticker, rsi])
    
    table_headers = ["Ticker", "RSI"]
    table = tabulate(table_data, headers=table_headers, tablefmt="grid")
    
    stdscr.addstr(table)
    stdscr.refresh()

def main(stdscr):
    stdscr.nodelay(True)  # Set non-blocking mode for keyboard input
    
    while True:
        tickers = []
        rsis = []

        end_timestamp = int(time.time())  # Current timestamp
        start_timestamp = end_timestamp - (30 * 24 * 60 * 60)  # 30 days ago
        timeframe = '1d'
        
        for ticker in config.TICKERS:
            # Fetch historical price data
            historical_data = config.EXCHANGE.fetch_ohlcv(
                ticker, 
                timeframe, 
                start_timestamp * 1000, 
                end_timestamp * 1000
            )
            
            # Extract closing prices from the fetched data
            closing_prices = np.array([data[4] for data in historical_data])
            
            # Calculate RSI
            rsi = strategies.calculate_rsi(closing_prices)
            
            # Round the RSI value to 3 decimal places
            rsi_rounded = round(rsi, 3)
            
            # Append ticker and rounded RSI to the lists
            tickers.append(ticker)
            rsis.append(rsi_rounded)
        
        # Print the RSI table
        print_rsi_table(stdscr, tickers, rsis)
        
        # Check for keyboard input
        key = stdscr.getch()
        if key == ord('q'):  # Quit if 'q' is pressed
            break
        
        time.sleep(config.MIN_REQUEST_WAIT)

curses.wrapper(main)