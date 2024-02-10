from .filter_date import filter_dates_within_range
import pandas as pd

def standardize_data(df: pd.DataFrame, text_col: str = '', date_col: str = '', timeframe_start: str = '', timeframe_end: str = '') -> pd.DataFrame:
    """
    Standardize DataFrame by applying timeframe, removing extra columns, and renaming columns.

    Args:
    - df (pandas.DataFrame): Input DataFrame.
    - text_col (str): Name of the text column for filtering (optional).
    - date_col (str): Name of the date column for filtering (optional).
    - timeframe_start (str): Start date of the timeframe (inclusive), format: 'yyyy-mm-dd' (optional).
    - timeframe_end (str): End date of the timeframe (inclusive), format: 'yyyy-mm-dd' (optional).

    Returns:
    - pandas.DataFrame: Standardized DataFrame.

    Example:
    >>> df = pd.DataFrame({'Text': ['A', 'B', 'C'], 'Date': ['2023-01-01', '2023-01-02', '2023-01-03'], 'Value': [1, 2, 3]})
    >>> standardized_df = standardize_data(df, text_col='Text', date_col='Date', timeframe_start='2023-01-02', timeframe_end='2023-01-03')
    >>> print(standardized_df)
      text        date
    1    B  2023-01-02
    2    C  2023-01-03
    """
    # Apply timeframe if provided
    if date_col and timeframe_start and timeframe_end:
        df = filter_dates_within_range(df, date_col, timeframe_start, timeframe_end)

    # Remove extra columns if specified and rename columns
    if text_col and date_col:
        df = df[[text_col, date_col]]
        df = df.rename(columns={date_col: 'date', text_col: 'text'})

    return df

# Example usage
if __name__ == "__main__":
    df = pd.DataFrame({'Text': ['A', 'B', 'C'], 'Date': ['2023-01-01', '2023-01-02', '2023-01-03'], 'Value': [1, 2, 3]})
    standardized_df = standardize_data(df, text_col='Text', date_col='Date', timeframe_start='2023-01-02', timeframe_end='2023-01-03')
    print(standardized_df)
