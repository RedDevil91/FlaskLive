from flask import Flask, render_template, make_response
import cv2
import base64

app = Flask(__name__)
cap = cv2.VideoCapture(0)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_image/')
def get_image():
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized_frame = cv2.resize(gray, (480, 360))
    _, encoded_img = cv2.imencode(".png", resized_frame)
    image_base64 = base64.encodebytes(encoded_img.tobytes())
    resp = make_response(image_base64)
    resp.headers.set('Content-Type', 'image/png')
    return resp
