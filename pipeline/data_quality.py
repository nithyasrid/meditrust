import pandas as pd
from pathlib import Path

INPUT = Path(__file__).parent.parent / "data/raw/patients.csv"

REQUIRED = ["patient_id", "full_name", "date_of_birth", "gender",
            "phone", "insurance_id", "admission_date"]

def run():
    df = pd.read_csv(INPUT)
    issues = []

    duplicate_mask = df.duplicated("patient_id", keep=False)
    for idx in df.index[duplicate_mask]:
        issues.append((idx, "DUPLICATE_PATIENT", "patient_id already exists"))

    for idx, row in df.iterrows():
        for col in REQUIRED:
            if pd.isna(row[col]) or str(row[col]).strip() == "":
                issues.append((idx, "MISSING_VALUE", f"{col} is missing"))

        if pd.notna(row["date_of_birth"]):
            dob = pd.to_datetime(row["date_of_birth"], errors="coerce")
            if pd.isna(dob):
                issues.append((idx, "INVALID_DATE", "invalid date_of_birth"))

        if pd.notna(row["admission_date"]):
            adm = pd.to_datetime(row["admission_date"], errors="coerce")
            if pd.isna(adm):
                issues.append((idx, "INVALID_DATE", "invalid admission_date"))

        phone = str(row["phone"]) if pd.notna(row["phone"]) else ""
        if phone and (not phone.isdigit() or len(phone) != 10):
            issues.append((idx, "INVALID_PHONE", "phone must contain 10 digits"))

    total = len(df)
    bad_rows = len(set(x[0] for x in issues))
    score = round(max(0, (total - bad_rows) / total * 100), 2) if total else 0

    print("=== MediTrust Data Quality Report ===")
    print(f"Rows processed : {total}")
    print(f"Rows with issues: {bad_rows}")
    print(f"Quality score  : {score}%")
    print("\nIssues:")
    for issue in issues:
        print(f"row={issue[0] + 2} | {issue[1]} | {issue[2]}")

    output = Path(__file__).parent.parent / "data/processed/quality_report.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(issues, columns=["row", "issue_type", "details"]).to_csv(output, index=False)
    print(f"\nReport written to: {output}")

if __name__ == "__main__":
    run()
