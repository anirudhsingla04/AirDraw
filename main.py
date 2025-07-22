import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import streamlit as st
from PIL import Image
import google.generativeai as genai

# Streamlit UI setup
st.set_page_config(layout='wide')
st.image('mathgest.png')

col1, col2 = st.columns([2, 1])
with col1:
    run = st.checkbox('Run', value=True)
    FRAME_WINDOW = st.image([])

with col2:
    st.title("Answer")
    output_text_area = st.empty()

# AI configuration
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')

# Video capture setup
cap = cv2.VideoCapture(0)
cap.set(3, 1920)  # Set width to 1920
cap.set(4, 1080)  # Set height to 1080
cap.set(cv2.CAP_PROP_FPS, 30)  # Set frame rate to 30

# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.8, minTrackCon=0.5)

def getHandInfo(img):
    hands, img = detector.findHands(img, draw=True, flipType=True)
    if hands:
        hand1 = hands[0]
        lmList = hand1["lmList"]
        fingers = detector.fingersUp(hand1)
        return fingers, lmList
    else:
        return None, None

def draw(info, prev_pos, canvas):
    fingers, lmList = info
    current_pos = None
    if fingers == [0, 1, 0, 0, 0]:  # Index finger up
        current_pos = lmList[8][0:2]
        if prev_pos is None:
            prev_pos = current_pos
        cv2.line(canvas, tuple(prev_pos), tuple(current_pos), (255, 0, 255), 10)
    elif fingers == [1, 1, 1, 1, 1]:  # All fingers up (reset canvas)
        canvas = np.zeros_like(canvas)
    return current_pos, canvas

def sendToAI(model, canvas, fingers):
    if fingers == [1, 0, 0, 0, 0]:  # thumb up
        pil_image = Image.fromarray(canvas)
        response = model.generate_content(["Solve this math problem", pil_image])
        return response.text
    return ''

prev_pos = None
canvas = None
output_text = ''

while run:
    success, img = cap.read()
    if not success:
        break
    img = cv2.flip(img, 1)
    
    # Apply Gaussian blur to smooth the image and reduce noise
    img = cv2.GaussianBlur(img, (5, 5), 0)

    if canvas is None:
        canvas = np.zeros_like(img)

    info = getHandInfo(img)
    if info[0] is not None:
        prev_pos, canvas = draw(info, prev_pos, canvas)
        output_text = sendToAI(model, canvas, info[0])

    image_combined = cv2.addWeighted(img, 0.7, canvas, 0.3, 0)
    FRAME_WINDOW.image(image_combined, channels="BGR")

    if output_text:
        output_text_area.subheader(output_text)

    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
