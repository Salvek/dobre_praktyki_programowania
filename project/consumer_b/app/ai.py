import cv2
import numpy as np
import imutils

def count_people(image: np.ndarray) -> int:
    """
    Liczy osoby na obrazie przy użyciu HOG + SVM detektor ludzi.

    Args:
        image (np.ndarray): Obraz w formacie BGR (OpenCV standard).

    Returns:
        int: Liczba wykrytych osób.
    """
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    MAX_WIDTH = 1500
    height, width = image.shape[:2]
    if width > MAX_WIDTH:
        ratio = MAX_WIDTH / width
        new_height = int(height * ratio)
        image = imutils.resize(image, width=MAX_WIDTH, height=new_height)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    regions, weights = hog.detectMultiScale(
        gray,
        winStride=(2, 2),
        padding=(5, 5),
        scale=1.02
    )

    if len(weights) == 0:
        return 0

    mean_w = np.mean(weights)
    std_w = np.std(weights)
    k = 0.86
    filtered_objects = [
        regions[i] for i, weight in enumerate(weights)
        if weight >= (mean_w - k * std_w)
    ]

    return len(filtered_objects)
