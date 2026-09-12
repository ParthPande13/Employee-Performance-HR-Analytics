import pandas as pd


def classify_salary(monthly_income):
    if monthly_income < 3000:
        return "Low"

    if monthly_income <= 7000:
        return "Medium"

    return "High"


def classify_experience(years):
    if years <= 3:
        return "Early Career"

    if years <= 10:
        return "Mid Career"

    return "Senior"


def transform_data(df):
    df = df.copy()

    # Annual salary
    df["AnnualIncome"] = (
        df["MonthlyIncome"] * 12
    )

    # Salary Band
    df["SalaryBand"] = (
        df["MonthlyIncome"].apply(classify_salary)
    )

    # Experience Group
    df["ExperienceGroup"] = (
        df["TotalWorkingYears"].apply(classify_experience)
    )

    # Attrition as numeric flag (useful for correlation analysis)
    df["AttritionFlag"] = (
        df["Attrition"].map({"Yes": 1, "No": 0})
    )

    return df