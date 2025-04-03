import pandas as pd
import sqlite3



# customer names, all the orders, and the names of all the product that were ordered.
with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT c.customer_name, o.order_id, p.product_name FROM customers c JOIN orders o ON c.customer_id = o.customer_id 
    JOIN line_items li ON o.order_id = li.order_id JOIN products p ON li.product_id = p.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    # print(df)

# The SQL statement should retrieve the line_item_id, quantity, product_id, product_name, 
# and price from a JOIN of the line_items table and the product table. 
# Hint: Your ON statement would be ON line_items.product_id = products.product_id.
with sqlite3.connect("../db/lesson.db") as conn:
    #sql_statement = "SELECT line_items.line_item_id,line_Items.quantity, line_items.product_id, products.product_name \
    #   FROM line_items JOIN products ON line_items.product_id = products.product_id"
    #sql_statement = "Select l.line_item_id, l.quantity, l.product_id, p.product_name FROM line_items as l JOIN products as p \
    #    ON l.product_id = p.product_id"
    sql_statement = "Select l.line_item_id, l.quantity, l.product_id, p.product_name, p.price FROM line_items l JOIN products p \
           ON l.product_id = p.product_id"
    df = pd.read_sql_query(sql_statement, conn)
    print(df.head(5))

    # Add a column to the DataFrame called "total". 
    # This is the quantity times the price. (This is easy: df[total] = df[quantity] * df[price]). Print out the first 5 lines of the DataFrame to make sure this works.
    df["total"] = df["quantity"] * df["price"]
    print(df.head(5))

    # Add groupby() code to group by the product_id. Use an agg() method that specifies 'count' for the line_item_id column, 'sum' for the total column, 
    # and 'first' for the 'product_name'. Print out the first 5 lines of the resulting DataFrame. Run the program to see if it is correct so far.
    # dfAgg = df.groupby ('product_id').agg({'product_name':['first'],'line_item_id':['count'], 'total':['sum']})
    dfAgg = df.groupby ('product_id').agg({'product_name':'first','line_item_id':'count', 'total':'sum'})
    print ("Aggregated:")
    print (dfAgg.head(10))
    column_names = df.columns.tolist()
    print ("Column names: ", column_names)

    # Sort the DataFrame by the product_name column.
    # dfAgg.sort_values(by=['product_name'])
    dfAgg.sort_values(by='product_name',ascending=True,inplace=True)
    print (dfAgg.head(10))

