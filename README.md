# AirDraw: AI-Powered Gesture-Based Drawing and Math Recognition

![AirDraw Logo](mathgest.png)

## Overview

**AirDraw** is an innovative application that combines computer vision and AI to enable users to draw in the air using hand gestures. The application captures these gestures through a webcam, processes them to create a virtual drawing, and uses AI to recognize the drawings or solve mathematical problems.

## Features

- **Gesture-Based Drawing**: Draw in the air using hand gestures captured by a webcam.
- **AI Recognition**: Recognize and interpret the drawings, including solving mathematical problems.
- **Interactive UI**: A user-friendly interface powered by Streamlit for an engaging experience.
- **Real-Time Processing**: Provides real-time feedback and results as you draw.

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/Sakshi081/AirDraw.git
   cd AirDraw
2. **Install Required Packages**
   
   pip install -r requirements.txt

4. **Usage**
   
   Run the Streamlit Application:

   1. streamlit run main.py

   2. **Interact with the Application:**
      
      Use the checkbox to start/stop the drawing session.
      
      **Use the following gestures:**
      
          Index Finger Up: Draw on the virtual canvas.
          All Fingers Up: Erase the canvas.
          Thumb Up: Send the drawing to the AI for recognition and interpretation.

</br>

4. **Requirements**

    -Python 3.x</br>
    -OpenCV</br>
    -CVZone</br>
    -Streamlit</br>
    -Google Generative AI</br>
    -Pillow</br>
    -NumPy


## How It Works

  -**Hand Detection**: Uses OpenCV and CVZone to detect hand gestures and track the index finger.</br>
  -**Drawing Capture**: Captures the drawing based on the movement of the index finger.</br>
  -**AI Processing**: Sends the captured drawing to an AI model for recognition and interpretation.</br>
  -**Display Results**: Displays the original image, the drawing on a virtual canvas, and the AI-generated interpretation.</br>

## Acknowledgements
OpenCV

CVZone

Streamlit

Google Generative AI
