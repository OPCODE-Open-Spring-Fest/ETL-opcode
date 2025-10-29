import pandas as pd
import logging
from datetime import datetime
# TODO (Find & Fix)
from typing import Optional


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform data by cleaning and standardizing it.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Transformed DataFrame
    """
    if df.empty:
        raise ValueError("DataFrame is Empty.")
        # TODO (Find & Fix): Should raise a ValueError if DataFrame is empty
        
    
    # Create a copy to avoid modifying original
    df_transformed = df.copy()
    
    logger.info(f"🔄 Starting transformation of {len(df_transformed)} rows")  # TODO (Find & Fix): Use logging instead of print
    
    # Handle duplicates
    initial_rows = len(df_transformed)
    df_transformed.drop_duplicates(inplace=True)# TODO (Find & Fix): Duplicates are not removed
    duplicates_removed = initial_rows - len(df_transformed)
    if duplicates_removed > 0:
        logger.info(f"Removed {duplicates_removed} duplicate rows.")
        # TODO (Find & Fix): Should log how many duplicates were removed
        pass
    
    # Handle null values in numeric columns
    numeric_columns = df_transformed.select_dtypes(include=['number']).columns
    for col in numeric_columns:
        if df_transformed[col].isnull().any():
            mean_value = df_transformed[col].mean()
            df_transformed[col].fillna(mean_value, inplace=True)
        # TODO (Find & Fix): Nulls in numeric columns are not handled
        pass
    
    # Handle null values in text columns
    text_columns = df_transformed.select_dtypes(include=['object']).columns
    for col in text_columns:
        if df_transformed[col].isnull().any():
            df_transformed[col].fillna("Unknown", inplace=True)
        # TODO (Find & Fix): Nulls in text columns are not handled
        pass
    
    # Standardize date columns (look for common date column names)
    date_columns = [col for col in df_transformed.columns 
                   if any(keyword in col.lower() for keyword in ['date', 'time', 'created', 'updated'])]
    
    for col in date_columns:
        df_transformed[col] = pd.to_datetime(df_transformed[col], errors='coerce')
        if df_transformed[col].isnull().any():
            median_date = df_transformed[col].median()
            df_transformed[col].fillna(median_date, inplace=True)# TODO (Find & Fix): Date columns are not standardized
        
    for col in text_columns:
        df_transformed[col] = df_transformed[col].astype(str).str.strip().str.lower()
    
    logger.info("Transformation completed successfully.")
    
    # TODO (Find & Fix): Text columns are not cleaned (strip, lowercase)
    return df_transformed