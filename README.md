# ETL_project

This project was made in python, using duckdb and polars.

First file ingest 3 csv files which are fb_clicks, google clicks and site_events. The ingestion is made executing with python duckdb API creating schemas where the csv will be stored.

Second file makes the corresponing transformations where 3 tables are unionized then necesary columns are selected, the resulting dataframe processed with polars is then write to a table in duckdb wich is the las step of the etl.