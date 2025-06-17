from ultralytics import YOLO
import cv2
import numpy as np

def detect_fire():
    # Load the model
    model = YOLO('best.pt')
    
    # For camera usage
    cap = cv2.VideoCapture(0)  # 0 is the default camera
    
    while cap.isOpened():
        # Read frame
        success, frame = cap.read()
        
        if success:
            # Make prediction with YOLOv8
            results = model(frame)
            
            # Visualize the results
            annotated_frame = results[0].plot()
            
            # Show the results
            cv2.imshow("YOLOv8 Fire Detection", annotated_frame)
            
            # Press 'q' to exit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

def detect_on_image(image_path):
    # Load the model
    model = YOLO('best.pt')
    
    # Add the image path
    image = cv2.imread(image_path)
    
    # Make prediction with YOLOv8
    results = model(image)
    
    # Visualize the results
    annotated_frame = results[0].plot()
    
    # Show the result
    cv2.imshow("YOLOv8 Fire Detection", annotated_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # For live detection using camera:
    detect_fire()
    
    # For detection on a single image (example):
    # detect_on_image("firee.jpg") 