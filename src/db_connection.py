from sqlalchemy import create_engine

from src.config import (
    get_mysql_uri,
    MYSQL_TABLE_NAME
)


def get_engine():
    engine = create_engine(
        get_mysql_uri()
    )

    return engine


def load_dataframe_to_mysql(df, engine):
    df.to_sql(
        MYSQL_TABLE_NAME,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(
        f"Loaded {len(df)} rows into MySQL table '{MYSQL_TABLE_NAME}'"
    )
