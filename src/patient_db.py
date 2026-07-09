import sqlite3
import uuid

# ======================================================
# Database Connection
# ======================================================

connection = sqlite3.connect(
    "database/medvision.db",
    check_same_thread=False
)

cursor = connection.cursor()

# ======================================================
# Generate Patient ID
# ======================================================

def generate_patient_id():
    return "PAT-" + str(uuid.uuid4())[:8].upper()

# ======================================================
# Add Patient
# ======================================================

def add_patient(
    name,
    age,
    gender,
    phone,
    email,
    blood_group,
    address,
    medical_history
):

    patient_id = generate_patient_id()

    cursor.execute(
        """
        INSERT INTO patients(
            patient_id,
            full_name,
            age,
            gender,
            phone,
            email,
            blood_group,
            address,
            medical_history
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            patient_id,
            name,
            age,
            gender,
            phone,
            email,
            blood_group,
            address,
            medical_history
        )
    )

    connection.commit()

    return patient_id

# ======================================================
# Get All Patients
# ======================================================

def get_all_patients():

    cursor.execute("""
        SELECT
            patient_id,
            full_name,
            age,
            gender,
            phone,
            email,
            blood_group
        FROM patients
        ORDER BY id DESC
    """)

    return cursor.fetchall()

# ======================================================
# Search Patient
# ======================================================

def search_patient(keyword):

    cursor.execute(
        """
        SELECT
            patient_id,
            full_name,
            age,
            gender,
            phone,
            email,
            blood_group
        FROM patients
        WHERE
            full_name LIKE ?
            OR patient_id LIKE ?
        ORDER BY id DESC
        """,
        (
            "%" + keyword + "%",
            "%" + keyword + "%"
        )
    )

    return cursor.fetchall()

# ======================================================
# Get Patient By Patient ID
# ======================================================

def get_patient(patient_id):

    cursor.execute(
        """
        SELECT
            patient_id,
            full_name,
            age,
            gender,
            phone,
            email,
            blood_group,
            address,
            medical_history
        FROM patients
        WHERE patient_id=?
        """,
        (patient_id,)
    )

    return cursor.fetchone()

# ======================================================
# Update Patient
# ======================================================

def update_patient(
    patient_id,
    name,
    age,
    gender,
    phone,
    email,
    blood_group,
    address,
    medical_history
):

    cursor.execute(
        """
        UPDATE patients
        SET
            full_name=?,
            age=?,
            gender=?,
            phone=?,
            email=?,
            blood_group=?,
            address=?,
            medical_history=?
        WHERE patient_id=?
        """,
        (
            name,
            age,
            gender,
            phone,
            email,
            blood_group,
            address,
            medical_history,
            patient_id
        )
    )

    connection.commit()

# ======================================================
# Delete Patient
# ======================================================

def delete_patient(patient_id):

    cursor.execute(
        """
        DELETE FROM patients
        WHERE patient_id=?
        """,
        (patient_id,)
    )

    connection.commit()

# ======================================================
# Get Total Patients
# ======================================================

def get_total_patients():

    cursor.execute("SELECT COUNT(*) FROM patients")

    return cursor.fetchone()[0]

# ======================================================
# Get Gender Statistics
# ======================================================

def get_gender_statistics():

    cursor.execute("""
        SELECT gender, COUNT(*)
        FROM patients
        GROUP BY gender
    """)

    return cursor.fetchall()

# ======================================================
# Get Patient IDs
# ======================================================

def get_patient_ids():

    cursor.execute(
        """
        SELECT
            patient_id,
            full_name
        FROM patients
        ORDER BY full_name ASC
        """
    )

    return cursor.fetchall()