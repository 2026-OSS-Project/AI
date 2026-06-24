import os

import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image


CLASS_NAMES = ["can", "paper", "plastic", "vinyl"]

MODEL_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "model",
        "best_model_mobilenetv2.pth"
    )
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def load_model():
    model = models.mobilenet_v2(weights=None)

    model.classifier[1] = nn.Linear(
        model.classifier[1].in_features,
        len(CLASS_NAMES)
    )

    state_dict = torch.load(MODEL_PATH, map_location=device)
    model.load_state_dict(state_dict)

    model.to(device)
    model.eval()

    return model


model = load_model()


transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


def predict_image(image: Image.Image):
    image = image.convert("RGB")
    input_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(input_tensor)
        probabilities = torch.softmax(outputs, dim=1)
        confidence, predicted_idx = torch.max(probabilities, dim=1)

    predicted_class = CLASS_NAMES[predicted_idx.item()]
    confidence_score = confidence.item()

    return predicted_class, confidence_score
