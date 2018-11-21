import platform
import queue

import numpy as np

if platform.system() == "Windows":
    import cv2
else:
    import picamera
    
image_queue = queue.Queue(maxsize=1)


class CaptureBase:
    image_size = (480, 360)
    frame_rate = 30

    def __init__(self):
        self._cap = None

    def get_image(self):
        return

    def open(self):
        return

    def close(self):
        return

    def __enter__(self):
        self.open()
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return


class WebCameraCapture(CaptureBase):
    def open(self):
        print("ENTER")
        self._cap = cv2.VideoCapture(0)
        return

    def close(self):
        print("EXIT")
        self._cap.release()

    def get_image(self):
        _, frame = self._cap.read()
        ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
        resized_frame = cv2.resize(ycrcb, self.image_size)
        _, encoded_img = cv2.imencode(".jpeg", resized_frame)
        return encoded_img


class PiCameraCapture(CaptureBase):
    def open(self):
        self._cap = picamera.PiCamera()
        self._cap.resolution = self.image_size
        self._cap.framerate = self.frame_rate
        return

    def close(self):
        self._cap.close()
        return

    def get_image(self):
        width, height = self.image_size
        out = np.empty((width, height, 3), dtype=np.uint8)
        self._cap.capture(out, "jpeg")
        return out


if platform.system() == "Windows":
    capture = WebCameraCapture()
else:
    capture = PiCameraCapture()
