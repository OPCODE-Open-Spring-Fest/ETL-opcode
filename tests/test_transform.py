import pytest
import numpy as np
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from app.etl.transform import (
    _remove_duplicates,
    _handle_nulls,
    _standardize_dates,
    _validate_types
)

def test_remove_duplicates():
    data = {'id': [1, 1, 2], 'name': ['a', 'a', 'b']}
    input_df = pd.DataFrame(data)
    expected_data = {'id': [1, 2], 'name': ['a', 'b']}
    expected_df = pd.DataFrame(expected_data).reset_index(drop=True)
    result_df = _remove_duplicates(input_df).reset_index(drop=True)
    assert len(result_df) == 2
    assert_frame_equal(result_df, expected_df)

def test_handle_nulls_does_nothing():
    data = {'numeric': [1, np.nan], 'text': ['a', np.nan]}
    input_df = pd.DataFrame(data)
    expected_df = input_df.copy()
    result_df = _handle_nulls(input_df)
    assert_frame_equal(result_df, expected_df)

def test_standardize_dates():
        data = {'report_date': ['2023-01-01 12:00:00', '02/25/2022', 'bad-date']}
        df = pd.DataFrame(data)

        result_df = _standardize_dates(df)

        expected = [
            '2023-01-01 12:00:00',
            '2022-02-25 00:00:00',
            np.nan
        ]
        assert result_df['report_date'].tolist() == expected

def test_validate_types_does_nothing():
    """
    Tests that _validate_types currently does nothing
    (as per the 'pass' in the logic).
    """
    data = {'name': [' Alice ', ' Bob ']}
    input_df = pd.DataFrame(data)
    expected_df = input_df.copy()
    
    result_df = _validate_types(input_df)
    assert_frame_equal(result_df, expected_df)