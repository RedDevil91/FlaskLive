import atexit
import queue
import threading

from flask import Flask, render_template, jsonify

from camera import capture

queue = queue.Queue(maxsize=10)


class CameraThread(threading.Thread):
    def __init__(self):
        super(CameraThread, self).__init__(daemon=True)
        return

    def run(self):
        capture.open()
        while True:
            if queue.empty():
                image = capture.get_image()
                queue.put_nowait(image)

    @staticmethod
    def close():
        capture.close()


app = Flask(__name__)
thread = CameraThread()
atexit.register(thread.close)


@app.route('/')
def index():
    if not thread.isAlive():
        thread.start()
    return render_template('index.html')


@app.route('/get_image/')
def get_image():
    image = queue.get()
    return jsonify(image.flatten().tolist())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
