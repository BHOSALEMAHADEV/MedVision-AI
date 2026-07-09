from ultralytics import YOLO

def train_model():

    model = YOLO("yolov8n.pt")

    model.train(
        data="dataset/blood_dataset/data.yaml",
        epochs=20,
        imgsz=512,
        batch=8,
        device=0,
        workers=0,          # IMPORTANT: Set to 0 on Windows
        cache=False,
        pretrained=True,
        project="models",
        name="blood_detection"
    )

    print("Training Completed Successfully!")


if __name__ == "__main__":
    train_model()