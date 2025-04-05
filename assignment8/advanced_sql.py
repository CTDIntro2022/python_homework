import pandas as pd
import sqlite3



# customer names, all the orders, and the names of all the product that were ordered.
with sqlite3.connect("../db/lesson.db") as conn:
    sql_statement = """SELECT c.customer_name, o.order_id, p.product_name FROM customers c JOIN orders o ON c.customer_id = o.customer_id 
    JOIN line_items li ON o.order_id = li.order_id JOIN products p ON li.product_id = p.product_id;"""
    df = pd.read_sql_query(sql_statement, conn)
    # print(df)

# For each of the first 5 orders (as ordered by order_id), find the each of the product names for the order.  
# Return a list that includes the order_id, the line_item_id, and the product name.  
# There are several steps here.  
#    1. You need a subquery to retrieve the order_id for the first 5 orders.  In this subquery, you use ORDER BY order_id and LIMIT 5.  
#    2. In the main query, you need to select the order_id, line_item_id, and product_name from the orders table, the line_items table, and the products table.  
#    3. Then you need a WHERE clause: WHERE o.order_id IN (...).  The subquery is what returns the set of order_ids you want to check.

# Task 1 Retrieve order details for the first 5 orders
query1 =  """
    SELECT o.order_id, l.line_item_id, p.product_name
    FROM orders o
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    WHERE o.order_id IN (
        SELECT order_id
        FROM orders
        ORDER BY order_id
        LIMIT 5
    )
    ORDER BY o.order_id, l.line_item_id;
"""

# Task 2 Find the total price of each of the first 5 orders. 
query2 = """
    SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
    FROM orders o
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5;
"""
# Task 3 Queries
# Insert order
query3_insert_order = """
                    INSERT INTO orders (customer_id, employee_id, date)
                    VALUES (?, ?, DATE('now'))
                    RETURNING order_id;
                """
# Insert corresponding line itmes
query3_insert_lineItems = """
                        INSERT INTO line_items (order_id, product_id, quantity)
                        VALUES (?, ?, 10)
                    """
# Get details of latest order 
query3_details = """
                    SELECT l.line_item_id, l.quantity, p.product_name
                    FROM line_items l
                    JOIN products p ON l.product_id = p.product_id
                    WHERE l.order_id = (SELECT MAX(order_id) FROM orders)
    """

# Task 4 Aggregation with HAVING
# Find all employees associated with more than 5 orders.
query4 = """
    SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
    FROM employees e
    JOIN orders o ON e.employee_id = o.employee_id
    GROUP BY e.employee_id
    HAVING COUNT(o.order_id) > 5;
"""
with sqlite3.connect("../db/lesson.db") as conn:

    cursor = conn.cursor()

    # Task 1
    # Retrieve order details for the first 5 orders
    df = pd.read_sql_query(query1, conn)
    print ("TGask 1: Details of first five orders:")
    print(df)

    # Task 2 Find the total price of each of the first 5 orders. 
    df = pd.read_sql_query(query2, conn)
    print ("Task 2: Total price of first fiver orders")
    print(df)
    
    # Task 3
    # An Insert Transaction Based on Data
    # Get customer_id for 'Perez and Sons'
    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
    customer_id = cursor.fetchone()[0]

    # Get employee_id for 'Miranda Harris'
    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
    employee_id = cursor.fetchone()[0]

    # Get product_ids of 5 least expensive products
    cursor.execute("SELECT product_id FROM products ORDER BY price LIMIT 5")
    product_ids = [row[0] for row in cursor.fetchall()]

    # Insert new order and retrieve order_id
    cursor.execute(query3_insert_order, (customer_id, employee_id))
    order_id = cursor.fetchone()[0]

    # Insert line items for the order
    for product_id in product_ids:
        cursor.execute(query3_insert_lineItems, (order_id, product_id))

    conn.commit()
    print(f"New order {order_id} created successfully.")

    # Task 3 continued - Get the details of newly created order
    df = pd.read_sql_query(query3_details, conn)
    print("\nNew Order Line Items:")
    print (df)

    # Task 4 - Employees with more thanm 5 orders
    df = pd.read_sql_query(query4, conn)
    print("\nEmployees with More Than 5 Orders:")
    print (df)
