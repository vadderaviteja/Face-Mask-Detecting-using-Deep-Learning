# 😷 Face Mask Detection using Deep Learning

## 📌 Project Overview
This project is a Face Mask Detection system built using Deep Learning.  
The model can classify whether a person is **wearing a mask** or **not wearing a mask** from an input image.

The system uses a pretrained **ResNet18** model implemented in PyTorch and is deployed using a Streamlit web application where users can upload images and receive predictions instantly.

---

## 🎯 Objectives
- Detect whether a person is wearing a mask or not.
- Build an image classification model using deep learning.
- Train the model using a labeled dataset.
- Evaluate model performance using metrics.
- Deploy the trained model using a web interface.

---

## 🧠 Technologies Used
- Python
- PyTorch
- Torchvision
- Streamlit
- NumPy
- Pillow

---

## 📂 Dataset
The dataset used for training contains images of faces with masks and without masks.

Dataset structure:

```
Face Mask Dataset
│
├── Train
│   ├── WithMask
│   └── WithoutMask
│
├── Validation
│   ├── WithMask
│   └── WithoutMask
│
└── Test
    ├── WithMask
    └── WithoutMask
```

Total images: **~12,000**

---

## 🏗 Model Architecture

Model used: **ResNet18**

Steps:
1. Load pretrained ResNet18 model
2. Replace final fully connected layer
3. Train the model for binary classification

Output classes:

```
0 → Mask
1 → No Mask
```

---

## 🔄 Training Configuration

- Loss Function: CrossEntropyLoss
- Optimizer: Adam
- Epochs: 5
- Batch Size: 32
- Image Size: 224 × 224

Data Augmentation:
- RandomHorizontalFlip
- RandomRotation
- RandomResizedCrop
- ColorJitter

---

## 📊 Model Performance

| Metric | Score |
|------|------|
Training Accuracy | ~99% |
Validation Accuracy | ~99% |
Test Accuracy | **98.89%** |

---

## 📈 Evaluation Metrics
The model was evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1 Score

---

## 💾 Model Saving

After training, the model weights are saved as:

```
mask_model1.pth1
```

This file contains the trained model parameters which are used during deployment.

---

## 🌐 Deployment

The model is deployed using **Streamlit**.

Features:
- Upload an image
- Model predicts mask or no mask
- Displays result instantly

---

## 🚀 How to Run the Project

### 1 Install dependencies

```bash
pip install torch torchvision streamlit pillow numpy
```

### 2 Run the Streamlit app

```bash
streamlit run app.py
```

### 3 Upload an Image

Upload a face image and the system will predict:

```
Mask
or
No Mask
```

---

## ⚠️ Limitations

- Beard images may sometimes be misclassified as masks.
- Model performance depends on dataset diversity.
- Lighting and face angles can affect predictions.

---

## 🔮 Future Improvements

- Real-time mask detection using webcam
- Face detection before classification
- Larger dataset training
- Cloud deployment

---

## 👨‍💻 Author

**Raviteja Vadde**

B.Tech – Computer Science Engineering  
Specialization: Artificial Intelligence & Data Science

Interested in Machine Learning, Computer Vision, and Data Science.
