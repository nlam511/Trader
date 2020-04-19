import utils
import pandas as pd
from test_data import test_data
from typing import TypeVar, List
PandasDataFrame = TypeVar('pd.core.frame.DataFrame')

def main():
    df = utils.def_list_to_pandas(test_data)
    sum = olhc_average(df, 4)
    print('done')


def olhc_average(df: PandasDataFrame, value: float):
    sum = df.open + df.close + df.high + df.low
    sum_div = sum / value
    return sum








if __name__ == "__main__":
    main()