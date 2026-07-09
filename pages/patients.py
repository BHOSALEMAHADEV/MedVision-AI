import streamlit as st
import pandas as pd

from src.patient_db import (
    add_patient,
    get_all_patients,
    search_patient,
    get_patient,
    update_patient,
    delete_patient
)

# ======================================================
# PAGE TITLE
# ======================================================

st.title("👤 Patient Management")

# ======================================================
# DASHBOARD METRICS
# ======================================================

patients = get_all_patients()

total_patients = len(patients)

male = len([p for p in patients if p[3] == "Male"])
female = len([p for p in patients if p[3] == "Female"])
other = len([p for p in patients if p[3] == "Other"])

st.write("---")

c1, c2, c3, c4 = st.columns(4)

c1.metric(" Total Patients", total_patients)
c2.metric(" Male", male)
c3.metric(" Female", female)
c4.metric("⚧ Other", other)

st.write("---")

# ======================================================
# PATIENT REGISTRATION
# ======================================================

with st.expander(" Register New Patient", expanded=True):

    with st.form("patient_form"):

        name = st.text_input("Full Name")

        age = st.number_input(
            "Age",
            min_value=0,
            max_value=120,
            value=25
        )

        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female",
                "Other"
            ]
        )

        phone = st.text_input("Phone Number")

        email = st.text_input("Email")

        blood_group = st.selectbox(
            "Blood Group",
            [
                "A+",
                "A-",
                "B+",
                "B-",
                "AB+",
                "AB-",
                "O+",
                "O-"
            ]
        )

        address = st.text_area("Address")

        medical_history = st.text_area("Medical History")

        submit = st.form_submit_button(" Save Patient")

        if submit:

            patient_id = add_patient(
                name,
                age,
                gender,
                phone,
                email,
                blood_group,
                address,
                medical_history
            )

            st.success(" Patient Registered Successfully")

            st.info(f"Patient ID : {patient_id}")

st.write("---")

# ======================================================
# SEARCH PATIENT
# ======================================================

st.subheader("🔍 Search Patient")

keyword = st.text_input(
    "Search by Patient ID or Name"
)

if keyword == "":
    patient_data = get_all_patients()
else:
    patient_data = search_patient(keyword)

st.write("---")

# ======================================================
# PATIENT LIST
# ======================================================

st.subheader(" Patient List")

df = pd.DataFrame(

    patient_data,

    columns=[
        "Patient ID",
        "Name",
        "Age",
        "Gender",
        "Phone",
        "Email",
        "Blood Group"
    ]

)

st.dataframe(

    df,

    use_container_width=True,

    hide_index=True,

    height=350

)

st.success(f"Total Patients : {len(df)}")

# ======================================================
# DOWNLOAD CSV
# ======================================================

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(

    label=" Download Patient Data",

    data=csv,

    file_name="patients.csv",

    mime="text/csv"

)

st.write("---")

# ======================================================
# UPDATE PATIENT
# ======================================================

st.subheader(" Update Patient")

update_patient_id = st.text_input(
    "Enter Patient ID to Update"
)

if st.button("Load Patient"):

    patient = get_patient(update_patient_id)

    if patient:

        st.session_state.patient = patient

    else:

        st.error(" Patient not found.")

# ------------------------------------------------------

if "patient" in st.session_state:

    patient = st.session_state.patient

    with st.form("update_patient_form"):

        name = st.text_input(
            "Full Name",
            patient[1]
        )

        age = st.number_input(
            "Age",
            min_value=0,
            max_value=120,
            value=int(patient[2])
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"],
            index=["Male", "Female", "Other"].index(patient[3])
        )

        phone = st.text_input(
            "Phone Number",
            patient[4]
        )

        email = st.text_input(
            "Email",
            patient[5]
        )

        blood_group = st.selectbox(
            "Blood Group",
            [
                "A+",
                "A-",
                "B+",
                "B-",
                "AB+",
                "AB-",
                "O+",
                "O-"
            ],
            index=[
                "A+",
                "A-",
                "B+",
                "B-",
                "AB+",
                "AB-",
                "O+",
                "O-"
            ].index(patient[6])
        )

        address = st.text_area(
            "Address",
            patient[7]
        )

        medical_history = st.text_area(
            "Medical History",
            patient[8]
        )

        update_btn = st.form_submit_button(
            " Update Patient"
        )

        if update_btn:

            update_patient(

                patient[0],

                name,

                age,

                gender,

                phone,

                email,

                blood_group,

                address,

                medical_history

            )

            st.success(" Patient Updated Successfully!")

            del st.session_state.patient

            st.rerun()

st.write("---")

# ======================================================
# DELETE PATIENT
# ======================================================

st.subheader("🗑 Delete Patient")

delete_patient_id = st.text_input(
    "Enter Patient ID to Delete"
)

if st.button("Delete Patient"):

    patient = get_patient(delete_patient_id)

    if patient:

        delete_patient(delete_patient_id)

        st.success(" Patient Deleted Successfully!")

        st.rerun()

    else:

        st.error(" Patient ID not found.")

st.write("---")

# ======================================================
# PATIENT PROFILE
# ======================================================

st.subheader("👤 Patient Profile")

profile_patient_id = st.text_input(
    "Enter Patient ID to View"
)

if st.button("View Profile"):

    patient = get_patient(profile_patient_id)

    if patient:

        st.success("Patient Found")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("### Basic Information")

            st.write(f"**Patient ID:** {patient[0]}")
            st.write(f"**Name:** {patient[1]}")
            st.write(f"**Age:** {patient[2]}")
            st.write(f"**Gender:** {patient[3]}")
            st.write(f"**Blood Group:** {patient[6]}")

        with col2:

            st.markdown("### Contact Details")

            st.write(f"**Phone:** {patient[4]}")
            st.write(f"**Email:** {patient[5]}")
            st.write(f"**Address:** {patient[7]}")

        st.markdown("### Medical History")

        if patient[8]:

            st.info(patient[8])

        else:

            st.warning("No medical history available.")

    else:

        st.error(" Patient not found.")