import pandas as pd

def infer_mysql_schema(csv_path, table_name):
    """
    infers a MySQL CREATE TABLE statement from a CSV file.

    parameters:
        csv_path (str): Path to the CSV file.
        table_name (str): Desired name for the MySQL table.

    Returns:
        str: SQL CREATE TABLE statement.

    """

    # Load CSV into DataFrame
    df = pd.read_csv(csv_path)

    # Mapping pandas dtypes to MySQL types
    dtype_map = {
        "object": "VARCHAR(255)",
        "int64": "INT",
        "float64": "FLOAT",
        "bool": "BOOLEAN",
        "datetime64[ns]": "DATETIME"
    }

    # Generate solumn definitions
    columns_sql = []
    for col, dtype in df.dtypes.items():
        mysql_type = dtype_map.get(str(dtype), "VARCHAR(255)")
        #Replace spaces and make column name lowercase
        col_safe = col.replace(" ", "_").lower()
        columns_sql.append(f"`{col_safe}` {mysql_type}")

    # Combine columns into CREATE TABLE statement
    column_definitions = ",\n ".join(columns_sql)
    create_table_sql = f"CREATE TABLE `{table_name}` (\n {column_definitions}\n);"

    return create_table_sql

# For standalone script execution
if __name__ == "__main__":
    import sys

    if len(sys.argv) !=3:
        print("Usage: python csv_to_sql.py path/to/file.csv table_name")
    else:
        csv_path, table_name = sys.argv[1], sys.argv[2]
        sql = infer_mysql_schema(csv_path, table_name)
        print(sql)


        