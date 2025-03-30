import cv2
import numpy as np
import os

MODEL_PATH = os.path.join("model", "resnet_50_1by2_nsfw.caffemodel")
PROTOTXT_PATH = os.path.join("model", "deploy.prototxt")

# Carrega modelo Caffe da Yahoo
net = cv2.dnn.readNetFromCaffe(PROTOTXT_PATH, MODEL_PATH)

def classify_image(image_path):
    """
    Classifica a imagem usando o modelo NSFW da Yahoo (Caffe + OpenCV).
    Retorna 'Safe' ou 'Suspicious' + score.
    """
    img = cv2.imread(image_path)
    blob = cv2.dnn.blobFromImage(img, 1.0, (224, 224), (104, 117, 123))
    net.setInput(blob)
    preds = net.forward()
    
    # NSFW = índice 1 (segundo valor)
    score = float(preds[0][1])
    label = "Suspicious" if score > 0.5 else "Safe"
    confidence = round(score * 100, 2) if label == "Suspicious" else round((1 - score) * 100, 2)

    return label, confidence
