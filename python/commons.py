import duckdb


class Commons:
    database = "database/project_database.db"
    conn_db = duckdb.connect(database)
    facebook_data = "data/facebook_clicks.csv"
    facebook_table = "facebook_csv"
    google_data = "data/google_clicks.csv"
    google_table = "google_csv"
    site_events_data = "data/site_events.csv"
    site_events_table = "site_events"
    tracked_user_table = "tracked_user"