import pandas as pd
import sqlite3
import os


def load_train_csv_to_sqlite(csv_path, db_path, table_name="passengers"):
    """Loads the csv file passanger training data into a SQLite database"""

    # read the csv into a df
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"[ERROR] CSV file not found: {csv_path}")

    # drop unnamed cols
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"], inplace=True)

    # connect or create SQLite
    conn = sqlite3.connect(db_path)

    # write in the db file, replace table if it already exists
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    # print first 5 rows
    print(f"[INFO] Loaded '{csv_path}' into '{table_name}' table in '{db_path}'")
    preview = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 5;", conn)
    print(preview)

    conn.close()


if __name__ == "__main__":
    csv_file = os.path.join("data", "train.csv")
    db_file = os.path.join("db", "training_titanic.db")

    load_train_csv_to_sqlite(csv_file, db_file)
