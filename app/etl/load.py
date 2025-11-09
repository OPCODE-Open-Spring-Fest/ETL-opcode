import pandas as pd
import sqlite3
import os
import logging  as lg 
# TODO (Find & Fix)
logger=lg.getLogger(__name__)
logger.setLevel(lg.DEBUG)


def load(df: pd.DataFrame, db_path: str = "etl_data.db", table_name: str = "processed_data"):
    """
    Loads data into SQLite database with proper error handling and upsert logic.
    
    Args:
        df: DataFrame to load
        db_path: Path to SQLite database file
        table_name: Name of the table to create/update
    """
    if df.empty:
        logger.warning("⚠️ Warning: Empty DataFrame received, nothing to load")  # TODO (Find & Fix)
        return
    
    logger.info(f"🔄 Loading {len(df)} rows into database '{db_path}'")  # TODO (Find & Fix)
    
    # Ensure directory exists
    db_dir = os.path.dirname(db_path)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir) 
    conn = None
    cursor = None
    try:
        # Connect to database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # TODO (Find & Fix): Table creation and schema logic missing
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            employee_id TEXT PRIMARY KEY, 
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

        placeholders = ", ".join(["?"] * len(df.columns))
        column_names = ", ".join(df.columns)
        sql_query = f"INSERT OR REPLACE INTO {table_name} ({column_names}) VALUES ({placeholders})"  
        cursor.executemany(sql_query, df.itertuples(index=False, name=None))
        conn.commit()
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
    except Exception as e:
        if conn:
            conn.rollback() 
    finally:
        # Ensure cursor is closed
        if cursor:
            cursor.close()
        # Ensure database connection is properly closed
        if conn:
            conn.close()
