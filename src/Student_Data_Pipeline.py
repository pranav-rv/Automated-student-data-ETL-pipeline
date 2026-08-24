import time
from pathlib import Path

import pandas as pd


# ---------------------------------------------------------
# PROJECT PATHS
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

SOURCE_FILE = BASE_DIR / "data" / "Student_Source.xlsx"
OUTPUT_FILE = BASE_DIR / "output" / "Student_Report.xlsx"


# ---------------------------------------------------------
# GRADE BUSINESS RULE
# ---------------------------------------------------------

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


# ---------------------------------------------------------
# ETL PIPELINE
# ---------------------------------------------------------

def run_pipeline():

    print("Running Student Data ETL Pipeline...")

    # -------------------------
    # 1. EXTRACT
    # -------------------------

    df = pd.read_excel(SOURCE_FILE)

    print("Source data extracted successfully.")

    # -------------------------
    # 2. TRANSFORM
    # -------------------------

    df["Grade"] = df["Marks"].apply(calculate_grade)

    df["Result"] = df["Marks"].apply(
        lambda x: "Pass" if x >= 50 else "Fail"
    )

    print("Business rules applied successfully.")

    # -------------------------
    # 3. LOAD
    # -------------------------

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    df.to_excel(OUTPUT_FILE, index=False)

    print("Report generated successfully!")
    print(f"Output file: {OUTPUT_FILE}")

    print("\nPipeline completed.\n")


# ---------------------------------------------------------
# INITIAL PIPELINE RUN
# ---------------------------------------------------------

run_pipeline()


# ---------------------------------------------------------
# AUTOMATIC CHANGE MONITORING
# ---------------------------------------------------------

print("Pipeline is running.")
print("Watching Student_Source.xlsx for changes...")
print("Press Ctrl+C to stop.\n")


last_modified = SOURCE_FILE.stat().st_mtime

start_time = time.time()

# Run for 1 hour
RUN_DURATION = 60 * 60


while time.time() - start_time < RUN_DURATION:

    time.sleep(2)

    try:
        current_modified = SOURCE_FILE.stat().st_mtime

        if current_modified != last_modified:

            print("\nChange detected in Student_Source.xlsx!")

            # Wait briefly for Excel to finish saving
            time.sleep(2)

            try:
                run_pipeline()

                last_modified = current_modified

            except PermissionError:

                print(
                    "Excel is still saving the file. "
                    "Waiting before retrying..."
                )

    except FileNotFoundError:

        print("Source Excel file not found.")

print("1 hour completed. Pipeline stopped.")