import pandas as pd

def transform_date_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms 'datePlayed' column into MySQL-compatible formats.

    Parameters:
        df (pd.DataFrame): Original dataframe with raw string columns.

    Returns:
        pd.DataFrame: Modified dataframe with converted datetime columns. 
    """

    # Convert 'datePlayed' from DD/MM/YYYY to YYYY-MM-DD
    if 'datePlayed' in df.columns:
        try:
            df['datePlayed'] = pd.to_datetime(df['datePlayed'], format="%d/%m/%Y").dt.date
        except Exception as e:
            print(f"[ERROR] Failed to convert 'datePlayed': {e}")

    return df

# For direct execution and testing
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python transform_datetime.py input_file.csv output_file.csv")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]

        df = pd.read_csv(input_path)
        df_cleaned = transform_date_columns(df)
        df_cleaned.to_csv(output_path, index=False)
        print(f"[INFO] Saved cleaned data to: {output_path}")
    