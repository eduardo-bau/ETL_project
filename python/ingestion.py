import duckdb


def main(csv_data):
    data = duckdb.read_csv(csv_data, header=True, sep="|")

    query = f"""
    SELECT *
    from {data}
    """



csv_data = 'data/*.csv'