import mysql.connector as c
import pandas as pd
con = c.connect(
    host='localhost',
    user='root',
    password='root',
    database='cvr'
)

if con.is_connected():
    print("✅ Connection successful!")

df=pd.read_sql("select * from student",con)
print(df)
print(type(df))
