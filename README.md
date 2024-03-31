# SmartControl

SmartControl is a software application that allows users to control their computer using hand gestures, voice commands, and voice typing. It includes features such as hand tracking, speech recognition, and automation of tasks based on user inputs.

## Introduction

SmartControl combines computer vision with natural language processing to create an interactive control system for your computer. Using a webcam, the application tracks hand movements to simulate mouse control and perform actions like clicking, scrolling, and typing. It also integrates speech recognition to interpret voice commands, allowing users to interact with the system through spoken instructions. Additionally, SmartControl supports voice typing, enabling users to dictate text using their voice.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/SmartControl.git
   ```
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Download NLTK data:
   ```sh
   python -c "import nltk; nltk.download('punkt')"

   ```
4. Train the machine learning model:

    - Ensure you have `intents.json` with training data.
    - Run `training.py` to train the model:
    ```sh
    python training.py
    ```
   Once the model is trained, update the model.tflearn file.  
5. Run the application:  
    ```sh
    python hand.py
    ```

## Features

- Hand tracking for mouse control and gestures.
- Speech recognition for voice commands.
- Voice typing for dictating text.
- Automated task execution based on user inputs.
- Easy setup and installation with minimal dependencies.
- Supports common operating system functions such as window management and application control.

## Usage

1. Start the application by running `hand.py`.
2. Use hand gestures to control the mouse cursor:
   - Two fingers for clicking.
   - Three fingers for scrolling.
   - Four fingers for voice input and voice typing.
3. Speak commands such as "assistant" to activate voice mode and interact with the system using natural language.
4. Perform tasks like opening applications, switching windows, or executing custom commands by voice or hand gestures.

## Code
- `hand.py` is explained in [hand.md](hand.md)
- `training.py` is explained in [training.md](training.md)
- `voicer.py` is explained in [voicer.md](voicer.md)

## Tutorials

Here are tutorials for the technologies used in SmartControl:

- [MediaPipe Getting Started Guide](https://google.github.io/mediapipe/getting_started/python.html)
- [MediaPipe Tutorials](https://google.github.io/mediapipe/solutions/solutions.html)
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
- [TensorFlow for Beginners](https://www.tensorflow.org/tutorials/quickstart/beginner)
- [NLTK Book](http://www.nltk.org/book/)
- [NLTK Tutorials](https://www.nltk.org/howto/)
- [Tkinter Tutorial](https://docs.python.org/3/library/tkinter.html)
- [Python GUI Programming With Tkinter](https://realpython.com/python-gui-tkinter/)
- [gTTS Documentation](https://gtts.readthedocs.io/en/latest/)
- [gTTS Tutorial](https://www.geeksforgeeks.org/convert-text-to-speech-in-python/)
- [TFLearn Documentation](http://tflearn.org/)
- [TFLearn Tutorials](https://github.com/tflearn/tflearn/tree/master/examples)
- [OpenCV Tutorials](https://docs.opencv.org/master/d9/df8/tutorial_root.html)
- [Learn OpenCV](https://www.learnopencv.com/)
- [NLTK Stemming](https://www.nltk.org/howto/stem.html)
- [LancasterStemmer Example](https://www.nltk.org/api/nltk.stem.html#module-nltk.stem.lancaster)

