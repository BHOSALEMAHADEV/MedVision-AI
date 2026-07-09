# 🏥 MedVision AI

> **AI-Powered Medical Imaging Analysis Platform using Deep Learning, Computer Vision, and Streamlit**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Application-red)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Deep%20Learning-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-lightgrey)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![License](https://img.shields.io/badge/License-MIT-success)

---

# 📖 Overview

**MedVision AI** is an AI-powered medical imaging platform designed to assist healthcare professionals in analyzing biomedical images using **Deep Learning**, **Computer Vision**, and **Medical Image Processing** techniques.

The platform integrates multiple medical imaging modules into a single application, allowing users to:

- Manage patient records
- Upload medical images
- Perform AI-based disease detection
- Process medical images
- Visualize AI predictions
- Generate medical reports

The project demonstrates the practical application of Artificial Intelligence in Healthcare by combining **YOLOv8**, **TensorFlow**, **OpenCV**, **SQLite**, and **Streamlit** into one integrated system.

---

#  Project Objectives

The primary objectives of MedVision AI are:

- Develop an intelligent medical imaging platform.
- Automate disease detection using Artificial Intelligence.
- Reduce diagnosis time through Deep Learning.
- Improve healthcare workflow efficiency.
- Manage patient information securely.
- Generate AI-assisted medical reports.
- Demonstrate Computer Vision applications in Healthcare.

---

# ⭐ Key Features

- Secure User Authentication
- Patient Management System
- Medical Image Upload
- Medical Image Processing
- Deep Learning Disease Detection
- Blood Cell Analysis using YOLOv8
- Confidence Score Generation
- SQLite Database Integration
- Streamlit Web Interface

---

# 🩸 Blood Cell Analyzer

## Overview

The **Blood Cell Analyzer** is one of the core AI modules of **MedVision AI**. It automatically detects and counts different types of blood cells from microscopic blood smear images using **YOLOv8**, a state-of-the-art deep learning object detection model.

Instead of manually examining blood smear images, the system identifies blood cells, counts them, and displays the results with confidence scores, helping healthcare professionals perform faster preliminary analysis.

---

## 🎯 Objective

The primary objective of this module is to:

- Detect blood cells automatically.
- Count Red Blood Cells (RBC).
- Count White Blood Cells (WBC).
- Count Platelets.
- Display detected cells with bounding boxes.
- Assist healthcare professionals in blood smear analysis.
- Reduce manual counting effort.

---

## 🧠 Deep Learning Model

The Blood Cell Analyzer is developed using **YOLOv8 (You Only Look Once Version 8)**, a real-time object detection model developed by **Ultralytics**.

The model was trained on a publicly available Blood Cell Detection Dataset and fine-tuned to identify three different blood cell types.

### Model Details

| Property | Value |
|----------|--------|
| Model | YOLOv8 Nano |
| Framework | Ultralytics YOLOv8 |
| Backend | PyTorch |
| Language | Python |
| GPU | NVIDIA GeForce GTX 1650 (CUDA) |
| Model File | best.pt |

---

## 📂 Dataset

The model is trained using a Blood Cell Detection Dataset containing annotated microscopic blood smear images.

### Classes

| Class | Description |
|--------|-------------|
| RBC | Red Blood Cell |
| WBC | White Blood Cell |
| Platelets | Blood Platelets |

Dataset contains:

- Training Images
- Validation Images
- Test Images
- Bounding Box Annotations

---

## ⚙️ Blood Cell Analysis Workflow

```text
Blood Smear Image
        │
        ▼
Upload Image
        │
        ▼
Image Preprocessing
        │
        ▼
YOLOv8 Deep Learning Model
        │
        ▼
Blood Cell Detection
        │
        ▼
Bounding Box Generation
        │
        ▼
Cell Counting
        │
        ▼
Confidence Score
        │
        ▼
Display Results
```

---

## 🔬 Image Processing

Before prediction, every uploaded image undergoes preprocessing.

Implemented preprocessing techniques:

- Image Loading
- Image Resizing
- RGB Conversion
- Pixel Normalization
- Tensor Conversion

These preprocessing steps prepare the image for accurate AI prediction.

---

## 🚀 Detection Process

The trained YOLOv8 model performs the following tasks:

1. Upload blood smear image
2. Detect all blood cells
3. Draw bounding boxes
4. Classify blood cells
5. Count RBC
6. Count WBC
7. Count Platelets
8. Calculate confidence
9. Display processed image

---

## 📊 Output

The application displays:

- Uploaded Blood Image
- Processed Blood Image
- RBC Count
- WBC Count
- Platelet Count
- Average Confidence
- Detection Status

Example:

```text
Blood Cell Analysis Report

RBC        : 56
WBC        : 1
Platelets  : 2

Confidence : 95.8 %

Status : Analysis Completed Successfully
```

---

## 📈 Model Performance

| Metric | Score |
|---------|-------|
| Precision | 85.9 % |
| Recall | 91.8 % |
| mAP@50 | 92.6 % |

The trained YOLOv8 model provides reliable blood cell detection for educational and research purposes.

---

## 💻 Technologies Used

- Python
- YOLOv8
- Ultralytics
- PyTorch
- CUDA
- OpenCV
- Pillow
- Streamlit
- SQLite

---

## 📂 Blood Cell Module Structure

```text
pages/
    blood_analyzer.py

src/
    blood_model.py
    train_blood_model.py

models/
    best.pt

dataset/
    blood_dataset/
```

---

## ✨ Blood Cell Analyzer Features

- AI-Based Blood Cell Detection
- YOLOv8 Object Detection
- Automatic Cell Counting
- Bounding Box Visualization
- Confidence Score
- GPU Accelerated Prediction
- Streamlit Interactive Interface
- Real-Time Analysis

---

## ⚠️ Disclaimer

This module is intended for **educational and research purposes only**.

The AI predictions generated by MedVision AI should **not** replace professional medical diagnosis. All results must be verified by qualified healthcare professionals.
---

# 🏗️ System Architecture

The MedVision AI platform follows a modular architecture where each component performs a specific task. The application integrates patient management, image processing, artificial intelligence models, and report generation into a single healthcare platform.

```text
                     User
                       │
                       ▼
              Streamlit Web Interface
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
 Authentication   Patient Module   Image Upload
        │              │              │
        └──────────────┼──────────────┘
                       ▼
             Image Preprocessing
                       │
                       ▼
            Artificial Intelligence
                       │
     ┌─────────────────┼──────────────────┐
     ▼                 ▼                  ▼
 Blood Analyzer   Lung Analyzer    Brain Analyzer
                       │
                       ▼
              AI Prediction Engine
                       │
                       ▼
            Results & Confidence Score
                       │
                       ▼
               SQLite Database
                       │
                       ▼
               Streamlit Dashboard
```

---

# 🔄 Application Workflow

The complete workflow of MedVision AI is shown below.

```text
User Login
     │
     ▼
Dashboard
     │
     ▼
Patient Registration
     │
     ▼
Medical Image Upload
     │
     ▼
Image Preprocessing
     │
     ▼
AI Model Prediction
     │
     ▼
Disease Detection
     │
     ▼
Confidence Score
     │
     ▼
Result Visualization
     │
     ▼
Database Storage
```

---

# 💻 Technology Stack

## Programming Language

- Python 3.12

---

## Web Framework

- Streamlit

---

## Deep Learning

- YOLOv8 (Ultralytics)
- TensorFlow
- Keras
- PyTorch

---

## Computer Vision

- OpenCV
- Pillow

---

## Database

- SQLite3

---

## Data Processing

- NumPy
- Pandas

---

## Visualization

- Matplotlib

---

## Development Tools

- Visual Studio Code
- Git
- GitHub

---

# 📂 Project Structure

```text
MEDVISION_AI/

│
├── app.py
├── config.py
├── database.py
├── README.md
├── requirements.txt
│
├── assets/
│   └── css/
│       └── style.css
│
├── database/
│   └── medvision.db
│
├── models/
│   ├── best.pt
│   ├── blood_model.keras
│   └── lung_model.keras
│
├── dataset/
│   ├── blood_dataset/
│   └── lung_dataset/
│
├── uploads/
│   ├── blood/
│   ├── lung/
│   ├── brain/
│   ├── retina/
│   ├── cancer/
│   └── processed/
│
├── pages/
│   ├── patients.py
│   ├── upload.py
│   ├── image_processing.py
│   ├── blood_analyzer.py
│   ├── lung_analyzer.py
│   ├── analytics.py
│   └── settings.py
│
├── src/
│   ├── auth.py
│   ├── patient_db.py
│   ├── upload_db.py
│   ├── image_processing.py
│   ├── blood_model.py
│   ├── lung_model.py
│   └── train_blood_model.py
│
└── reports/
```

---

# 🗄️ Database Design

The project uses **SQLite** as the backend database to securely store patient information and medical records.

## Patients Table

| Column | Description |
|----------|-------------|
| id | Primary Key |
| patient_id | Unique Patient ID |
| full_name | Patient Name |
| age | Patient Age |
| gender | Gender |
| phone | Contact Number |
| email | Email Address |
| blood_group | Blood Group |
| address | Patient Address |
| medical_history | Medical History |

---

## Medical Image Table

| Column | Description |
|----------|-------------|
| id | Primary Key |
| patient_id | Patient ID |
| image_type | Blood / CT / MRI |
| image_name | Uploaded Image |
| upload_date | Upload Date |
| file_path | Image Location |

---

# 📊 Current Modules

| Module | Status |
|----------|----------|
| 🔐 Authentication | ✅ Completed |
| 👨‍⚕️ Patient Management | ✅ Completed |
| 📤 Medical Image Upload | ✅ Completed |
| 🖼 Image Processing | ✅ Completed |
| 🩸 Blood Cell Analyzer | ✅ Completed |
| 🫁 Lung CT Analyzer | 🚧 In Progress |
| 🧠 Brain MRI Analyzer | 📅 Planned |
| 👁 Retina Analyzer | 📅 Planned |
| 🔬 Histopathology Analyzer | 📅 Planned |
| 📈 Analytics Dashboard | 📅 Planned |

---

# 🔒 Security Features

The application includes several security and data management features:

- Secure User Authentication
- Session Management
- Unique Patient ID Generation
- Organized Image Storage
- SQLite Database Integration
- Modular Source Code Structure

---

# 🎯 Why MedVision AI?

MedVision AI demonstrates how Artificial Intelligence can be integrated into healthcare applications to assist medical professionals.

Key advantages include:

- AI-assisted disease detection
- Faster preliminary diagnosis
- Automated blood cell counting
- Medical image enhancement
- User-friendly web interface
- Modular architecture for future expansion
- Deep Learning model integration
- Secure patient data management

---
---

# 🚀 Installation Guide

Follow these steps to set up and run the MedVision AI project on your local machine.

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/MedVision-AI.git
```

Navigate to the project directory.

```bash
cd MedVision-AI
```

---

## 2️⃣ Create a Virtual Environment

Windows

```bash
python -m venv venv
```

Activate the virtual environment

```bash
venv\Scripts\activate
```

---

## 3️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

If the `requirements.txt` file is unavailable, install the major dependencies manually.

```bash
pip install streamlit
pip install ultralytics
pip install torch torchvision torchaudio
pip install tensorflow
pip install opencv-python
pip install pillow
pip install matplotlib
pip install pandas
pip install numpy
```

---

## 4️⃣ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your default web browser.

---

# 📸 Application Screenshots

## 🏠 Dashboard

- Overview of all AI modules
- Navigation sidebar
- Patient statistics
- Medical analytics

*(Add dashboard screenshot here)*

---

## 👨‍⚕️ Patient Management

Features

- Add Patient
- Update Patient
- Delete Patient
- Search Patient

*(Add patient management screenshot here)*

---

## 📤 Medical Image Upload

Features

- Upload Medical Images
- Preview Uploaded Image
- Store Image Information

*(Add upload page screenshot here)*

---

## 🖼 Image Processing

Available Processing Operations

- Grayscale Conversion
- Histogram Equalization
- Gaussian Blur
- Edge Detection

*(Add image processing screenshot here)*

---

## 🩸 Blood Cell Analyzer

The Blood Cell Analyzer performs:

- Blood Cell Detection
- RBC Counting
- WBC Counting
- Platelet Counting
- Confidence Score
- Bounding Box Visualization

*(Add Blood Analyzer screenshot here)*

---

# 📊 Sample Prediction

```text
Blood Cell Analysis Report

Detected Cells

RBC        : 56

WBC        : 1

Platelets  : 2

Confidence : 95.8 %

Status : Analysis Completed Successfully
```

---

# 📈 Model Training

The Blood Cell Analyzer uses a custom-trained YOLOv8 model.

Training configuration

| Parameter | Value |
|-----------|--------|
| Model | YOLOv8 Nano |
| Framework | Ultralytics |
| Backend | PyTorch |
| GPU | NVIDIA GTX 1650 |
| CUDA | Enabled |
| Epochs | 20 |
| Image Size | 512 × 512 |
| Batch Size | 8 |

---

# 📊 Validation Results

| Metric | Score |
|---------|-------|
| Precision | 85.9 % |
| Recall | 91.8 % |
| mAP@50 | 92.6 % |

These results demonstrate that the trained model can accurately detect blood cells in microscopic blood smear images.

---

# 📌 Future Enhancements

The MedVision AI platform can be extended with several advanced features.

## AI Modules

- Lung CT Disease Detection
- Brain MRI Tumor Detection
- Retinal Disease Detection
- Histopathology Cancer Detection

---

## Healthcare Features

- PDF Report Generation
- Electronic Medical Records
- Doctor Dashboard
- Patient History Tracking
- Appointment Scheduling

---

## AI Improvements

- Explainable AI (Grad-CAM)
- Transfer Learning
- Multi-Class Disease Detection
- DICOM Image Support
- Cloud AI Inference

---

## Deployment

- Docker Container
- AWS Deployment
- Azure Deployment
- Google Cloud Deployment

---

# 🏆 Project Highlights

✅ Artificial Intelligence

✅ Deep Learning

✅ Computer Vision

✅ Medical Image Processing

✅ YOLOv8 Object Detection

✅ GPU Accelerated Training

✅ SQLite Database

✅ Streamlit Web Application

✅ Modular Software Architecture

---

# 📚 Learning Outcomes

During the development of MedVision AI, the following skills were applied and enhanced:

- Python Programming
- Object-Oriented Programming
- Deep Learning
- Computer Vision
- Medical Image Analysis
- Streamlit Development
- Database Design
- YOLOv8 Model Training
- GPU Computing using CUDA
- Software Engineering

---

# 👨‍💻 Developer

**Mahadev Bhosale**

Artificial Intelligence & Machine Learning Engineering

Basaveshwar Engineering College, Bagalkot

### Technical Skills

- Python
- Deep Learning
- Machine Learning
- Computer Vision
- TensorFlow
- PyTorch
- YOLOv8
- OpenCV
- Streamlit
- SQLite

---

# 🙏 Acknowledgements

This project was developed using the following open-source technologies and datasets.

- Ultralytics YOLOv8
- PyTorch
- TensorFlow
- Streamlit
- OpenCV
- SQLite
- NumPy
- Pandas
- Pillow
- Kaggle Datasets

Special thanks to the open-source community for providing high-quality tools, frameworks, and publicly available datasets that made this project possible.

---
#OUTPUT
<img width="1917" height="907" alt="image" src="https://github.com/user-attachments/assets/4416b62d-20af-4c5b-8472-3fddc1b9bff7" />
<img width="1904" height="936" alt="image" src="https://github.com/user-attachments/assets/1a5f752e-3a72-4bca-8205-4b710c93a074" />
<img width="1814" height="934" alt="image" src="https://github.com/user-attachments/assets/aa87bc5c-a0e5-475d-bf84-ee6b2f076c49" />
<img width="1911" height="930" alt="image" src="https://github.com/user-attachments/assets/6cfe7ae5-dff8-45ee-84ac-0943498bb762" />
<img width="1919" height="896" alt="image" src="https://github.com/user-attachments/assets/76f0f5a5-8520-45fe-a983-4c4fe590374c" />





# 📜 License

This project is developed for **educational, research, and demonstration purposes**.

The AI predictions generated by MedVision AI are intended to assist healthcare professionals and **should not be considered a replacement for professional medical diagnosis**.

Users should always consult qualified medical practitioners before making healthcare decisions.

---

# ⭐ Support the Project

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support helps encourage further development and improvements.

---

## Thank You ❤️

Thank you for exploring **MedVision AI**.

We hope this project demonstrates the practical application of Artificial Intelligence, Deep Learning, and Computer Vision in modern healthcare systems.
