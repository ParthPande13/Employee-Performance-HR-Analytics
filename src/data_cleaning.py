import pandas as pd

from src.config import PROCESSED_DATA_PATH


def clean_data(df):
    df = df.copy()

    # Remove duplicates
    df = df.drop_duplicates()

    # Clean text columns
    text_columns = [
        "Attrition",
        "BusinessTravel",
        "Department",
        "EducationField",
        "Gender",
        "JobRole",
        "MaritalStatus",
        "Over18",
        "OverTime"
    ]

    for column in text_columns:
        df[column] = (
            df[column]
            .astype(str)
            .str.strip()
        )

    # Numeric conversion (defensive - source data is already numeric,
    # but this guards against dirty exports)
    numeric_columns = [
        "Age",
        "DailyRate",
        "DistanceFromHome",
        "Education",
        "HourlyRate",
        "JobLevel",
        "MonthlyIncome",
        "MonthlyRate",
        "NumCompaniesWorked",
        "PercentSalaryHike",
        "PerformanceRating",
        "StockOptionLevel",
        "TotalWorkingYears",
        "TrainingTimesLastYear",
        "YearsAtCompany",
        "YearsInCurrentRole",
        "YearsSinceLastPromotion",
        "YearsWithCurrManager"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"  # converts bad values into NaN
        )

    # Handle missing values
   
    df["MonthlyIncome"] = df["MonthlyIncome"].fillna(
        df["MonthlyIncome"].median()
    )

    df["TotalWorkingYears"] = df["TotalWorkingYears"].fillna(
        df["TotalWorkingYears"].median()
    )

    df["Age"] = df["Age"].fillna(
        df["Age"].median()
    )

    df["NumCompaniesWorked"] = df["NumCompaniesWorked"].fillna(0)

    # Remove invalid / impossible values
    df = df[
        df["Age"] > 0
    ]

    df = df[
        df["MonthlyIncome"] > 0
    ]

    df = df[
        df["TotalWorkingYears"] >= 0
    ]

    # Drop any row where Age, MonthlyIncome, OR TotalWorkingYears is NaN (missing).
    df = df.dropna(
        subset=["Age", "MonthlyIncome", "TotalWorkingYears"]
    )

    # Reset index
    df = df.reset_index(
        drop=True
    )

    return df


def save_cleaned_data(df):
    df.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )
