import logging
from app.etl.extract import extract
from app.etl.transform import transform
from app.etl.load import load

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def run_pipeline(csv_path: str = "data.csv", db_path: str = "etl_data.db"):
    """
    Run the complete ETL pipeline.
    
    Args:
        csv_path: Path to the input CSV file
        db_path: Path to the output SQLite database
    """
    try:
        logging.info("🚀 Starting ETL Pipeline")  # TODO (Find & Fix): Use logging instead of logging.info
        logging.info(f"📁 Input file: {csv_path}")
        logging.info(f"🗄️ Output database: {db_path}")
        logging.info("-" * 50)
        
        # Extract
        logging.info("📥 STEP 1: EXTRACT")
        df = extract(csv_path)
        logging.info(f"✅ Extracted {len(df)} rows")
        logging.info(f"📊 Columns: {list(df.columns)}")
        logging.info("-" * 50)

        
        # Transform
        logging.info("🔄 STEP 2: TRANSFORM")
        df_transformed = transform(df)
        logging.info(f"✅ Transformed data ready")
        logging.info("-" * 50)

        
        # Load
        logging.info("📤 STEP 3: LOAD")
        load(df_transformed, db_path)
        logging.info("-" * 50)

        
        logging.info("🎉 ETL Pipeline completed successfully!")
        logging.info(f"📈 Final dataset: {len(df_transformed)} rows, {len(df_transformed.columns)} columns")
        
    except FileNotFoundError as e:
        logging.error(f"❌ File Error: {e}")

    except ValueError as e:
        logging.error(f"⚠️ Value Error: {e}")
        raise
        # TODO (Find & Fix): Error handling missing
        
    except Exception as e:
        # TODO (Find & Fix): Error handling missing
        logging.exception(f"🔥 Unexpected error: {e}")

if __name__ == "__main__":    
    # Run the pipeline
    run_pipeline()