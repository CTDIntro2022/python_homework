# Lesson 7 - Task 6

# The program should read all the orders for all the customers, 
# to get all the products that each as ordered into a DataFrame.
import pandas as pd
import sqlite3

with sqlite3.connect("./db/lesson.db") as conn:
    sql_statement = """SELECT c.customer_name, o.order_id, p.product_name FROM customers c JOIN orders o ON c.customer_id = o.customer_id 
    JOIN line_items li ON o.order_id = li.order_id JOIN products p ON li.product_id = p.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    print("DF: \n", df.head)
    print ("DF Info:\n", df.info())

    # As some customers may have ordered the same product in several different orders, you want to combine the rows for these different orders
    dfGroup = df.groupby(['customer_name', 'product_name']).size().reset_index(name='count')
    print ("Customer-Product Info:")
    print (dfGroup.info())
    print ("Customer-Prdouct Head:")
    print (dfGroup.head())

    dfFiltered = dfGroup[dfGroup['count'] > 1]
    print ("Customer-Prdouct GT1 Head:")
    print (dfFiltered.head())

    # Sort the DataFrame by the order_id column.
    df = df.sort_values(by='order_id')
    print ("Last 20 rows sorted by customer id")
    print (df.tail(20))