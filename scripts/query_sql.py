import sqlite3
import pandas as pd
import os


def get_connection(db_path):
    """Opens a connection to the SQLite db"""
    
    return sqlite3.connect(db_path)


def run_query(query, db_path):
    """Runs a SQL query and returns the result as a pandas df"""
    
    conn = get_connection(db_path)
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    return df


if __name__ == "__main__":
    db_path = os.path.join("db", "training_titanic.db")
    
    query = """
    SELECT * FROM passengers ORDER BY RANDOM() LIMIT 10;
    """
    
    result = run_query(query, db_path)
    print("[INFO] Query result:")
    print(result)