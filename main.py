import os

from src.config import (
    PROCESSED_DATA_PATH,
    GRAPH_PATH,
    ANALYSIS_PATH,
    REPORT_PATH,
    SQL_PATH
)

from src.data_loader import (
    load_data
)

from src.data_cleaning import (
    clean_data,
    save_cleaned_data
)

from src.data_transformation import (
    transform_data
)

from src.db_connection import (
    get_engine,
    load_dataframe_to_mysql
)

from src.sql_queries import (
    run_all_sql_tasks,
    save_sql_results
)

from src.analysis import (
    generate_analysis,
    save_business_insights
)

from src.visualization import (
    create_visualizations
)

from src.report import (
    create_report
)


def main():

    print("Loading data...")
    df = load_data()

    print("Cleaning data...")
    df = clean_data(df)

    os.makedirs(
        os.path.dirname(PROCESSED_DATA_PATH),
        exist_ok=True
    )
    save_cleaned_data(df)

    print("Transforming data...")
    df = transform_data(df)

    print("Connecting to MySQL and loading table...")
    engine = get_engine()
    load_dataframe_to_mysql(df, engine)

    print("Running SQL tasks...")
    sql_results = run_all_sql_tasks(engine)

    os.makedirs(
        os.path.dirname(SQL_PATH),
        exist_ok=True
    )
    save_sql_results(sql_results, SQL_PATH)

    print("Generating analysis...")
    analysis = generate_analysis(df)

    print("Saving business insights...")
    os.makedirs(
        os.path.dirname(ANALYSIS_PATH),
        exist_ok=True
    )
    save_business_insights(analysis, ANALYSIS_PATH)

    print("Creating visualizations...")
    os.makedirs(GRAPH_PATH, exist_ok=True)
    create_visualizations(df, GRAPH_PATH)

    print("Creating PDF report...")
    os.makedirs(
        os.path.dirname(REPORT_PATH),
        exist_ok=True
    )
    create_report(analysis, df, GRAPH_PATH, REPORT_PATH)

    print("\nHR Analytics Project Completed Successfully")


if __name__ == "__main__":
    main()