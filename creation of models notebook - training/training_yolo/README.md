# 🧠 YOLOv8 SDS Pictogram Training

This folder contains the configuration and scripts related to training a YOLOv8 model for detecting and classifying **Safety Data Sheet (SDS)** pictograms.

---

## 📂 Dataset Structure

Due to the sensitive nature of the original dataset, the actual images and annotations are **not included** in this repository. However, to train your own YOLOv8 model, you must follow the directory format shown below:

```yaml
datasets/
└── dataset.yaml
├── images/
│ ├── train/ # Training images
│ └── val/ # Validation images
└── labels/
  ├── train/ # Corresponding YOLO-format .txt label files
  └── val/
```

Each label file should follow YOLO format:

``
<class_id> <x_center> <y_center> <width> <height>
``

*All values are normalized (between 0 and 1).*

You can use tools like:
- [LabelImg](https://github.com/tzutalin/labelImg) (with YOLO format)
- [Roboflow](https://roboflow.com) (for annotation and export)

---

## ⚙️ `.yaml`

The file `.yaml` defines your dataset structure and classes for YOLOv8 training.

```yaml
path: ../data/custom_dataset        # Root directory of the dataset
train: images/train                 # Relative path to training images
val: images/val                     # Relative path to validation images

nc: 9                               # Number of classes
names: [
    'Explosive',
    'Flammable',
    'Oxidizer',
    'Gas',
    'Corrosive',
    'Toxic',
    'Irritant',
    'Health Hazard',
    'Environmental Hazard'
]
```

You may modify:

- `path` to point to your local dataset
- `names` to match your label classes

---

## 🏁 Training Command

After installing [Ultralytics YOLOv8](https://docs.ultralytics.com/), you can run this line of code (which is included in the notebook) to train the YOLOv8 model:

```python
model.train(data="datasets\dataset.yaml", epochs=50, imgsz=640, batch=16, augment=True)
```

## 📌 Notes

- You can use any YOLOv8 model variant: yolov8n.pt, yolov8s.pt, yolov8m.pt, etc.
- The training logs, metrics, and weights will be saved to the runs/ directory.
- The final fine-tuned YOLOv8 model "best.pt" will be saved in the "creation of models notebook - training\training_yolo\runs\detect\train2\weights\best.pt"
- Use tensorboard or YOLOv8’s built-in visualization tools to monitor training.
