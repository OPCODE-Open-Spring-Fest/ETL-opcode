import pandas as pd
import sqlite3
import os
# TODO (Find & Fix)
from typing import Optional

def load(df: pd.DataFrame, db_path: str = "etl_data.db", table_name: str = "processed_data"):
    """
    Loads data into SQLite database with proper error handling and upsert logic.
    
    Args:
        df: DataFrame to load
        db_path: Path to SQLite database file
        table_name: Name of the table to create/update
    """
    if df.empty:
        print("⚠️ Warning: Empty DataFrame received, nothing to load")  # TODO (Find & Fix)
        return
    
    print(f"🔄 Loading {len(df)} rows into database '{db_path}'")  # TODO (Find & Fix)
    
    # Ensure directory exists
    db_dir = os.path.dirname(db_path)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir)
    
    conn = None
    try:
        # Connect to database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # TODO (Find & Fix): Table creation and schema logic missing
        
        # TODO (Find & Fix): Idempotency check missing (should avoid duplicate inserts)
        # TODO (Find & Fix): Bulk insert without checking for duplicates
        df.to_sql(table_name, conn, if_exists="append", index=False)
        conn.commit()
        
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
    except Exception as e:
        if conn:
            conn.rollback() 
    finally:
        if conn:
            conn.close()