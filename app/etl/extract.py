import pandas as pd
import os
# TODO (Find & Fix)
from typing import Optional

def extract(path: str = "xyz.csv") -> pd.DataFrame :
    """
    Extracts data from CSV file.
    
    Args:
        path: Path to the CSV file
        
    Returns:
        DataFrame containing the extracted data  # TODO (Find & Fix): Should specify pd.DataFrame in docstring
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file is empty or invalid
    """
    # Validate file path
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ File not found: {path}")
    
    if not path.lower().endswith('.csv'):  # TODO (Find & Fix)
        raise ValueError(f"❌ File must be a CSV: {path}")
    
    try:
        # Try different encodings
        encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
        df = None
        
        for encoding in encodings:
            try:
                df = pd.read_csv(path, encoding=encoding)
                print(f"Successfully read CSV with encoding: {encoding}")
                break
            except UnicodeDecodeError:
                print(f"Failed to read with encoding '{encoding}'")  # Log the encoding that failed
                continue
            except Exception as e:
                print(f"Error reading with encoding '{encoding}': {e}")
                continue
        
        if df is None:
            raise ValueError(f" Could not read CSV with tried encodings: {encodings}")
        
        # Validate data
        if df.empty:
            raise ValueError("File contains no data")
        
        print(f"✅ Extracted {len(df)} rows and {len(df.columns)} columns")  # TODO: Use logging instead of print
        return df
        
    except pd.errors.EmptyDataError:
        raise ValueError("❌ File contains no data")
    except pd.errors.ParserError as e:
        raise ValueError(f"❌ Error parsing CSV: {e}")
    except Exception as e:
        raise ValueError(f"❌ Unexpected error reading file: {e}")