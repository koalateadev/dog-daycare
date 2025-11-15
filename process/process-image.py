from ultralytics import YOLO
import cv2
import sys

PERSON_CLASS_ID = 0
DOG_CLASS_ID = 16

class DogHumanDetector:
    def __init__(self, weights_path: str = "yolov8m.pt", conf: float = 0.25):
        self.model = YOLO(weights_path)
        self.conf = conf

    def detect(self, image_path: str):
        img = cv2.imread(image_path)

        result = self.model(img, conf=self.conf)[0]
        boxes = result.boxes
        names = result.names

        for box in boxes:
            cls = int(box.cls[0])
            if cls not in (PERSON_CLASS_ID, DOG_CLASS_ID):
                continue

            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            label = f"{names[cls]} {conf:.2f}"

            # Draw rectangle
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Draw label
            cv2.putText(img, label, (x1, y1 - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)

        # Show result in window
        cv2.imshow("Detections", img)
        cv2.waitKey(0)  # Wait for a key press
        cv2.destroyAllWindows()

image_path = sys.argv[1]
if not image_path:
    print("Usage: python process-image.py <image_path>")
    exit(1)

detector = DogHumanDetector(weights_path="yolov8m.pt")
detector.detect(image_path)