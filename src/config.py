import ccxt
import os

# Currencies
TICKERS = [
    'BTC-USD',
    'ETH-USD',
    'SOL-USD',
]

# Exchange
EXCHANGE = ccxt.coinbasepro({
    'apiKey': os.environ['COINBASE_PRO_API_KEY'],
    'secret': os.environ['COINBASE_PRO_SECRET'],
})

# Max # of requests / second
API_RATE_LIMIT = 10.0
MIN_REQUEST_WAIT = API_RATE_LIMIT / 60.0

# RSI Calculations
RSI_PERIOD = 14