import streamlit as st
import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image

# Load model
model = models.resnet18(pretrained=False)
model.fc = nn.Linear(model.fc.in_features, 2)

model.load_state_dict(torch.load("mask_model1.pth", map_location=torch.device('cpu')))
model.eval()

# Class labels
classes = ["Mask", "No Mask"]

# Image transform
transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

st.title("Face Mask Detection App")

uploaded_file = st.file_uploader("Upload an image", type=["jpg","jpeg","png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_column_width=True)

    img = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(img)
        _, predicted = torch.max(outputs,1)

    prediction = classes[predicted.item()]

    st.subheader(f"Prediction: {prediction}")