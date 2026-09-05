import csv
import random
from datetime import datetime, timedelta


random.seed(42)


departments = {
    "General Medicine": 12000,
    "Cardiology": 25000,
    "Pediatrics": 15000,
    "Dermatology": 18000,
    "Orthopedics": 22000,
}


branches = [
    "Lekki",
    "Ikeja",
    "Victoria Island",
]


visit_types = [
    "Consultation",
    "Follow-up",
    "Routine Check",
]


visit_statuses = [
    "Completed",
    "Completed",
    "Completed",
    "Completed",
    "Cancelled",
    "Pending",
]


start_date = datetime(2026, 1, 1)

rows = []


for i in range(1, 501):

    department = random.choice(list(departments.keys()))

    visit_id = f"V{i:04d}"
    patient_id = f"P{random.randint(1, 180):04d}"
    doctor_id = f"D{random.randint(1, 30):03d}"

    visit_type = random.choice(visit_types)
    branch = random.choice(branches)
    visit_status = random.choice(visit_statuses)

    visit_date = start_date + timedelta(
        days=random.randint(0, 179)
    )

    consultation_fee = departments[department]

    rows.append([
        visit_id,
        patient_id,
        department,
        doctor_id,
        visit_type,
        visit_date.strftime("%Y-%m-%d"),
        consultation_fee,
        visit_status,
        branch,
    ])

    with open(
        "data/hospital_visits.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "visit_id",
            "patient_id",
            "department",
            "doctor_id",
            "visit_type",
            "visit_date",
            "consultation_fee",
            "visit_status",
            "branch",
        ])

        writer.writerows(rows)

        print("CareBridge dataset created successfully.")
        print("Number of records:", len(rows))