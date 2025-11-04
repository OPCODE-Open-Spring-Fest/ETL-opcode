import os

from app.etl.extract import extract
from app.etl.transform import transform
from app.etl.load import load

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
        print("🚀 Starting ETL Pipeline")  # TODO (Find & Fix): Use logging instead of print
        print(f"📁 Input file: {csv_path}")
        print(f"🗄️ Output database: {db_path}")
        print("-" * 50)
        
        # Extract
        print("📥 STEP 1: EXTRACT")
        df = extract(csv_path)
        print(f"✅ Extracted {len(df)} rows")
        print(f"📊 Columns: {list(df.columns)}")
        print()
        
        # Transform
        print("🔄 STEP 2: TRANSFORM")
        df_transformed = transform(df)
        print(f"✅ Transformed data ready")
        print()
        
        # Load
        print("📤 STEP 3: LOAD")
        load(df_transformed, db_path)
        print()
        
        print("🎉 ETL Pipeline completed successfully!")
        print(f"📈 Final dataset: {len(df_transformed)} rows, {len(df_transformed.columns)} columns")
        
    except FileNotFoundError as e:
        print(f"❌ File Error: {e}")

    except ValueError as e:
        # TODO (Find & Fix): Error handling missing
        pass
    except Exception as e:
        # TODO (Find & Fix): Error handling missing
        pass

if __name__ == "__main__":    
    # Run the pipeline
    run_pipeline()