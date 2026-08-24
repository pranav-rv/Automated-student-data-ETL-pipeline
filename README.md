# Automated-student-data-ETL-pipeline
Python-based automated ETL pipeline for Excel-to-Excel student data synchronization and reporting.
# Automated Student Data ETL Pipeline

## 📌 Project Overview

This project demonstrates a Python-based automated ETL (Extract, Transform, Load) pipeline that connects two Excel-based applications.

The pipeline extracts student data from a source Excel workbook, applies predefined business rules to calculate Grade and Pass/Fail status, and loads the transformed data into a separate reporting workbook.

The pipeline also monitors the source file for changes and automatically refreshes the reporting output when new changes are detected.

---

## 🎯 Business Problem

In a traditional manual reporting process, users need to:

1. Update student marks.
2. Calculate grades.
3. Determine Pass/Fail status.
4. Copy or transfer the updated data into a reporting workbook.
5. Repeat the process whenever the source data changes.

This creates unnecessary manual effort and increases the risk of:

- Data-entry errors
- Incorrect calculations
- Outdated reports
- Repetitive work
- Inconsistent business rules

---

## 💡 Solution

A lightweight Python ETL pipeline was developed to automate the process.

```text
Student_Source.xlsx
        ↓
      Extract
        ↓
      Pandas
        ↓
     Transform
        ↓
 Grade + Pass/Fail
        ↓
       Load
        ↓
Student_Report.xlsx