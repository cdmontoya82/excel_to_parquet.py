import pandas as pd
import os
import glob
import warnings

# Ignore openpyxl warnings about missing default styles in auto-generated Excel files
warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

def convert_excel_to_parquet(source_folder, destination_folder):
    """
    Converts all Excel (.xlsx) files in the source directory to Parquet format.
    """
    # 1. Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder: {destination_folder}")

    # 2. Find all .xlsx files in the source folder
    excel_files = glob.glob(os.path.join(source_folder, "*.xlsx"))
    
    print(f"Found {len(excel_files)} file(s) to process.\n")

    for file in excel_files:
        try:
            # Get the base filename without extension
            file_name = os.path.basename(file)
            name_without_ext = os.path.splitext(file_name)[0]
            
            # Define the final Parquet file path
            parquet_file = os.path.join(destination_folder, f"{name_without_ext}.parquet")

            # 3. Read the Excel file
            print(f"Reading: {file_name}...")
            df = pd.read_excel(file)

            # 4. Clean data types for Parquet compatibility
            # Parquet is strict with data types. Converting 'object' columns to explicit strings.
            for col in df.columns:
                if df[col].dtype == 'object':
                    df[col] = df[col].astype(str)

            # 5. Save as Parquet
            df.to_parquet(parquet_file, engine='pyarrow', index=False)
            
            print(f"-> Successfully saved: {name_without_ext}.parquet")

        except Exception as e:
            print(f"XXX Error converting {file_name}: {e}")

    print("\n--- Process completed ---")

# --- CONFIGURATION ---
# Use generic relative paths for the public repository
INPUT_FOLDER = r'./input_data'
OUTPUT_FOLDER = r'./output_data'

if __name__ == "__main__":
    convert_excel_to_parquet(INPUT_FOLDER, OUTPUT_FOLDER)
