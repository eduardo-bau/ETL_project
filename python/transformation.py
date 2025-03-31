from polars import col, concat_str, concat
import duckdb
from commons import Commons

com = Commons()

conn = com.conn_db

df_fb = conn.sql("SELECT * from facebook_csv").pl()

df_google = conn.sql("SELECT * from google_csv").pl()

df_events = conn.sql("SELECT * FROM site_events").pl()

df_concated = concat([df_fb, df_google, df_events], how="align")

df_transformed = (
    df_concated
    .select(
        concat_str([col("session_key"), col("device_type")]).alias("tracked_user_id"),
        col("user_id").alias("visitor_id"),
        col("session_key").alias("session_id"),
        col("device_type").alias("device_id"),
        col("utm_channel").alias("utm_source"),
        col("action_details").alias("traits"),
        col("timestamp").min().alias("first_seen"),
        col("timestamp").max().alias("last_seen")
    )
)

conn.execute(f"""
CREATE OR REPLACE TABLE {com.tracked_user_table} AS
    SELECT *
    FROM df_transformed
""")

conn.close()