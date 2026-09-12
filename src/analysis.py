import pandas as pd


def generate_analysis(df):

    analysis = {}

    # Overall KPIs
    analysis["Total Employees"] = df.shape[0]

    analysis["Average Salary"] = df["MonthlyIncome"].mean()

    analysis["Highest Salary"] = df["MonthlyIncome"].max()

    analysis["Average Experience (Years)"] = df["TotalWorkingYears"].mean()

    analysis["Attrition Rate (%)"] = (
        df["AttritionFlag"].mean() * 100
    )

    analysis["Average Performance Rating"] = df["PerformanceRating"].mean()

    # Department analysis
    dept_salary = (
        df.groupby("Department")["MonthlyIncome"].mean()
        .sort_values(ascending=False)
    )

    analysis["Highest Paying Department"] = (
        dept_salary.index[0]
    )

    dept_attrition = (
        df.groupby("Department")["AttritionFlag"].mean()
        .sort_values(ascending=False)
    )

    analysis["Department with Highest Attrition"] = (
        dept_attrition.index[0]
    )

    # Education analysis
    education_salary = (
        df.groupby("EducationField")["MonthlyIncome"].mean()
        .sort_values(ascending=False)
    )

    analysis["Highest Paying Education Field"] = (
        education_salary.index[0]
    )

    # Business Travel analysis (used in place of Work Mode,
    # since this dataset has no Remote/Hybrid/Office column)
    travel_counts = (
        df["BusinessTravel"].value_counts()
    )

    analysis["Most Common Business Travel Pattern"] = (
        travel_counts.index[0]
    )

    # Gender distribution
    gender_counts = (
        df["Gender"].value_counts()
    )

    analysis["Majority Gender"] = (
        gender_counts.index[0]
    )

    # Correlation: Experience vs Salary
    analysis["Experience-Salary Correlation"] = (
        df["TotalWorkingYears"].corr(df["MonthlyIncome"])
    )

    return analysis


def save_business_insights(
        analysis,
        file_path
):
    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        for key, value in analysis.items():

            if isinstance(value, float):
                value = round(
                    value,
                    2
                )

            file.write(
                f"{key}: {value}\n"
            )