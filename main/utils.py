from typing import List
import pandas as pd


def def_list_to_pandas(data: List, drop_columns: List = []):
    """
    Function to convert a list of dictionaries into a pandas data frame

    Parameters:
        data (List): data represented as a list of dictionaries
        drop_columns (List): Columns to drop, default=None

    Return:
        data formatted in a pandas data frame
    """
    df = pd.DataFrame(data)
    return df.drop(drop_columns, axis=1)
