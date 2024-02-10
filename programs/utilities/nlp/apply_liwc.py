from ..python.check_package_availability import check_package_availability
from .spanish_liwc import *

PACKAGES_REQUIERED = ['re','pandas']

def apply_normalize_liwc(df, text_col_name='text', date_col_name='date'):
    '''
    Apply LIWC (Linguistic Inquiry and Word Count) normalization to a DataFrame.

    Args:
        df (pandas.DataFrame): Input DataFrame.
        text_col_name (str): Name of the text column in the DataFrame (default is 'text').

    Returns:
        pandas.DataFrame: DataFrame with LIWC normalized features.

    Example:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'text': ['The quick brown fox', 'jumps over the lazy dog.']})
        >>> normalized_df = apply_normalize_liwc(df, text_col_name='text')
        >>> print(normalized_df)
           Analytic  Authentic  ...  WC  WPS
        0       0.0        0.0  ...   4  4.0
        1       0.0        0.0  ...   5  5.0

    Raises:
        ImportError: If required packages are not available.
    '''
    # Check and Install if required packages are available
    check_package_availability(PACKAGES_REQUIERED)
    import pandas as pd
    import re

    # Initialize LIWC_ALL list
    LIWC_ALL = []

     # Get LIWC dummy count and extract headers
    LIWC_dummy = liwc().getLIWCCount('')
    HEADERS = list(LIWC_dummy.keys())
    HEADERS.sort()

    # Initialize liwc_vector list with headers
    liwc_vector = ['date']
    for head in HEADERS:
        liwc_vector.append(head)
    # Append liwc_vector to LIWC_ALL list
    LIWC_ALL.append(liwc_vector)
    
    # Initialize data_list
    data_list = []

    # Iterate over DataFrame rows
    for index, row in df.iterrows():
        # Preprocess text
        text = row[text_col_name].lower().replace('\n', ' ')
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r' +', ' ', text)

        # Get LIWC counts for preprocessed text
        LIWC_raw = liwc().getLIWCCount(text)

        # Normalize LIWC counts
        LIWC_norm = {}
        for item in LIWC_raw:
            if item != 'WC':
                LIWC_norm[item] = LIWC_raw[item] / LIWC_raw['WC']
            else:
                LIWC_norm['WC'] = LIWC_raw['WC']

        # Initialize liwc_vector for each row
        liwc_vector = {}
        for head in HEADERS:
            liwc_vector[head] = LIWC_norm[head]

        # Add date to the liwc_vector
        liwc_vector[date_col_name] = row[date_col_name]
        
        # Append liwc_vector to data_list
        data_list.append(liwc_vector)

    # Create a DataFrame from the list of dictionaries
    liwc_df = pd.DataFrame(data_list)

    return liwc_df