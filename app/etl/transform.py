import pandas as pd
import logging as lg
# TODO (Find & Fix)

def _remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Handles duplicate removal."""
    initial_rows = len(df)
    df = df.drop_duplicates()
    duplicates_removed = initial_rows - len(df)
    if duplicates_removed > 0:
        print(f"✅ Removed {duplicates_removed} duplicate rows.")
    return df

def _handle_nulls(df: pd.DataFrame) -> pd.DataFrame:
    """Handles null values (currently a placeholder)."""
    numeric_columns = df.select_dtypes(include=['number']).columns
    for col in numeric_columns:
        # TODO (Find & Fix): Nulls in numeric columns are not handled
        pass
        text_columns = df.select_dtypes(include=['object']).columns
    for col in text_columns:
        # TODO (Find & Fix): Nulls in text columns are not handled
        pass
    return df

def _standardize_dates(df: pd.DataFrame) -> pd.DataFrame:
    """Handles date standardization."""
    date_columns = [col for col in df.columns 
                      if any(keyword in col.lower() for keyword in ['date', 'time', 'created', 'updated'])]
    for col in date_columns:
        try:
            df[col] = pd.to_datetime(df[col], errors='coerce', format='mixed')
            # Standardize all dates to 'YYYY-MM-DD HH:MM:SS'
            df[col] = df[col].dt.strftime('%Y-%m-%d %H:%M:%S')
            
            print(f"✅ Standardized date column '{col}' (e.g., {df[col].iloc[0]})")
        except Exception as e:
            print(f"⚠️ Could not standardize column '{col}': {e}")
    return df

def _validate_types(df: pd.DataFrame) -> pd.DataFrame:
    # TODO (Find & Fix): Text columns are not cleaned (strip, lowercase)
    pass
    return df
def transform(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        # TODO (Find &Fix): Should raise a ValueError if DataFrame is empty
        pass
    
    df_transformed = df.copy()
    
    print(f"🔄 Starting transformation of {len(df_transformed)} rows")  # TODO (Find & Fix): Use logging instead of print
    df_transformed = _remove_duplicates(df_transformed)
    df_transformed = _handle_nulls(df_transformed)
    df_transformed = _standardize_dates(df_transformed)
    df_transformed = _validate_types(df_transformed)
    
    return df_transformed