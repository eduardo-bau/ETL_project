# ETL Project

This project was developed in Python using DuckDB and Polars.

The first script ingests three CSV files (`fb_clicks`, `google_clicks`, and `site_events`) by executing the DuckDB API in Python, creating schemas to store the CSV data.

The second script performs the necessary transformations:
- Unionizes the three tables
- Selects the required columns
- Processes the resulting DataFrame with Polars
- Writes the final output to a DuckDB table, completing the ETL pipeline.