# Employee Performance & HR Analytics

An end-to-end HR analytics pipeline built with **Python, MySQL, and Power BI**.
The project analyzes employee performance, salary distribution, department
productivity, education level, and attrition to help HR make data-driven
decisions.



## Overview

This project takes the raw IBM HR Analytics Employee Attrition dataset and
runs it through a complete analytics pipeline:

**CSV → Clean → Transform → MySQL → SQL Analysis → Pandas EDA → Visualizations → PDF Report → Power BI Dashboard**

Everything is modular — each stage of the pipeline lives in its own file
under `src/`, and `main.py` runs them all in sequence.



## Dataset

- **Source:** Kaggle — IBM HR Analytics Employee Attrition & Performance
- **File:** `WA_Fn-UseC_-HR-Employee-Attrition.csv` (renamed to `hr_raw.csv`)
- **Size:** 1,470 employee records, 35 columns
- **Quality:** No missing values, no duplicates in the original file

### Note on "Work Mode"
The project brief calls for a Remote/Hybrid/Office "Work Mode" analysis, but
this dataset has no such column. **`BusinessTravel`** (Non-Travel /
Travel_Rarely / Travel_Frequently) is used as the closest available
real-world substitute wherever "Work Mode" appears in tasks, charts, or the
dashboard. This is called out explicitly rather than inventing fake data.

### Note on Performance Rating
`PerformanceRating` in this dataset only contains two values (3 and 4), not
a full 1–5 scale — so performance-related analysis reflects that binary
split rather than a wide distribution.


---

## Setup

### 1. Create the MySQL database
In MySQL Workbench (or CLI), run once:
```sql
CREATE DATABASE IF NOT EXISTS hr_analytics;
```

### 2. Configure credentials
Open `src/config.py` and update the MySQL section with your own credentials:
```python
MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'your_password_here'
MYSQL_DATABASE = 'hr_analytics'
```

### 3. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Add the dataset
Place the dataset at `data/raw/hr_raw.csv`.

---

## Running the Pipeline

```bash
python main.py
```

This single command will, in order:

1. Load the raw CSV
2. Clean the data (remove duplicates, fix types, handle missing values, drop invalid rows)
3. Save the cleaned dataset to `data/processed/hr_cleaned.csv`
4. Add derived columns (`AnnualIncome`, `SalaryBand`, `ExperienceGroup`, `AttritionFlag`)
5. Connect to MySQL and load the data into an `employees` table
6. Run all 10 required SQL tasks and save results (query + output) to a text file
7. Compute business insights / KPIs with Pandas
8. Save business insights to a text file
9. Generate all 12 required visualizations as PNGs
10. Assemble the final PDF report (overview, cleaning summary, statistics, charts, insights, conclusion)



## SQL Tasks Covered

1. Total employees by department
2. Average salary by department
3. Top 10 highest-paid employees
4. Average years of experience by department
5. Employees with the highest performance rating
6. Employee count by Business Travel pattern (Work Mode substitute)
7. Departments with the highest attrition rate
8. Salary rank within department (window function — `RANK() OVER`)
9. Employees earning above the company average salary (subquery)
10. Gender-wise employee distribution



## Visualizations Covered

Salary histogram · Age histogram · Salary box plot · Experience box plot ·
Department count plot · Gender count plot · Education count plot ·
Average salary by department (bar) · Business travel distribution (pie) ·
Experience vs. salary (scatter) · Correlation heatmap · Pair plot


## Power BI Dashboard

Two pages covering all required sections:

**Page 1 — Executive Overview**
KPI cards (Total Employees, Average Salary, Average Performance, Attrition
Rate, Total Departments), Employees by Department, Gender Distribution,
Education Analysis, Age Distribution — with slicers for Department, Gender,
Job Role, Education Field, and Over Time.

**Page 2 — Performance & Workforce**
KPI cards (Average Performance, Average Salary, Overtime Employees,
Attrition Rate), Performance by Department, Performance Distribution,
Attrition by Department, Salary vs. Experience (scatter).

### KPI Cards
Total Employees · Average Salary · Highest Salary · Average Experience ·
Attrition Rate · Average Performance Rating



## Tech Stack

- **Python** — pandas, numpy, matplotlib, seaborn, reportlab
- **MySQL** — SQLAlchemy + mysql-connector-python
- **Power BI** — interactive dashboard



## License

This project's code is licensed under the MIT License. The dataset used
(IBM HR Analytics Employee Attrition & Performance) is sourced from Kaggle
and is subject to its own terms — see the original dataset page for details.



## Author's Note

This project was built end-to-end as a learning exercise — every module was
written and understood individually (config → loading → cleaning →
transformation → MySQL connection → SQL queries → analysis → visualization
→ reporting → orchestration) rather than generated as one block, in order
to genuinely understand each stage of a real analytics pipeline.


