import utils
import pandas as pd
from test_data import test_data
from typing import TypeVar, List
PandasDataFrame = TypeVar('pd.core.frame.DataFrame')

def main():
    initial_data = utils.def_list_to_pandas(test_data)
    olhc4= olhc_average(initial_data, 4)
    print(olhc4)


def olhc_average(df: PandasDataFrame, value: float):
    time = pd.to_datetime(df['datetime'], unit="ms")
    sum = (df.open + df.close + df.high + df.low) / value
    return pd.DataFrame({'datetime': time, 'sum': sum}, columns=['datetime', 'sum'])



if __name__ == "__main__":
    main()