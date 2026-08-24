# Automated Student Data ETL Pipeline

> Python-based ETL automation for Excel-to-Excel student data processing, business-rule transformation, and automated reporting.

---

## 📌 1. Project Overview

This project demonstrates a Python-based automated ETL (Extract, Transform, Load) pipeline designed to automate a manual student reporting process.

The solution extracts student data from a source Excel workbook, applies predefined business rules to calculate Grade and Pass/Fail status, and loads the transformed data into a separate reporting workbook.

The pipeline also monitors the source Excel file for changes and automatically refreshes the reporting output when the source data is updated.

---

## 🎯 2. Business Problem

The original process required users to manually:

1. Update student marks in Excel.
2. Calculate grades.
3. Determine Pass/Fail status.
4. Transfer updated information to a reporting workbook.
5. Repeat the process whenever the source data changed.

This created:

- Repetitive manual work
- Risk of calculation errors
- Copy-paste dependency
- Delayed reporting
- Inconsistent application of business rules

### Business Objective

Automate the data processing and reporting workflow while maintaining consistent business rules and reducing manual intervention.

---

## 💡 3. Proposed Solution

A Python-based ETL pipeline was developed to automate the complete workflow.

```text
Student_Source.xlsx
        │
        ▼
     EXTRACT
        │
        ▼
   Python / Pandas
        │
        ▼
    TRANSFORM
   ┌───────────────┐
   │ Grade         │
   │ Pass / Fail   │
   └───────────────┘
        │
        ▼
      LOAD
        │
        ▼
Student_Report.xlsx