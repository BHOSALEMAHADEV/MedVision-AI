import streamlit as st
import tempfile
from PIL import Image

from src.blood_model import detect_blood_cells

st.title("Blood Cell Analyzer")

st.write("Upload a blood smear image for AI analysis.")

uploaded_file = st.file_uploader(
    "Upload Blood Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("Analyze Blood Image"):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".jpg"
        ) as temp:

            temp.write(uploaded_file.getbuffer())

            image_path = temp.name

        results = detect_blood_cells(image_path)

        result = results[0]

        output = result.plot()

        st.image(
            output,
            caption="Detection Result",
            use_container_width=True
        )

        counts = {}

        for box in result.boxes:

            cls = int(box.cls)

            label = result.names[cls]

            counts[label] = counts.get(label, 0) + 1

        st.subheader("Blood Cell Count")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "RBC",
            counts.get("RBC", 0)
        )

        col2.metric(
            "WBC",
            counts.get("WBC", 0)
        )

        col3.metric(
            "Platelets",
            counts.get("Platelets", 0)
        )

        st.success("Analysis Completed Successfully")