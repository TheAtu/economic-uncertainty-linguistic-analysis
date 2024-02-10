import pandas as pd

def filter_dates_within_range(df, date_col, start_date, end_date):
    """
    Filter rows within a specified date range from a DataFrame.

    Args:
    - df (pandas.DataFrame): Input DataFrame containing the date column.
    - date_col (str): Input DataFrame column's name that contains the dates.
    - start_date (str): Start date of the range (inclusive), format: 'yyyy-mm-dd'.
    - end_date (str): End date of the range (inclusive), format: 'yyyy-mm-dd'.

    Returns:
    - pandas.DataFrame: DataFrame with rows filtered to keep only dates within the specified range.

    Example:
    >>> df = pd.DataFrame({'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']})
    >>> filtered_df = filter_dates_within_range(df, '2023-01-02', '2023-01-03')
    >>> print(filtered_df)
             date
    1  2023-01-02
    2  2023-01-03
    """

    filtered_rows = []
    
    for index, row in df.iterrows():
        if start_date <= row[date_col] <= end_date:
            filtered_rows.append(row)
    return pd.DataFrame(filtered_rows)

# Example usage
if __name__ == "__main__":
    df = pd.DataFrame({'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']})
    filtered_df = filter_dates_within_range(df, '2023-01-02', '2023-01-03')
    print(filtered_df)
