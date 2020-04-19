from typing import List

def getSMA(prices: List):
    sma = []


def getEMA(prices: List):
    """
        EMA: exponential moving average;
        start with the SMA build from there.
         sigma = 2/(periods + 1)
         EMA = price * sigma + (1-sigma) * EMA_previous
    :param prices: list of floats
    :return: list of floats representing the EMA
    """
    ema = []
    sigma: float = 2.0 / (len(prices) + 1.0)

    for x in range(len(prices)):
        if(x == len(prices) -1):
            ema.add(x)
        else:
            ema.add((sigma * prices[x]) + (1 + sigma) * ema[x+1])

    return ema
