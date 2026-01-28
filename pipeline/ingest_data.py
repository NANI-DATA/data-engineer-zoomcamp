import pandas as pd
from sqlalchemy import create_engine

def run():

    pg_user = 'root'
    pg_pass = 'root'
    pg_host = 'localhost'
    pg_port = 5432
    pg_db = 'ny_taxi'

    engine = create_engine(
        f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}'
    )

    # ---------------- GREEN TAXI DATA ----------------
    year = 2025
    month = 11

    prefix = 'https://d37ci6vzurychx.cloudfront.net/trip-data'
    url = f'{prefix}/green_tripdata_{year}-{month:02d}.parquet'

    df = pd.read_parquet(url)

    df.to_sql(
        name='green_tripdata_2025_11',
        con=engine,
        if_exists='replace',
        index=False
    )

    # ---------------- ZONE LOOKUP ----------------
    zone_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv'
    df_zone = pd.read_csv(zone_url)

    df_zone.to_sql(
        name='taxi_zone_lookup',
        con=engine,
        if_exists='replace',
        index=False
    )

    print("✅ Data ingestion completed successfully")

if __name__ == '__main__':
    run()
