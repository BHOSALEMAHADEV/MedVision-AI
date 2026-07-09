from ultralytics import YOLO
import os

# ==========================================================
# Load Trained Blood Cell Detection Model
# ==========================================================

MODEL_PATH = "runs/detect/models/blood_detection-5/weights/best.pt"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        f"Model not found:\n{MODEL_PATH}"
    )

model = YOLO(MODEL_PATH)

# ==========================================================
# Blood Cell Detection
# ==========================================================

def detect_blood_cells(image_path):

    results = model.predict(

        source=image_path,

        conf=0.25,

        imgsz=640,

        save=False,

        verbose=False

    )

    return results

# ==========================================================
# Count Blood Cells
# ==========================================================

def count_cells(results):

    prediction = results[0]

    counts = {

        "RBC": 0,

        "WBC": 0,

        "Platelets": 0

    }

    for box in prediction.boxes:

        class_id = int(box.cls)

        class_name = prediction.names[class_id]

        if class_name in counts:

            counts[class_name] += 1

    return counts

# ==========================================================
# Average Confidence
# ==========================================================

def average_confidence(results):

    prediction = results[0]

    if len(prediction.boxes) == 0:

        return 0

    total = 0

    for box in prediction.boxes:

        total += float(box.conf)

    confidence = (total / len(prediction.boxes)) * 100

    return round(confidence, 2)

# ==========================================================
# Return Processed Image
# ==========================================================

def processed_image(results):

    prediction = results[0]

    return prediction.plot()