import psycopg2
import pandas as pd

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="finance_db",
    user="finance_db_user",
    password="1234",
    host="localhost",
    port="5432"
)

df = pd.read_sql("SELECT * FROM products", conn)
df.to_csv("open_orders_by_date_status.csv", index=False)
## Export: Open Orders by Delivery Date and Status
#df = pd.read_sql("SELECT * FROM mv_open_orders", conn)
#df.to_csv("open_orders_by_date_status.csv", index=False)
#
## Export: Top 3 Delivery Dates
#df = pd.read_sql("SELECT * FROM mv_top_delivery_dates", conn)
#df.to_csv("top_delivery_dates.csv", index=False)
#
## Export: Pending Items by Product ID
#df = pd.read_sql("SELECT * FROM mv_pending_items", conn)
#df.to_csv("pending_items_by_product.csv", index=False)
#
## Export: Top 3 Customers
#df = pd.read_sql("SELECT * FROM mv_top_customers", conn)
#df.to_csv("top_customers.csv", index=False)
