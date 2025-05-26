from ultralytics import YOLO
import cv2
import numpy as np
import mss
import ctypes
import time
import keyboard

# SendInput low-level setup

INPUT_KEYBOARD = 1
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_SCANCODE = 0x0008
SendInput = ctypes.windll.user32.SendInput

class KeyboardInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyboardInput),
                ("mi", MouseInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def press_key(scan_code):
    # key press
    key_down = KeyboardInput(0, scan_code, KEYEVENTF_SCANCODE, 0, None)
    input_obj = Input(INPUT_KEYBOARD, Input_I(ki=key_down))
    SendInput(1, ctypes.byref(input_obj), ctypes.sizeof(input_obj))
    time.sleep(0.01)
    # key release
    key_up = KeyboardInput(0, scan_code, KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP, 0, None)
    input_obj = Input(INPUT_KEYBOARD, Input_I(ki=key_up))
    SendInput(1, ctypes.byref(input_obj), ctypes.sizeof(input_obj))

# YOLO + bot logic

def press_move_key(scan_code):
    key_down = KeyboardInput(0, scan_code, KEYEVENTF_SCANCODE, 0, None)
    input_obj = Input(INPUT_KEYBOARD, Input_I(ki=key_down))
    SendInput(1, ctypes.byref(input_obj), ctypes.sizeof(input_obj))
    time.sleep(0.5)
    # key release
    key_up = KeyboardInput(0, scan_code, KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP, 0, None)
    input_obj = Input(INPUT_KEYBOARD, Input_I(ki=key_up))
    SendInput(1, ctypes.byref(input_obj), ctypes.sizeof(input_obj))

model = YOLO("best.pt")
CONFIDENCE_THRESHOLD = 0.3

screenshot_area = {"top": 0, "left": 0, "width": 1920, "height": 1080}

previous_direction = "left"
counter = 0

left = 30
right = 32

with mss.mss() as sct:
    print("Bot was launched. ALT+TAB to the game")
    while True:
        if keyboard.is_pressed("k"):
            break
        screenshot = np.array(sct.grab(screenshot_area))
        frame = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

        results = model(frame, conf=CONFIDENCE_THRESHOLD)

        for box in results[0].boxes:
            conf = box.conf[0].item()
            if conf < CONFIDENCE_THRESHOLD:
                continue

            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            print(f"Zombie was found (conf={conf:.2f}) → click to ({cx}, {cy}) + E")
            for i in range(3):
                press_key(0x12)  # Scan code of "E" button

            if previous_direction == "left":
                press_move_key(left)
                counter += 1
                if counter >= 2:
                    previous_direction = "right"
                    counter = 0
            else:
                press_move_key(right)
                counter += 1
                if counter >= 2:
                    previous_direction = "left"
                    counter = 0
    

