import pandas as pd
import sqlite3
import os


def load_data_from_sqlite(db_path, table_name="passengers"):
    """Connects to the SQLite database and returns it in a pandas df"""
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    
    return df


def clean_data(df):
    
    # drop cols that are not useful for modelling
    df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])
    
    # handle missing age by filling with the median
    # df["Age"].fillna(df["Age"].median(), inplace=True)
    df["Age"] = df["Age"].fillna(df["Age"].median())
    
    # drop rows where embarked is missing (only 2)
    df.dropna(subset=["Embarked"], inplace=True)
    
    # encode sex: male -> 0 female -> 1
    df["Sex"].map({"male" : 0, 
                   "female" : 1})
    # one-hot encode Embarked (drop first to avoid multicollinearity)
    df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)
    
    return df


if __name__ == "__main__":
    db_path = os.path.join("db", "training_titanic.db")
    output_path = os.path.join("output", "cleaned_data.csv")
    
    # load data
    df = load_data_from_sqlite(db_path)
    print(f"[INFO] Loaded {len(df)} rows from database.")
    
    # clean data
    df_clean = clean_data(df)
    print(f"[INFO] Cleaned data shape: {df_clean.shape}")
    
    # save to csv
    df_clean.to_csv(output_path, index=False)
    print(f"[INFO] Saved cleaned data to {output_path}")
