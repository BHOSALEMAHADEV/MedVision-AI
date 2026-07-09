import sqlite3
import os

# ==========================================================
# Create Database Folder
# ==========================================================

os.makedirs("database", exist_ok=True)

# ==========================================================
# Connect to Database
# ==========================================================

connection = sqlite3.connect(
    "database/medvision.db",
    check_same_thread=False
)

cursor = connection.cursor()

# ==========================================================
# USERS TABLE
# ==========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL,

    role TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

# ==========================================================
# PATIENTS TABLE
# ==========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    patient_id TEXT UNIQUE NOT NULL,

    full_name TEXT NOT NULL,

    age INTEGER,

    gender TEXT,

    phone TEXT,

    email TEXT,

    blood_group TEXT,

    address TEXT,

    medical_history TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

# ==========================================================
# UPLOADS TABLE
# ==========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS uploads(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    patient_id TEXT NOT NULL,

    module TEXT NOT NULL,

    image_name TEXT NOT NULL,

    image_path TEXT NOT NULL,

    image_size REAL,

    image_format TEXT,

    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

# ==========================================================
# REPORTS TABLE
# ==========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS reports(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    patient_id TEXT NOT NULL,

    module TEXT NOT NULL,

    image_name TEXT,

    prediction TEXT,

    confidence REAL,

    report_path TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

# ==========================================================
# ANALYSIS TABLE
# ==========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS analysis(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    patient_id TEXT,

    module TEXT,

    model_name TEXT,

    prediction TEXT,

    confidence REAL,

    processing_time REAL,

    analyzed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

# ==========================================================
# SETTINGS TABLE
# ==========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS settings(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    theme TEXT DEFAULT 'Light',

    language TEXT DEFAULT 'English'

)
""")

# ==========================================================
# DEFAULT USER
# ==========================================================

cursor.execute(
    """
    SELECT *
    FROM users
    WHERE username=?
    """,
    ("admin",)
)

user = cursor.fetchone()

if user is None:

    cursor.execute(
        """
        INSERT INTO users(
            username,
            password,
            role
        )
        VALUES(?,?,?)
        """,
        (
            "admin",
            "admin123",
            "Medical Professional"
        )
    )

# ==========================================================
# SAVE DATABASE
# ==========================================================

connection.commit()