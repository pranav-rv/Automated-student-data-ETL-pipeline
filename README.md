# Automated Student Data ETL Pipeline

> Python-based automated ETL pipeline for Excel-to-Excel student data transformation, business-rule application, reporting, and automated change monitoring.

---

## 1. Executive Summary

This project demonstrates a Python-based automated ETL (Extract, Transform, Load) solution designed to reduce manual effort in student data processing and reporting.

The pipeline extracts student records from a source Excel workbook, applies predefined business rules to calculate grades and Pass/Fail status, and loads the transformed data into a separate reporting workbook.

The solution also monitors the source Excel file for changes and automatically regenerates the reporting output when updated data is detected.

From a Business Analyst perspective, the project demonstrates how a repetitive manual business process can be analyzed, documented, standardized, automated, tested, and improved using a structured data pipeline.

---

## 2. Business Problem & Objectives

### Business Problem

The existing student reporting process involves manually reviewing student marks, calculating grades, determining Pass/Fail status, and updating a separate reporting workbook.

This manual process can result in:

- Repetitive manual effort
- Calculation errors
- Delayed report updates
- Inconsistent application of business rules
- Dependency on manual intervention
- Difficulty maintaining a consistent reporting process

### Business Objectives

The solution aims to:

1. Automate student data extraction.
2. Standardize grade calculation.
3. Automate Pass/Fail classification.
4. Generate a consistent reporting workbook.
5. Detect changes in the source data.
6. Automatically refresh the report when changes occur.
7. Reduce manual processing effort.
8. Improve consistency and reporting reliability.

---

## 3. Stakeholders

| Stakeholder | Responsibility / Interest |
|---|---|
| Business Analyst | Defines requirements, business rules, process flow, scope, and KPIs |
| Academic / Operations Team | Provides and maintains student data |
| Reporting User | Consumes the generated student report |
| Management | Uses reporting information for monitoring and decision-making |
| Developer / Data Analyst | Implements and maintains the ETL pipeline |

---

## 4. Scope / Out of Scope

### In Scope

- Excel-based student data ingestion
- Data extraction using Python
- Data transformation using Pandas
- Grade calculation
- Pass/Fail classification
- Excel report generation
- Source-file change detection
- Automated report refresh
- Basic execution monitoring
- Git/GitHub version control

### Out of Scope

- Database integration
- Cloud deployment
- User authentication
- Web-based application
- Advanced predictive analytics
- Enterprise workflow orchestration
- Production-grade scheduling infrastructure
- Role-based access control

---

## 5. Business & Functional Requirements

### Business Requirements

| ID | Requirement |
|---|---|
| BR-01 | Student data should be processed consistently |
| BR-02 | Grade calculations should follow predefined business rules |
| BR-03 | Pass/Fail status should be calculated automatically |
| BR-04 | Reports should be generated without repetitive manual calculations |
| BR-05 | Changes in source data should trigger report refresh |
| BR-06 | The solution should reduce manual reporting effort |

### Functional Requirements

| ID | Requirement |
|---|---|
| FR-01 | Read student data from an Excel workbook |
| FR-02 | Process student marks |
| FR-03 | Calculate Grade |
| FR-04 | Calculate Result |
| FR-05 | Generate Student_Report.xlsx |
| FR-06 | Monitor Student_Source.xlsx |
| FR-07 | Re-run the pipeline when source changes are detected |
| FR-08 | Display pipeline execution status |
| FR-09 | Store source and output files in defined project folders |

---

## 6. Source Data Structure

The source workbook contains student-level records.

### Key Fields

| Field | Description |
|---|---|
| Student_ID | Unique student identifier |
| Name | Student name |
| Course | Academic course |
| Marks | Student marks |

### Example

| Student_ID | Name | Course | Marks |
|---:|---|---|---:|
| 153 | Varun | MBA | 76 |
| 154 | Yashwanth | MBA | 80 |
| 155 | Aadarsh | MBA | 24 |

The source workbook is stored under the `data/` directory.

---

## 7. Business Rules

### Grade Calculation

| Marks | Grade |
|---:|---|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |

### Result Calculation

| Marks | Result |
|---:|---|
| 50 or above | Pass |
| Below 50 | Fail |

These business rules are implemented programmatically to ensure consistent application across student records.

### Example

A student with:

