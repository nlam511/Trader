from typing import TypeVar, List
PandasDataFrame = TypeVar('pd.core.frame.DataFrame')
import pandas as pd



def get_sma(periods : int, price_data: PandasDataFrame):
    """
        SMA: simple moving average
        =Sum(price,period)/ periods
    :param price_data:
    """
    price_data.drop(price_data.columns[1], axis=1, inplace = True)
    price_data['SMA'] = price_data.rolling(window=periods).mean()
    return price_data

#
# int getSMA(int length, int arrayLength, double & prices[], double & returnArray[])
# {
#     int smaLength = arrayLength - length;
# ArrayResize(returnArray, smaLength);
#
# for (int x = 0; x < smaLength; x++)
# {
#     returnArray[x] = 0.0;
# for (int y = x; y < x + length; y++)
# {
#     returnArray[x] += prices[y];
# }
# returnArray[x] /= length;
# }
# return smaLength;
# }

def get_ema(prices: List):
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
