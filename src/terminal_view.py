from tabulate import tabulate

def print_rsi_table(stdscr, tickers, rsis):
    stdscr.clear()
    
    table_data = []
    for ticker, rsi in zip(tickers, rsis):
        table_data.append([ticker, rsi])
    
    table_headers = ["Ticker", "RSI"]
    table = tabulate(table_data, headers=table_headers, tablefmt="grid")
    
    stdscr.addstr(table)
    stdscr.refresh()