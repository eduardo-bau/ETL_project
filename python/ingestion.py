import duckdb
from commons import Commons


def main_extraction(csv_data, table_name, connection):
    
    create_table = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
    timestamp DATETIME,
    user_id VARCHAR,
    session_key VARCHAR,
    device_type VARCHAR,
    campaign VARCHAR,
    ad_set VARCHAR,
    spend double,
    utm_channel VARCHAR,
    fbclid VARCHAR
    )
    """
    
    query = f"""
    INSERT OR REPLACE INTO {table_name}
    SELECT *
    FROM read_csv('{csv_data}', header = True, sep = '|')
    """

    connection.sql(create_table)
    connection.sql(query)

if __name__ == "__main__":
    com = Commons()
    conn = com.conn_db
    csv_data = com.facebook_data
    table_name_1 = com.facebook_table
    main_extraction(csv_data, table_name_1, conn)
    conn.close()