from flask import Flask, render_template, jsonify

from camera import capture, image_queue

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_image/')
def get_image():
    encoded_img = capture.get_image()
    return jsonify(encoded_img.flatten().tolist())


if __name__ == '__main__':
    capture.open()
    app.run(debug=True, host='0.0.0.0')
    capture.close()
