import os

import matplotlib.pyplot as plt

import seaborn as sns


def create_visualizations(
    df,
    output_path
):
    os.makedirs(
        output_path,
        exist_ok=True
    )

    # 1. Histogram - Salary Distribution
    plt.figure(figsize=(8, 5))
    plt.hist(df["MonthlyIncome"], bins=30, color="steelblue", edgecolor="black")
    plt.title("Salary Distribution")
    plt.xlabel("Monthly Income")
    plt.ylabel("Number of Employees")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "salary_histogram.png"))
    plt.close()

    # 2. Histogram - Age Distribution
    plt.figure(figsize=(8, 5))
    plt.hist(df["Age"], bins=20, color="darkorange", edgecolor="black")
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Number of Employees")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "age_histogram.png"))
    plt.close()

    # 3. Box Plot - Salary
    plt.figure(figsize=(6, 5))
    sns.boxplot(y=df["MonthlyIncome"])
    plt.title("Salary Box Plot")
    plt.ylabel("Monthly Income")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "salary_boxplot.png"))
    plt.close()

    # 4. Box Plot - Experience
    plt.figure(figsize=(6, 5))
    sns.boxplot(y=df["TotalWorkingYears"])
    plt.title("Experience Box Plot")
    plt.ylabel("Total Working Years")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "experience_boxplot.png"))
    plt.close()

    # 5. Count Plot - Department
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="Department", order=df["Department"].value_counts().index)
    plt.title("Employee Count by Department")
    plt.xlabel("Department")
    plt.ylabel("Number of Employees")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "department_countplot.png"))
    plt.close()

    # 6. Count Plot - Gender
    plt.figure(figsize=(6, 5))
    sns.countplot(data=df, x="Gender")
    plt.title("Employee Count by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Number of Employees")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "gender_countplot.png"))
    plt.close()

    # 7. Count Plot - Education
    plt.figure(figsize=(6, 5))
    sns.countplot(data=df, x="Education")
    plt.title("Employee Count by Education Level")
    plt.xlabel("Education Level (1=Below College ... 5=Doctor)")
    plt.ylabel("Number of Employees")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "education_countplot.png"))
    plt.close()

    # 8. Bar Chart - Average Salary by Department
    dept_salary = (
        df.groupby("Department")["MonthlyIncome"].mean()
        .sort_values(ascending=False)
    )
    plt.figure(figsize=(8, 5))
    dept_salary.plot(kind="bar", color="seagreen")
    plt.title("Average Salary by Department")
    plt.xlabel("Department")
    plt.ylabel("Average Monthly Income")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "avg_salary_by_department.png"))
    plt.close()

    # 9. Pie Chart - Business Travel Distribution
    # (used in place of Work Mode, since this dataset has no
    # Remote/Hybrid/Office column)
    travel_counts = df["BusinessTravel"].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(
        travel_counts,
        labels=travel_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Business Travel Distribution")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "business_travel_piechart.png"))
    plt.close()

    # 10. Scatter Plot - Experience vs Salary
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x="TotalWorkingYears", y="MonthlyIncome", hue="Attrition")
    plt.title("Experience vs Salary")
    plt.xlabel("Total Working Years")
    plt.ylabel("Monthly Income")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "experience_vs_salary.png"))
    plt.close()

    # 11. Correlation Heatmap
    numeric_cols = [
        "Age", "MonthlyIncome", "TotalWorkingYears", "YearsAtCompany",
        "PerformanceRating", "JobSatisfaction", "DistanceFromHome",
        "PercentSalaryHike", "YearsSinceLastPromotion", "AttritionFlag"
    ]
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[numeric_cols].corr(), annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "correlation_heatmap.png"))
    plt.close()

    # 12. Pair Plot
    pairplot_cols = ["Age", "MonthlyIncome", "TotalWorkingYears", "PerformanceRating"]
    pairplot_fig = sns.pairplot(df[pairplot_cols])
    pairplot_fig.savefig(os.path.join(output_path, "pairplot.png"))
    plt.close("all")