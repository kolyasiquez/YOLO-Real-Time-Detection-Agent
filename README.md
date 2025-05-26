# YOLO-Real-Time-Detection-Agent
Real-time object detection &amp; low-level input automation using YOLOv8, OpenCV, and Windows API

🧠 Real-time Object Detection & Response Automation  
This project demonstrates the application of computer vision (YOLOv8), low-level input emulation (via Windows API), and screen capture (MSS) to create a real-time automation system for the game (in this case).

📊 Dataset & Training  
The object detection model was trained using a small custom dataset (I took screenshots in the game by myself) created with Roboflow. I used only one class named "zombies" to detect them.  
The model was trained with YOLOv8 for 50 epochs on this dataset, achieving good precision in the target detection scenario, especially considering dataset's small size.

⚙️ Tech Stack  
Python 3.12.6  
Ultralytics YOLOv8  
OpenCV  
MSS (Screen capture)  
ctypes (Windows input emulation)  
keyboard (keypress monitoring)  

🚀 How It Works  
The screen is continuously captured from the specified region.  

Each frame is passed to YOLOv8, which detects targets (zombies in this case).  

If a target is found with confidence above threshold:  

The script simulates pressing the E key.  

Then player is moving using simple algorithm (2 times left, 2 times right and it repeats instantly.  

Stops when K is pressed.  
 


🧪 Example Use Case  
Automating interactions in 2D/3D games (fighting zombies in lobby in this case)  
