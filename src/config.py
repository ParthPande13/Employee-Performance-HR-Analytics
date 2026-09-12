import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

RAW_DATA_PATH = os.path.join(
    BASE_DIR,
    'data',
    'raw',
    'hr_raw.csv'
)

PROCESSED_DATA_PATH = os.path.join(
    BASE_DIR,
    'data',
    'processed',
    'hr_cleaned.csv'
)

GRAPH_PATH = os.path.join(
    BASE_DIR,
    'outputs',
    'graphs'

)

ANALYSIS_PATH = os.path.join(
    BASE_DIR,
    'outputs',
    'analysis',
    'business_insights.txt'

)

REPORT_PATH = os.path.join(
    BASE_DIR ,
    'outputs',
    'reports',
    'HR_Analytics_EDA_report.pdf'

)

SQL_PATH = os.path.join(
    BASE_DIR ,
    'outputs',
    'analysis',
    'sql_query_results.txt'
)


# SQL CONNECTION
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'MyNewPassword123!'
MYSQL_DATABASE = 'hr_analytics'
MYSQL_TABLE_NAME = 'employees'


def get_mysql_uri():
    return (
        f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}"
        f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    )