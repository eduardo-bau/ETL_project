import polars as pl
import duckdb
from commons import Commons

com = Commons()

conn = com.conn_db

df = conn.sql("""SELECT * from facebook_csv""").pl()

df_transformed = (
    df
    .select()
)