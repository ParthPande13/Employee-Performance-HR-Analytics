import pandas as pd


def total_employees_by_department(engine):
    query = """
        SELECT Department, COUNT(*) AS TotalEmployees
        FROM employees
        GROUP BY Department
        ORDER BY TotalEmployees DESC;
    """
    return query, pd.read_sql(query, engine)


def average_salary_by_department(engine):
    query = """
        SELECT Department, ROUND(AVG(MonthlyIncome), 2) AS AvgMonthlyIncome
        FROM employees
        GROUP BY Department
        ORDER BY AvgMonthlyIncome DESC;
    """
    return query, pd.read_sql(query, engine)


def top_10_highest_paid_employees(engine):
    query = """
        SELECT EmployeeNumber, Department, JobRole, MonthlyIncome
        FROM employees
        ORDER BY MonthlyIncome DESC
        LIMIT 10;
    """
    return query, pd.read_sql(query, engine)


def average_experience_by_department(engine):
    query = """
        SELECT Department, ROUND(AVG(TotalWorkingYears), 2) AS AvgExperienceYears
        FROM employees
        GROUP BY Department
        ORDER BY AvgExperienceYears DESC;
    """
    return query, pd.read_sql(query, engine)


def employees_with_highest_performance_rating(engine):
    query = """
        SELECT EmployeeNumber, Department, JobRole, PerformanceRating
        FROM employees
        WHERE PerformanceRating = (
            SELECT MAX(PerformanceRating) FROM employees
        );
    """
    return query, pd.read_sql(query, engine)


def count_by_business_travel(engine):
    # Used as the closest available substitute for "Work Mode"
    # (Remote/Hybrid/Office), since this dataset has no such column.
    query = """
        SELECT BusinessTravel, COUNT(*) AS EmployeeCount
        FROM employees
        GROUP BY BusinessTravel
        ORDER BY EmployeeCount DESC;
    """
    return query, pd.read_sql(query, engine)


def departments_with_highest_attrition(engine):
    query = """
        SELECT
            Department,
            SUM(AttritionFlag) AS AttritionCount,
            COUNT(*) AS TotalEmployees,
            ROUND(SUM(AttritionFlag) * 100.0 / COUNT(*), 2) AS AttritionRatePct
        FROM employees
        GROUP BY Department
        ORDER BY AttritionRatePct DESC;
    """
    return query, pd.read_sql(query, engine)


def rank_employees_by_salary_within_department(engine):
    query = """
        SELECT
            EmployeeNumber,
            Department,
            JobRole,
            MonthlyIncome,
            RANK() OVER (
                PARTITION BY Department
                ORDER BY MonthlyIncome DESC
            ) AS SalaryRankInDept
        FROM employees
        ORDER BY Department, SalaryRankInDept;
    """
    return query, pd.read_sql(query, engine)


def employees_above_average_salary(engine):
    query = """
        SELECT EmployeeNumber, Department, JobRole, MonthlyIncome
        FROM employees
        WHERE MonthlyIncome > (
            SELECT AVG(MonthlyIncome) FROM employees
        )
        ORDER BY MonthlyIncome DESC;
    """
    return query, pd.read_sql(query, engine)


def gender_distribution(engine):
    query = """
        SELECT Gender, COUNT(*) AS EmployeeCount
        FROM employees
        GROUP BY Gender;
    """
    return query, pd.read_sql(query, engine)


def run_all_sql_tasks(engine):
    tasks = {
        "Total Employees by Department": total_employees_by_department,
        "Average Salary by Department": average_salary_by_department,
        "Top 10 Highest Paid Employees": top_10_highest_paid_employees,
        "Average Experience by Department": average_experience_by_department,
        "Employees with Highest Performance Rating": employees_with_highest_performance_rating,
        "Employee Count by Business Travel": count_by_business_travel,
        "Departments with Highest Attrition": departments_with_highest_attrition,
        "Salary Rank within Department": rank_employees_by_salary_within_department,
        "Employees Above Average Salary": employees_above_average_salary,
        "Gender-wise Employee Distribution": gender_distribution,
    }

    results = {}

    for name, func in tasks.items():
        query, result_df = func(engine)
        results[name] = {
            "query": query.strip(),
            "result": result_df
        }

    return results


def save_sql_results(results, file_path):
    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        for name, content in results.items():
            file.write(f"{'=' * 70}\n")
            file.write(f"{name}\n")
            file.write(f"{'=' * 70}\n")
            file.write(content["query"] + "\n\n")
            file.write(content["result"].to_string(index=False))
            file.write("\n\n")