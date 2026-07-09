import sqlite3

# ======================================================
# Database Connection
# ======================================================

connection = sqlite3.connect(
    "database/medvision.db",
    check_same_thread=False
)

cursor = connection.cursor()

# ======================================================
# Save Upload
# ======================================================

def save_upload(
    patient_id,
    module,
    image_name,
    image_path,
    image_size,
    image_format
):

    cursor.execute(
        """
        INSERT INTO uploads(
            patient_id,
            module,
            image_name,
            image_path,
            image_size,
            image_format
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            patient_id,
            module,
            image_name,
            image_path,
            image_size,
            image_format
        )
    )

    connection.commit()


# ======================================================
# Get All Uploads
# ======================================================

def get_uploads():

    cursor.execute(
        """
        SELECT
            id,
            patient_id,
            module,
            image_name,
            image_size,
            image_format,
            uploaded_at
        FROM uploads
        ORDER BY uploaded_at DESC
        """
    )

    return cursor.fetchall()


# ======================================================
# Search Uploads
# ======================================================

def search_uploads(keyword):

    cursor.execute(
        """
        SELECT
            id,
            patient_id,
            module,
            image_name,
            image_size,
            image_format,
            uploaded_at
        FROM uploads
        WHERE
            patient_id LIKE ?
            OR module LIKE ?
            OR image_name LIKE ?
        ORDER BY uploaded_at DESC
        """,
        (
            "%" + keyword + "%",
            "%" + keyword + "%",
            "%" + keyword + "%"
        )
    )

    return cursor.fetchall()


# ======================================================
# Get Upload by ID
# ======================================================

def get_upload(upload_id):

    cursor.execute(
        """
        SELECT
            id,
            patient_id,
            module,
            image_name,
            image_path,
            image_size,
            image_format,
            uploaded_at
        FROM uploads
        WHERE id=?
        """,
        (upload_id,)
    )

    return cursor.fetchone()


# ======================================================
# Delete Upload
# ======================================================

def delete_upload(upload_id):

    cursor.execute(
        """
        DELETE FROM uploads
        WHERE id=?
        """,
        (upload_id,)
    )

    connection.commit()


# ======================================================
# Total Uploads
# ======================================================

def get_total_uploads():

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM uploads
        """
    )

    return cursor.fetchone()[0]


# ======================================================
# Upload Statistics
# ======================================================

def get_upload_statistics():

    cursor.execute(
        """
        SELECT
            module,
            COUNT(*)
        FROM uploads
        GROUP BY module
        """
    )

    return cursor.fetchall()