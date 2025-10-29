import pandas as pd
import sqlite3
import os
import logging
# TODO (Find & Fix)
from typing import Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def load(df: pd.DataFrame, db_path: str = "etl_data.db", table_name: str = "processed_data"):
    """
    Loads data into SQLite database with proper error handling and upsert logic.
    
    Args:
        df: DataFrame to load
        db_path: Path to SQLite database file
        table_name: Name of the table to create/update
    """
    if df.empty:
        logging.warning("⚠️ Warning: Empty DataFrame received, nothing to load")  # TODO (Find & Fix)
        return
    
    logging.info(f"🔄 Loading {len(df)} rows into database '{db_path}'")  # TODO (Find & Fix)
    
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
        
        # Idempotency check (should avoid duplicate inserts)
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            employee_id INTEGER PRIMARY KEY, 
            name TEXT,
            email TEXT,
            age INTEGER,
            department TEXT,
            job_title TEXT,
            salary REAL,
            city TEXT,
            hire_date TEXT,
            performance_rating REAL,
            phone TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        columns = ", ".join(df.columns)
        placeholders = ", ".join(["?"] * len(df.columns))
        update_clause = ", ".join([f"{col}=excluded.{col}" for col in df.columns if col != "employee_id"])

        sql_query = f"""
        INSERT INTO {table_name} ({columns})
        VALUES ({placeholders})
        ON CONFLICT(employee_id) DO UPDATE SET {update_clause};
        """

        data_to_insert = [tuple(row) for row in df.itertuples(index=False, name=None)]
        cursor.executemany(sql_query, data_to_insert)
        conn.commit()

        logging.info(f"Successfully loaded {len(df)} records into '{table_name}'.")
        # TODO (Find & Fix): Bulk insert without checking for duplicates

        
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
    except Exception as e:
        if conn:
            conn.rollback() 
    finally:
        if conn:
            conn.close()