import config
import time

def get_past_30_days(ticker):
    today = int(time.time())  # Current timestamp
    thirty_days_ago = today - (30 * 24 * 60 * 60)  # 30 days ago
    timeframe = '1d'

    try:
        return config.EXCHANGE.fetch_ohlcv(
            ticker, 
            timeframe, 
            thirty_days_ago * 1000, 
            today * 1000
        )
    except:
        pass

    return None