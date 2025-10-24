import pandas as pd
import os
# TODO (Find & Fix)
from typing import Optional

def extract(path: str = "xyz.csv") -> pd.DataFrame:
    """
    Extracts data from CSV, Excel, or JSON file.
    
    Args:
        path: Path to the data file (supports .csv, .xlsx, .json)
        
    Returns:
        pd.DataFrame: DataFrame containing the extracted data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file format is unsupported or file is empty/invalid
    """
    # Validate file path
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ File not found: {path}")
    
    # Get file extension
    file_ext = os.path.splitext(path)[-1].lower()
    
    # Check if file format is supported
    supported_formats = ['.csv', '.xlsx', '.xls', '.json']
    if file_ext not in supported_formats:
        raise ValueError(f"❌ Unsupported file format: {file_ext}. Supported formats: {supported_formats}")
    
    try:
        df = None
        
        if file_ext == '.csv':
            # Try different encodings for CSV files
            encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
            
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
                raise ValueError(f"Could not read CSV with tried encodings: {encodings}")
                
        elif file_ext in ['.xlsx', '.xls']:
            # Read Excel files
            try:
                df = pd.read_excel(path)
                print(f"Successfully read Excel file: {path}")
            except Exception as e:
                raise ValueError(f"❌ Error reading Excel file: {e}")
                
        elif file_ext == '.json':
            # Read JSON files
            try:
                df = pd.read_json(path)
                print(f"Successfully read JSON file: {path}")
            except Exception as e:
                raise ValueError(f"❌ Error reading JSON file: {e}")
        
        # Validate data
        if df is None:
            raise ValueError("❌ Failed to read data from file")
        
        if df.empty:
            raise ValueError(" File contains no data")
        
        print(f"✅ Extracted {len(df)} rows and {len(df.columns)} columns")  # TODO: Use logging instead of print
        return df
        
    except pd.errors.EmptyDataError:
        raise ValueError("❌ File contains no data")
    except pd.errors.ParserError as e:
        raise ValueError(f"❌ Error parsing file: {e}")
    except Exception as e:
        raise ValueError(f"❌ Unexpected error reading file: {e}")