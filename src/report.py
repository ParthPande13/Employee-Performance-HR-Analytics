import os

from reportlab.lib.pagesizes import A4

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.units import inch


def create_report(
        analysis,
        df,
        graph_path,
        report_path
):

    documents = SimpleDocTemplate(
        report_path,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    story = []

    # ---------------- Title ----------------
    story.append(
        Paragraph("Employee Performance & HR Analytics Report", styles["Title"])
    )
    story.append(Spacer(1, 20))

    # ---------------- Dataset Overview ----------------
    story.append(
        Paragraph("Dataset Overview", styles["Heading2"])
    )
    story.append(Spacer(1, 8))

    total_rows = df.shape[0]
    total_columns = df.shape[1]
    department_list = ", ".join(df["Department"].unique())

    story.append(
        Paragraph(f"Total Records: {total_rows}", styles["Normal"])
    )
    story.append(
        Paragraph(f"Total Columns: {total_columns}", styles["Normal"])
    )
    story.append(
        Paragraph(f"Departments: {department_list}", styles["Normal"])
    )
    story.append(Spacer(1, 20))

    # ---------------- Data Cleaning Summary ----------------
    story.append(
        Paragraph("Data Cleaning Summary", styles["Heading2"])
    )
    story.append(Spacer(1, 8))

    cleaning_text = (
        "Duplicate records were removed, text columns were standardized, "
        "numeric columns were validated, and missing values were filled "
        "using the column median. Rows with invalid values (such as "
        "non-positive age or salary) were removed."
    )

    story.append(
        Paragraph(cleaning_text, styles["Normal"])
    )
    story.append(Spacer(1, 20))

    # ---------------- Statistical Summary ----------------
    story.append(
        Paragraph("Statistical Summary", styles["Heading2"])
    )
    story.append(Spacer(1, 8))

    story.append(
        Paragraph(f"Average Age: {round(df['Age'].mean(), 2)}", styles["Normal"])
    )
    story.append(
        Paragraph(f"Average Monthly Income: {round(df['MonthlyIncome'].mean(), 2)}", styles["Normal"])
    )
    story.append(
        Paragraph(f"Average Working Years: {round(df['TotalWorkingYears'].mean(), 2)}", styles["Normal"])
    )
    story.append(
        Paragraph(f"Average Performance Rating: {round(df['PerformanceRating'].mean(), 2)}", styles["Normal"])
    )
    story.append(Spacer(1, 20))

    story.append(PageBreak())

    # ---------------- Visualizations ----------------
    story.append(
        Paragraph("Visualizations", styles["Heading2"])
    )
    story.append(Spacer(1, 10))

    chart_files = sorted(os.listdir(graph_path))

    for chart_file in chart_files:
        if chart_file.endswith(".png"):

            image_path = os.path.join(graph_path, chart_file)

            story.append(
                Image(image_path, width=5.5 * inch, height=3.5 * inch)
            )
            story.append(Spacer(1, 15))

    story.append(PageBreak())

    # ---------------- Business Insights ----------------
    story.append(
        Paragraph("Business Insights", styles["Heading2"])
    )
    story.append(Spacer(1, 10))

    for key, value in analysis.items():

        if isinstance(value, float):
            value = round(value, 2)

        text = f"<b>{key}:</b> {value}"

        story.append(
            Paragraph(text, styles["Normal"])
        )
        story.append(Spacer(1, 8))

    story.append(Spacer(1, 10))

    # ---------------- Conclusion ----------------
    story.append(
        Paragraph("Conclusion", styles["Heading2"])
    )
    story.append(Spacer(1, 8))

    conclusion_text = (
        "The analysis highlights key drivers of employee salary, "
        "performance, and attrition across departments. These insights "
        "can help the HR department improve retention, address "
        "compensation gaps, and support promotion decisions."
    )

    story.append(
        Paragraph(conclusion_text, styles["Normal"])
    )

    documents.build(story)