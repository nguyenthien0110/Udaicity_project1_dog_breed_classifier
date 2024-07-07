from torchvision import models, transforms
from PIL import Image
import torch

def load_model(architecture='vgg'):
    if architecture == 'vgg':
        model = models.vgg16(pretrained=True)
    # Add other models if necessary
    model.eval()
    return model

def process_image(image_path):
    image = Image.open(image_path)
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    return preprocess(image).unsqueeze(0)

def classify_image(model, image_path):
    image = process_image(image_path)
    with torch.no_grad():
        output = model(image)
    _, predicted = output.max(1)
    return predicted.item()

def read_dognames(dogfile):
    with open(dogfile, 'r') as f:
        dognames = f.read().splitlines()
    return dognames

def is_dog(label, dognames):
    return label.lower() in dognames
