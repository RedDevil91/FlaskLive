import atexit

from flask import Flask, render_template, jsonify
import cv2

app = Flask(__name__)
cap = cv2.VideoCapture(0)

atexit.register(cap.release)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_image/')
def get_image():
    _, frame = cap.read()
    ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    resized_frame = cv2.resize(ycrcb, (480, 360))
    _, encoded_img = cv2.imencode(".jpeg", resized_frame)
    return jsonify(encoded_img.flatten().tolist())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
