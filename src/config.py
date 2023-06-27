import ccxt
import os

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

# Currencies
TICKERS = [
    'BTC-USD',    # Bitcoin
    'ETH-USD',    # Etherium
    'SOL-USD',    # Solana
    'ADA-USD',    # Cardano
    'DOGE-USD',   # Dogecoin
    'TRX-USD',    # Tron
    'LTC-USD',    # Litecoin
    'DOT-USD',    # Polkadot
    'MATIC-USD',  # Polygon
    'AVAX-USD',   # Avalanche
    'SHIB-USD',   # Shiba Inu
    'LINK-USD',   # Chainlink
    'ATOM-USD',   # Cosmos
    'UNI-USD'     # Uniswap
]