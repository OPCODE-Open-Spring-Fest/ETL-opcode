import os
from app.etl.extract import extract
from app.etl.transform import transform
from app.etl.load import load
import logging as lg
lg.basicConfig(level=lg.debug())

logger = lg.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "data.csv")

def run_pipeline(csv_path: str =data_path, db_path: str = "etl_data.db"):
    """
    Run the complete ETL pipeline.
    
    Args:
        csv_path: Path to the input CSV file
        db_path: Path to the output SQLite database
    """
    try:
        lg.info("🚀 Starting ETL Pipeline")  # TODO (Find & Fix): Use logging instead of print
        lg.info(f"📁 Input file: {csv_path}")
        lg.info(f"🗄️ Output database: {db_path}")
        lg.info("-" * 50)
        
        # Extract
        lg.info("📥 STEP 1: EXTRACT")
        df = extract(csv_path)
        lg.info(f"✅ Extracted {len(df)} rows")
        lg.info(f"📊 Columns: {list(df.columns)}")
        lg.info()
        
        # Transform
        lg.info("🔄 STEP 2: TRANSFORM")
        df_transformed = transform(df)
        lg.info(f"✅ Transformed data ready")
        lg.info()
        
        # Load
        lg.info("📤 STEP 3: LOAD")
        load(df_transformed, db_path)
        lg.info()
        
        lg.info("🎉 ETL Pipeline completed successfully!")
        lg.info(f"📈 Final dataset: {len(df_transformed)} rows, {len(df_transformed.columns)} columns")
        
    except FileNotFoundError as e:
        lg.error(f"❌ File Error: {e}")

    except ValueError as e:
        # TODO (Find & Fix): Error handling missing
        pass
    except Exception as e:
        # TODO (Find & Fix): Error handling missing
        pass

if __name__ == "__main__":    
    # Run the pipeline
    run_pipeline()