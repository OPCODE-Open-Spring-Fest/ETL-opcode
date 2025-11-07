import pandas as pd
import logging as lg
# TODO (Find & Fix)

logger = lg.getLogger(__name__)
logger.setLevel(lg.DEBUG)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform data by cleaning and standardizing it.

    Args:
        df: Input DataFrame

    Returns:
        Transformed DataFrame
    """
    if df.empty:
        # TODO (Find & Fix): Should raise a ValueError if DataFrame is empty
        pass

        # Create a copy to avoid modifying original
    df_transformed = df.copy()

    # TODO (Find & Fix): Use logging instead of print
    logger.info(f"🔄 Starting transformation of {len(df_transformed)} rows")

    # Handle duplicates
    initial_rows = len(df_transformed)
    # Removing duplicates
    df_transformed = df_transformed.drop_duplicates()

    duplicates_removed = initial_rows - len(df_transformed)
    if duplicates_removed > 0:
        # Number of duplicates removed
        logger.info(f"✅ Removed {duplicates_removed} duplicate rows.")

    # Handle null values in numeric columns
    numeric_columns = df_transformed.select_dtypes(include=['number']).columns
    for col in numeric_columns:
        # TODO (Find & Fix): Nulls in numeric columns are not handled
        pass

    # Handle null values in text columns
    text_columns = df_transformed.select_dtypes(include=['object']).columns
    for col in text_columns:
        # TODO (Find & Fix): Nulls in text columns are not handled
        pass

    # Standardize date columns (look for common date column names)
    date_columns = [col for col in df_transformed.columns
                    if any(keyword in col.lower() for keyword in ['date', 'time', 'created', 'updated'])]

    for col in date_columns:
        try:
            df_transformed[col] = pd.to_datetime(
                df_transformed[col], errors='coerce', infer_datetime_format=True)
            # Standardize all dates to 'YYYY-MM-DD HH:MM:SS'
            df_transformed[col] = df_transformed[col].dt.strftime(
                '%Y-%m-%d %H:%M:%S')

            logger.info(
                f"✅ Standardized date column '{col}' (e.g., {df_transformed[col].iloc[0]})")
        except Exception as e:
            logger.error(f"⚠️ Could not standardize column '{col}': {e}")

    # TODO (Find & Fix): Text columns are not cleaned (strip, lowercase)
    return df_transformed
