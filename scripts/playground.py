import pandas as pd
import query_sql as qs
import os


db_path = os.path.join("db", "training_titanic.db")
# print(qs.run_query("SELECT * FROM passengers WHERE age > 24 ORDER BY RANDOM() LIMIT 5", db_path))

print("Total entries: \n")
print(qs.run_query("SELECT COUNT(*) FROM passengers", db_path))

# check if columns have NULL values
print("Suvived NULL: \n")
print(qs.run_query("SELECT COUNT(*) FROM passengers WHERE SURVIVED IS NULL", db_path))

print("Pclass NULL: \n")
print(qs.run_query("SELECT COUNT(*) FROM passengers WHERE Pclass IS NULL", db_path))

print("Sex NULL: \n")
print(qs.run_query("SELECT COUNT(*) FROM passengers WHERE Sex IS NULL", db_path))

print("Age NULL: \n")
print(qs.run_query("SELECT COUNT(*) FROM passengers WHERE Age IS NULL", db_path))

print("Age NULL: \n")
print(qs.run_query("SELECT COUNT(*) FROM passengers WHERE Age IS NULL", db_path))

print("SibSp NULL: \n")
print(qs.run_query("SELECT COUNT(*) FROM passengers WHERE SibSp IS NULL", db_path))

print("Parch NULL: \n")
print(qs.run_query("SELECT COUNT(*) FROM passengers WHERE Parch IS NULL", db_path))

print("Fare NULL: \n")
print(qs.run_query("SELECT COUNT(*) FROM passengers WHERE Fare IS NULL", db_path))

print("Embarked NULL: \n")
print(qs.run_query("SELECT COUNT(*) FROM passengers WHERE Embarked IS NULL", db_path))

