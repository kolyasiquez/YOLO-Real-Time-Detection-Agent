# YOLO-Real-Time-Detection-Agent
Real-time object detection &amp; low-level input automation using YOLOv8, OpenCV, and Windows API

🧠 Real-time Object Detection & Response Automation  
This project demonstrates the application of `computer vision (YOLOv8)`, low-level input emulation (via `Windows API`), and screen capture (`MSS`) to create a real-time automation system for the game (in this case).

📊 Dataset & Training  
The object detection model was trained using a small custom dataset (I took screenshots in the game by myself) created with `Roboflow`. I used only one class named "zombies" to detect them.  
The model was trained with YOLOv8 for 50 epochs on this dataset, achieving good precision in the target detection scenario, especially considering dataset's small size.
I used this command to train the model:
```
yolo task=detect mode=train model=yolov8n.pt data=path/to/data.yaml epochs=50 imgsz=640
```

👁 Screenshot showing model's detection of zombies on the first validation batch:   

<img src="https://github.com/user-attachments/assets/37ba0730-9d31-4bf4-881c-796d0da138f8" width="480"/>  

📁 Model File  
The detection relies on a custom-trained model file `best.pt`, which contains the weights obtained after training YOLOv8 on the "zombies" dataset.
  
⚙️ Tech Stack  
Python 
Ultralytics YOLOv8  
OpenCV  
MSS (Screen capture)  
ctypes (Windows input emulation)  
keyboard (keypress monitoring)   

📦 Installation  
1. **Install Python 3.12+**  
   (https://www.python.org/downloads/)

2. **Clone the repository**
   ```cmd
   git clone https://github.com/your-username/YOLO-Real-Time-Detection-Agent.git
   cd YOLO-Real-Time-Detection-Agent
   
Install dependencies:
  `
  pip install -r requirements.txt
  `   
Make sure best.pt is in the root folder (or change the path in the script), then:

  ```cmd
  python YOLO-Real-Time-Detection-Agent.py
```

🚀 How It Works  
The screen is continuously captured from the specified region.  

Each frame is passed to YOLOv8, which detects targets (zombies in this case).  

If a target is found with confidence above threshold:  

The script simulates pressing the E key.  

Then player is moving using simple algorithm (2 times left, 2 times right and it repeats instantly.  

Stops when K is pressed.  
 


🧪 Example Use Case  
Automating interactions in 3D games (in this case fighting zombies in lobby)   

⚠️ Disclaimer:  
This GIF showcases gameplay from PANICORE used solely for demonstrating the object detection model’s performance. All game content belongs to their respective owners. This is not an official promotion or endorsement.  

![model_is_working](https://github.com/user-attachments/assets/b7786aca-a9e6-4a7c-8a10-0b0a128b3d52)

