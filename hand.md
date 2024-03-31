# Main file

Tracks hand movements and performs actions based on gestures, such as clicking, scrolling, and recognizing speech commands.

## Libraries

- `cv2`: OpenCV for image processing.
- `tkinter`: GUI library for creating the application interface.
- `mediapipe`: MediaPipe library for hand tracking.
- `speech_recognition`: Library for speech recognition.
- `pyautogui`: Library for controlling the mouse and keyboard.
- `numpy`: Library for numerical operations.
- `math`: Math library for calculations.
- `gtts`: Google Text-to-Speech for converting text to speech.
- `os`: Library for operating system-related functions.
- `playsound`: Library for playing sound files.

## Functions

1. `count_fingers(hand_landmarks)`: Counts the number of fingers extended based on hand landmarks.
2. `get_click(hand_landmarks, image, h, w)`: Simulates a mouse click based on hand position.
3. `auto_scroll(hand_landmarks, image, h, w)`: Scrolls the screen based on hand position.
4. `speak(text)`: Converts text to speech and plays the audio.
5. `commands(tag, got)`: Executes commands based on recognized speech tags.

## Main Functions

- `start_camera()`: Initializes the webcam for hand tracking.
- `pause_camera()`: Pauses the webcam feed.
- `stop_camera()`: Stops the webcam feed and closes the application.
- `update_frame()`: Updates the video frame with hand tracking and gesture recognition.

## Hand Tracking and Gestures

- Uses MediaPipe to detect hand landmarks and track finger positions.
- Recognizes gestures such as clicking (2 fingers), scrolling (3 fingers), and speech commands (4 fingers).
- Hand movements control the mouse cursor, simulate clicks, and scroll the screen.

## Speech Recognition

- Uses speech recognition to convert spoken commands into text.
- Recognizes commands such as activating/deactivating the assistant and executing tasks based on recognized tags.

## GUI Interface

- Creates a tkinter window for the application.
- Includes buttons for starting, pausing, and stopping the hand tracking functionality.


