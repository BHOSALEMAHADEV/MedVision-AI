import os
from PIL import Image
import streamlit as st

from src.patient_db import get_patient_ids
from src.upload_db import (
    save_upload,
    get_uploads,
    search_uploads,
    delete_upload,
    get_total_uploads,
    get_upload_statistics
)

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("Medical Image Upload")

st.caption("Upload biomedical images for AI analysis")

st.divider()

# ==========================================================
# DASHBOARD
# ==========================================================

total_uploads = get_total_uploads()

stats = get_upload_statistics()

blood = 0
lung = 0
brain = 0
retina = 0
cancer = 0

for module, count in stats:

    if module == "blood":
        blood = count

    elif module == "lung":
        lung = count

    elif module == "brain":
        brain = count

    elif module == "retina":
        retina = count

    elif module == "cancer":
        cancer = count

c1, c2, c3 = st.columns(3)

c1.metric("Total Uploads", total_uploads)
c2.metric("Blood Images", blood)
c3.metric("Lung Images", lung)

c4, c5 = st.columns(2)

c4.metric("Brain Images", brain)
c5.metric("Retina + Cancer", retina + cancer)

st.divider()

# ==========================================================
# PATIENT SELECTION
# ==========================================================

patients = get_patient_ids()

patient_list = []

for patient in patients:

    patient_list.append(
        f"{patient[0]} - {patient[1]}"
    )

if len(patient_list) == 0:

    st.warning("No patients registered.")

    st.stop()

selected_patient = st.selectbox(
    "Select Patient",
    patient_list
)

patient_id = selected_patient.split(" - ")[0]

# ==========================================================
# MODULE SELECTION
# ==========================================================

module = st.selectbox(

    "Select Medical Module",

    [

        "blood",

        "lung",

        "brain",

        "retina",

        "cancer"

    ]

)

# ==========================================================
# IMAGE UPLOAD
# ==========================================================

uploaded_file = st.file_uploader(

    "Upload Medical Image",

    type=[

        "jpg",

        "jpeg",

        "png",

        "bmp",

        "tif",

        "tiff"

    ]

)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.subheader("Image Preview")

    st.image(
        image,
        use_container_width=True
    )

    image_name = uploaded_file.name

    image_size = round(
        uploaded_file.size / 1024,
        2
    )

    image_format = image.format

    st.write("### Image Information")

    col1, col2 = st.columns(2)

    with col1:

        st.write("Image Name")
        st.info(image_name)

        st.write("Format")
        st.info(image_format)

    with col2:

        st.write("Size (KB)")
        st.info(image_size)

        st.write("Module")
        st.info(module)

    st.divider()

# ==========================================================
# SAVE IMAGE
# ==========================================================

    if st.button("Save Image", use_container_width=True):

        folder = os.path.join("uploads", module)

        os.makedirs(folder, exist_ok=True)

        file_path = os.path.join(
            folder,
            image_name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        save_upload(

            patient_id,

            module,

            image_name,

            file_path,

            image_size,

            image_format

        )

        st.success("Image uploaded successfully.")

st.divider()

# ==========================================================
# SEARCH UPLOADS
# ==========================================================

st.subheader("Search Uploads")

keyword = st.text_input(
    "Search by Patient ID, Module or Image Name"
)

if keyword.strip() == "":

    uploads = get_uploads()

else:

    uploads = search_uploads(keyword)

st.divider()

# ==========================================================
# UPLOAD HISTORY
# ==========================================================

st.subheader("Upload History")

if len(uploads) == 0:

    st.info("No uploaded images found.")

else:

    import pandas as pd

    df = pd.DataFrame(

        uploads,

        columns=[

            "ID",

            "Patient ID",

            "Module",

            "Image Name",

            "Image Size (KB)",

            "Format",

            "Uploaded At"

        ]

    )

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True,

        height=350

    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(

        label="Download Upload History",

        data=csv,

        file_name="upload_history.csv",

        mime="text/csv"

    )

st.divider()

# ==========================================================
# DELETE UPLOAD
# ==========================================================

st.subheader("Delete Upload")

if len(uploads) != 0:

    upload_ids = [row[0] for row in uploads]

    selected_upload = st.selectbox(
        "Select Upload ID",
        upload_ids
    )

    if st.button("Delete Upload", use_container_width=True):

        upload = None

        for row in uploads:

            if row[0] == selected_upload:
                upload = row
                break

        if upload is not None:

            image_name = upload[3]
            module = upload[2]

            image_path = os.path.join(
                "uploads",
                module,
                image_name
            )

            if os.path.exists(image_path):

                os.remove(image_path)

            delete_upload(selected_upload)

            st.success("Upload deleted successfully.")

            st.rerun()

else:

    st.info("No uploads available.")

st.divider()

# ==========================================================
# RECENT UPLOADS
# ==========================================================

st.subheader("Recent Uploads")

if len(uploads) == 0:

    st.info("No uploaded images found.")

else:

    recent_uploads = uploads[:5]

    for upload in recent_uploads:

        st.container(border=True)

        st.write(f"Patient ID : {upload[1]}")
        st.write(f"Module : {upload[2]}")
        st.write(f"Image : {upload[3]}")
        st.write(f"Size : {upload[4]} KB")
        st.write(f"Format : {upload[5]}")
        st.write(f"Uploaded : {upload[6]}")

        st.write("--------------------------------")

st.divider()

# ==========================================================
# MODULE SUMMARY
# ==========================================================

st.subheader("Module Summary")

stats = get_upload_statistics()

if len(stats) == 0:

    st.info("No upload statistics available.")

else:

    summary = {}

    for module_name, count in stats:

        summary[module_name] = count

    st.write(summary)

st.divider()

# ==========================================================
# PROJECT STATUS
# ==========================================================

st.success("Medical Image Upload Module Ready")

st.info(
    """
Completed Features

- Patient Selection
- Image Upload
- Image Preview
- Save Image
- Upload History
- Search Uploads
- Delete Upload
- Download CSV
- Module Statistics
- Recent Uploads
"""
)
