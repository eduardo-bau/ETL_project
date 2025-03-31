import duckdb
from commons import Commons


def main_extraction(csv_data, table_name, connection):
    
    create_table = f"""
    CREATE OR REPLACE TABLE {table_name} (
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
    INSERT INTO {table_name}
    SELECT *
    FROM read_csv('{csv_data}', header=True, sep='|')   
    """

    connection.execute(create_table)
    connection.execute(query)

def google_extraction(csv_data, table_name, connection):
    
    create_table = f"""
    CREATE OR REPLACE TABLE {table_name} (
    timestamp DATETIME,
    user_id VARCHAR,
    session_key VARCHAR,
    device_type VARCHAR,
    campaign VARCHAR,
    ad_group VARCHAR,
    cost double,
    utm_channel VARCHAR,
    gclid VARCHAR
    )
    """
    
    query = f"""
    INSERT INTO {table_name}   
    SELECT *
    FROM read_csv('{csv_data}', header=True, sep='|')
    """

    connection.execute(create_table)
    connection.execute(query)

def site_extraction(csv_data, table_name, connection):
    
    create_table = f"""
    CREATE OR REPLACE TABLE {table_name} (
    timestamp DATETIME,
    user_id VARCHAR,
    session_key VARCHAR,
    device_type VARCHAR,
    action_type VARCHAR,
    action_details VARCHAR,
    utm_channel VARCHAR
    )
    """
    
    query = f"""
    INSERT INTO {table_name}   
    SELECT *
    FROM read_csv('{csv_data}', header=True, sep='|')
    """

    connection.execute(create_table)
    connection.execute(query)

if __name__ == "__main__":
    com = Commons()
    conn = com.conn_db
    csv_data = com.facebook_data
    csv_data_2 = com.google_data
    csv_data_3 = com.site_events_data
    table_name_1 = com.facebook_table
    table_name_2 = com.google_table
    table_name_3 = com.site_events_table
    main_extraction(csv_data, table_name_1, conn)
    google_extraction(csv_data_2, table_name_2, conn)
    site_extraction(csv_data_3, table_name_3, conn)
    print("creation of stage tables completed")
    conn.close()