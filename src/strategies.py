import numpy as np
import config

def calculate_rsi(prices, period = config.RSI_PERIOD):
    prices = prices[-period:]
    
    # Calculate price changes
    deltas = np.diff(prices)

    # Separate gains and losses
    gains = np.where(deltas >= 0, deltas, 0)
    losses = np.where(deltas < 0, -deltas, 0)

    # Calculate average gains and losses
    avg_gain = np.mean(gains)
    avg_loss = np.mean(losses)

    # Calculate relative strength (RS)
    rs = avg_gain / avg_loss

    # Calculate relative strength index (RSI)
    rsi = 100 - (100 / (1 + rs))

    return rsi