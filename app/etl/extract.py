import pandas as pd
import os

# Get the base directory (app/) relative to this file (app/etl/extract.py)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DATA_PATH = os.path.join(BASE_DIR, "data.csv")

def extract(path: str = DEFAULT_DATA_PATH) -> pd.DataFrame :
    """
    Extracts data from CSV, Excel, or JSON file.
    
    Args:
        path: Path to the data file (supports .csv, .xlsx, .json)
        
    Returns:
        pd.DataFrame: DataFrame containing the extracted data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file is empty or invalid
    """
    # Validate file path
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ File not found: {path}")
    
    # Get file extension
    ext = os.path.splitext(path)[-1].lower()
    
    # Check if file format is supported
    if ext not in ['.csv', '.xlsx', '.xls', '.json']:
        raise ValueError(f"Unsupported file format: {ext}")
    
    try:
        if ext == '.csv':
            # Try different encodings for CSV files
            encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
            df = None
            
            for encoding in encodings:
                try:
                    df = pd.read_csv(path, encoding=encoding)
                    print(f"Successfully read CSV with encoding: {encoding}")
                    break
                except UnicodeDecodeError:
                    print(f"Failed to read with encoding '{encoding}'")
                    continue
                except Exception as e:
                    print(f"Error reading with encoding '{encoding}': {e}")
                    continue
            
            if df is None:
                raise ValueError(f"Could not read CSV with tried encodings: {encodings}")
                
        elif ext in ['.xls', '.xlsx']:
            df = pd.read_excel(path)
            print(f"Successfully read Excel file: {path}")
            
        elif ext == '.json':
            df = pd.read_json(path)
            print(f"Successfully read JSON file: {path}")
        
        # Validate data
        if df.empty:
            raise ValueError("File contains no data")
        
        print(f"✅ Extracted {len(df)} rows and {len(df.columns)} columns")  # TODO: Use logging instead of print
        return df
        
    except pd.errors.EmptyDataError:
        raise ValueError("❌ File contains no data")
    except pd.errors.ParserError as e:
        raise ValueError(f"❌ Error parsing file: {e}")
    except Exception as e:
        raise ValueError(f"❌ Unexpected error reading file: {e}")
