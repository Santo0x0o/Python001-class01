# 作业背景：在数据处理的步骤中，可以使用 SQL 语句或者 pandas 加 Python 库、函数等方式进行数据的清洗和处理工作。
# 因此需要你能够掌握基本的 SQL 语句和 pandas 等价的语句，利用 Python 的函数高效地做聚合等操作。
# 作业要求：请将以下的 SQL 语句翻译成 pandas 语句：
# 1. SELECT * FROM data;
# 2. SELECT * FROM data LIMIT 10;
# 3. SELECT id FROM data;  //id 是 data 表的特定一列
# 4. SELECT COUNT(id) FROM data;
# 5. SELECT * FROM data WHERE id<1000 AND age>30;
# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
# 9. DELETE FROM table1 WHERE id=10;
# 10. ALTER TABLE table1 DROP COLUMN column_name;

import pandas as pd
import pymysql

conn = pymysql.connect('ip','name','pass','dbname','charset=utf8')
### 1. get data from mysql
# 1. SELECT * FROM data;
sql  =  'SELECT *  FROM data'
df = pd.read_sql(sql,conn)
df
### 2. select LIMIT 10 line
# 2. SELECT * FROM data LIMIT 10;
df.head(10)
### 3. get id
# 3. SELECT id FROM data;  //id 是 data 表的特定一列
df['id']
### 4. count id in data
# 4. SELECT COUNT(id) FROM data;
df['id'].shape[0]
### 5. get specific data 
# 5. SELECT * FROM data WHERE id<1000 AND age>30;
df[(df['id']<1000) & (df['age']>30)]
### 6. get id and order_id dictinct value
# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
sql_t1  =  'SELECT *  FROM table1'
df_t1 = pd.read_sql(sql_t1, conn)
df_t1.groupby('id')['order_id'].count()
### 7. join table
# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
sql_t2  =  'SELECT *  FROM table2'
df_t2 = pd.read_sql(sql_t2, conn)
pd.merge(df_t1, df_t2, on='id', how='inner')
### 8. concat data
# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat([df_t1, df_t2], axis=0).drop_duplicates()
### 9. delete specific data
# 9. DELETE FROM table1 WHERE id=10;
df_t1=df_t1[~(df_t1['id']==10)]
### 10.
# 10. ALTER TABLE table1 DROP COLUMN column_name;
df_t1.drop(columns='column_name', inplace=True)