```text
Marks = 76

will receive:

Grade = C
Result = Pass

A student with:

Marks = 24

will receive:

Grade = F
Result = Fail
8. Solution Architecture
                 SOURCE
        Student_Source.xlsx
                  |
                  v
             EXTRACT
                  |
                  v
        Python + Pandas
                  |
                  v
             TRANSFORM
          /               \
     Grade Rule        Result Rule
          \               /
                  |
                  v
                LOAD
                  |
                  v
        Student_Report.xlsx
                  |
                  v
        Change Monitoring
                  |
                  v
          Source updated?
             /       \
           No         Yes
           |           |
        Continue    Re-run ETL
Architecture Components

Source Layer

data/Student_Source.xlsx

Contains the original student records.

Processing Layer

src/Student_Data_Pipeline.py

Contains the Python ETL logic.

Output Layer

output/Student_Report.xlsx

Contains the transformed reporting data.

Monitoring Layer

The pipeline monitors the source workbook and re-runs the ETL process when a change is detected.

9. End-to-End Process Flow
Source Excel file is created or updated.
Pipeline identifies the source file.
Student records are extracted.
Data is processed using Pandas.
Grade business rules are applied.
Pass/Fail rules are applied.
Transformed data is loaded into the reporting workbook.
Pipeline displays execution status.
Source file is monitored for future changes.
When a change is detected, the pipeline automatically regenerates the report.
Process Flow
Source Excel
     |
     v
Extract Data
     |
     v
Validate / Process
     |
     v
Apply Grade Rule
     |
     v
Apply Result Rule
     |
     v
Generate Report
     |
     v
Monitor Source
     |
     +----------------------+
     |                      |
 No Change              Change Detected
     |                      |
 Continue              Re-run Pipeline
                            |
                            v
                     Updated Report
10. Technical Implementation
Technology Stack
Python
Pandas
OpenPyXL
Excel
pathlib
time
Git
GitHub
Project Path Handling

The project uses relative paths through Python's pathlib library rather than machine-specific file paths.

Example:

BASE_DIR = Path(__file__).resolve().parent.parent

SOURCE_FILE = BASE_DIR / "data" / "Student_Source.xlsx"

OUTPUT_FILE = BASE_DIR / "output" / "Student_Report.xlsx"

This makes the project more portable across development environments.

Data Extraction
df = pd.read_excel(SOURCE_FILE)
Grade Transformation
df["Grade"] = df["Marks"].apply(calculate_grade)
Result Transformation
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)
Report Generation
df.to_excel(OUTPUT_FILE, index=False)
Change Monitoring

The pipeline compares the source file's modification state and detects when the source workbook has been updated.

When a change is detected, the ETL workflow is executed again and a refreshed report is generated.

11. Development Journey

The project was developed incrementally to demonstrate the transition from a manual process to an automated workflow.

Phase 1 — Manual Data Processing

Student data was initially processed using Excel-based calculations.

The process required manual effort to:

Review student marks
Calculate grades
Determine Pass/Fail status
Update the reporting workbook
Phase 2 — Python Transformation

Python and Pandas were introduced to automate:

Data extraction
Grade calculation
Pass/Fail classification
Report generation
Phase 3 — ETL Pipeline

The transformation logic was structured into an ETL workflow consisting of:

Extract → Transform → Load
Phase 4 — Automation

Source-file change detection was added so that the pipeline could automatically refresh the reporting output when source data changed.

Phase 5 — Portfolio Engineering

The project was organized into a professional repository structure:

Automated-student-data-ETL-pipeline/
│
├── data/
├── output/
├── src/
├── README.md
├── requirements.txt
└── .gitignore

The project was then version-controlled using Git and published to GitHub.

12. Testing Strategy & Results

Testing was performed to verify that the pipeline correctly applies business rules and generates the expected output.

Test Case 1 — Grade A
Input Marks = 95
Expected Grade = A
Expected Result = Pass
Test Case 2 — Grade B
Input Marks = 85
Expected Grade = B
Expected Result = Pass
Test Case 3 — Grade C
Input Marks = 75
Expected Grade = C
Expected Result = Pass
Test Case 4 — Grade D
Input Marks = 65
Expected Grade = D
Expected Result = Pass
Test Case 5 — Fail Scenario
Input Marks = 24
Expected Grade = F
Expected Result = Fail
Test Case Summary
Marks	Expected Grade	Expected Result
95	A	Pass
85	B	Pass
75	C	Pass
65	D	Pass
24	F	Fail
Automation Test

A source record was changed from:

Marks = 78

to:

Marks = 24

The pipeline detected the source change and regenerated the reporting workbook.

Expected output:

Marks = 24
Grade = F
Result = Fail
Testing Result

The test confirmed that the ETL pipeline correctly:

Detected source changes
Extracted updated data
Applied business rules
Generated the updated report
Reflected the updated Grade and Result
13. Before / After Scenario
Before Automation
Open Excel
     |
     v
Review student marks
     |
     v
Calculate Grade manually
     |
     v
Calculate Pass/Fail manually
     |
     v
Update reporting workbook
     |
     v
Repeat whenever data changes
After Automation
Update Source Excel
        |
        v
Pipeline detects change
        |
        v
Python extracts data
        |
        v
Business rules applied
        |
        v
Report automatically regenerated
Process Improvement
Before	After
Manual calculations	Automated calculations
Manual report updates	Automated report generation
Repetitive effort	Reduced manual effort
Higher error risk	Consistent business rules
Reactive process	Change-triggered process
14. Current-State vs Future-State Process
Current-State Process
Student Data
     |
     v
Manual Excel Review
     |
     v
Manual Grade Calculation
     |
     v
Manual Result Calculation
     |
     v
Manual Report Update
     |
     v
Final Report
Future-State Process
Student Data
     |
     v
Automated Extraction
     |
     v
Business Rule Processing
     |
     +------------------+
     |                  |
 Grade Calculation   Result Calculation
     |                  |
     +--------+---------+
              |
              v
      Automated Report
              |
              v
       Change Monitoring
              |
              v
       Automatic Refresh
State Comparison
Current-State	Future-State
Manual data processing	Automated processing
Manual grade calculation	Rule-based calculation
Manual Pass/Fail calculation	Automated classification
Manual report updates	Automated report generation
Higher dependency on users	Reduced manual intervention
Greater risk of calculation errors	Consistent business rules
Reactive reporting	Change-triggered reporting
15. Business Value

The solution provides business value by:

Reducing repetitive manual work
Improving calculation consistency
Reducing human error
Improving reporting turnaround time
Standardizing business rules
Improving data-processing transparency
Providing a repeatable reporting process
Improving operational efficiency
Business Analyst Perspective

The project demonstrates the ability to:

Identify Business Problem
        ↓
Gather Requirements
        ↓
Define Business Rules
        ↓
Analyze Current-State Process
        ↓
Design Future-State Process
        ↓
Define Solution
        ↓
Implement Automation
        ↓
Test Solution
        ↓
Measure Business Value

This demonstrates both business analysis and technical problem-solving capabilities.

16. Risks & Mitigations
Risk	Potential Impact	Mitigation
Incorrect source data	Incorrect report	Data validation
Excel file locked	Report generation failure	File-access handling
Invalid marks	Incorrect classification	Data quality rules
File path changes	Pipeline failure	Relative project paths
Unexpected source structure	Processing failure	Schema validation
Duplicate records	Reporting inaccuracies	Duplicate checks
Missing values	Incorrect output	Missing-value validation
Pipeline failure	Delayed reporting	Execution monitoring and error handling
17. Data Quality Controls

The solution can use the following data-quality controls:

Completeness
Check for missing Student_ID
Check for missing Name
Check for missing Course
Check for missing Marks
Validity
Validate Marks between 0 and 100
Validate expected column names
Validate data types
Uniqueness
Identify duplicate Student_ID values
Accuracy
Validate Grade against Marks
Validate Result against the defined Pass/Fail rule
Availability
Confirm that the source workbook exists before processing
Confirm that the output workbook is successfully generated
Data Quality Framework
Source Data
    |
    v
Completeness Check
    |
    v
Validity Check
    |
    v
Uniqueness Check
    |
    v
Business Rule Validation
    |
    v
ETL Processing
    |
    v
Output Validation
18. Monitoring & Logging

The pipeline provides execution messages to give basic operational visibility.

Example:

Running Student Data ETL Pipeline...
Source data extracted successfully.
Business rules applied successfully.
Report generated successfully.
Output file: /output/Student_Report.xlsx
Pipeline completed.
Change Monitoring

The pipeline also monitors the source Excel file.

When a change is detected:

Change detected in Student_Source.xlsx!
Running Student Data ETL Pipeline...
Source data extracted successfully.
Business rules applied successfully.
Report generated successfully.
Pipeline completed.
Current Monitoring Approach

The current implementation uses console-based status messages.

Future Monitoring Approach

The monitoring capability can be extended using:

Structured logs
Error logs
Execution timestamps
Pipeline status dashboards
Email notifications
Cloud monitoring
19. Limitations

Current limitations include:

Excel is used as both source and destination.
No centralized database is used.
No enterprise scheduler is implemented.
No Power BI dashboard is included.
Logging is currently console-based.
Authentication is not implemented.
Role-based access control is not implemented.
The solution is intended as a portfolio/demo project rather than a production enterprise system.
The current monitoring mechanism is suitable for demonstration purposes and can be strengthened for production use.
20. Future Enhancements

Potential future improvements include:

Database integration using SQL.
Power BI dashboard integration.
Automated email notifications.
Structured logging.
Advanced error-handling framework.
Comprehensive data validation framework.
Cloud deployment.
Scheduled execution.
Pipeline orchestration using Apache Airflow or similar tools.
CI/CD integration using GitHub Actions.
Automated data-quality reports.
Business KPI dashboard.
Database-based source and destination systems.
Role-based access control.
Pipeline performance monitoring.
Automated unit and integration testing.
Future Architecture
Excel / Database
       |
       v
   ETL Pipeline
       |
       v
Data Quality Layer
       |
       v
Centralized Database
       |
       v
Power BI Dashboard
       |
       v
Business Users
21. Suggested KPIs & Assumptions
Suggested KPIs
KPI	Purpose
Pipeline Success Rate	Measures successful pipeline executions
Report Refresh Time	Measures processing efficiency
Data Quality Error Rate	Measures source-data quality
Manual Processing Time Saved	Measures automation benefit
Report Generation Success Rate	Measures pipeline reliability
Change Detection Success Rate	Measures monitoring effectiveness
Data Processing Volume	Measures records processed per execution
KPI Formulas
Pipeline Success Rate
Successful Executions / Total Executions × 100
Data Quality Error Rate
Invalid Records / Total Records × 100
Manual Processing Time Saved
Manual Processing Time - Automated Processing Time
Assumptions
Marks are numeric.
Marks are expected to fall between 0 and 100.
Student_ID is expected to uniquely identify students.
Source Excel structure remains consistent.
Grade and Pass/Fail rules are business-approved.
Users maintain the source workbook correctly.
The source workbook is accessible when the pipeline executes.
22. Conclusion

The Automated Student Data ETL Pipeline demonstrates how a repetitive Excel-based business process can be transformed into a structured and automated data workflow.

The solution combines Business Analysis concepts with technical implementation by translating business requirements and rules into a Python-based ETL pipeline.

The project demonstrates practical skills in:

Business process analysis
Requirements definition
Business-rule modelling
Current-State analysis
Future-State design
ETL design
Data transformation
Python and Pandas
Excel automation
Testing
Data quality
Monitoring
Git/GitHub
Process improvement

The project provides a foundation that can be extended toward SQL, Power BI, cloud platforms, workflow orchestration, CI/CD, and enterprise-grade data pipelines.

23. Portfolio Evidence Checklist
Business Analysis
 Business problem identified
 Business objectives defined
 Stakeholders identified
 Scope defined
 Out-of-scope items defined
 Business requirements documented
 Functional requirements documented
 Business rules documented
 Current-State process documented
 Future-State process documented
 Business value identified
 Risks and mitigations documented
 Suggested KPIs documented
Technical
 Python ETL pipeline
 Pandas transformation
 Excel extraction
 Excel report generation
 Automated change detection
 Relative project paths
 requirements.txt
 .gitignore
 Git version control
 GitHub repository
Testing
 Grade-rule testing
 Pass/Fail testing
 Source-change testing
 Output validation
 End-to-end pipeline testing
Data Quality
 Missing-value considerations
 Data-type validation considerations
 Range validation
 Duplicate checks
 Business-rule validation
 Output validation
Portfolio Artifacts
 Source dataset
 Generated report
 Python source code
 requirements.txt
 .gitignore
 Project documentation
 GitHub repository
Project Structure
Automated-student-data-ETL-pipeline/
│
├── data/
│   └── Student_Source.xlsx
│
├── output/
│   └── Student_Report.xlsx
│
├── src/
│   └── Student_Data_Pipeline.py
│
├── .gitignore
├── README.md
└── requirements.txt
Folder Description
Folder / File	Purpose
data/	Contains the source Excel workbook
output/	Contains the generated reporting workbook
src/	Contains the Python ETL pipeline
.gitignore	Defines files and folders excluded from version control
README.md	Contains complete project documentation
requirements.txt	Lists Python dependencies

Author

**❤️ Pranav Krishna R V ❤️**

MBA | Business Analytics / Business Analyst Portfolio

GitHub: pranav-rv

Disclaimer

This project is created for educational and portfolio demonstration purposes.

The student dataset and business rules are illustrative and do not represent a real institutional student information system.

The solution is intended to demonstrate Business Analysis, ETL, Python, data transformation, automation, testing, and reporting concepts.

