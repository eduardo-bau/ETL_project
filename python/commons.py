import duckdb


class Commons:
    database = "database/project_database.db"
    conn_db = duckdb.connect(database)
    facebook_data = "data/facebook_clicks.csv"
    facebook_table = "facebook_csv"