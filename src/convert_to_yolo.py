import os
import xml.etree.ElementTree as ET

# ----------------------------------------------------
# Dataset Path
# ----------------------------------------------------

DATASET_PATH = "dataset/blood_dataset"

# ----------------------------------------------------
# Class Names
# ----------------------------------------------------

classes = [
    "RBC",
    "WBC",
    "Platelets"
]

# ----------------------------------------------------
# Convert XML to YOLO
# ----------------------------------------------------

def convert_folder(folder):

    xml_folder = os.path.join(DATASET_PATH, folder, "ann")

    label_folder = os.path.join(DATASET_PATH, folder, "labels")

    os.makedirs(label_folder, exist_ok=True)

    for xml_file in os.listdir(xml_folder):

        if not xml_file.endswith(".xml"):
            continue

        xml_path = os.path.join(xml_folder, xml_file)

        tree = ET.parse(xml_path)

        root = tree.getroot()

        width = int(root.find("size/width").text)

        height = int(root.find("size/height").text)

        txt_name = xml_file.replace(".xml", ".txt")

        txt_path = os.path.join(label_folder, txt_name)

        with open(txt_path, "w") as f:

            for obj in root.findall("object"):

                cls = obj.find("name").text

                if cls not in classes:
                    continue

                cls_id = classes.index(cls)

                box = obj.find("bndbox")

                xmin = float(box.find("xmin").text)

                ymin = float(box.find("ymin").text)

                xmax = float(box.find("xmax").text)

                ymax = float(box.find("ymax").text)

                x_center = ((xmin + xmax) / 2) / width

                y_center = ((ymin + ymax) / 2) / height

                w = (xmax - xmin) / width

                h = (ymax - ymin) / height

                f.write(
                    f"{cls_id} {x_center} {y_center} {w} {h}\n"
                )

# ----------------------------------------------------

convert_folder("train")

convert_folder("val")

convert_folder("test")

print("Dataset Converted Successfully")