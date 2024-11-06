import cv2
from flask import Flask, Response
from datetime import datetime

app = Flask(__name__)

def apply_night_filter(frame):
    # Convert the frame to grayscale
    night_filter = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return night_filter

def generate_frames():
    camera = cv2.VideoCapture(0)  # may need to change the index depending on how many cameras are connected
    while True:
        success, frame = camera.read()  # Read a frame from the webcam
        if not success:
            break
        else:
            # Uncomment to apply night vision effect
            frame = apply_night_filter(frame)
            
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Define text overlay
            text = f'Date & Time: {current_time}'
            text2 = f'Camera Name: '

            # Define the position, font, scale, color, and thickness
            position = (10, 30)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.7
            color = (255, 255, 255)  # White color
            thickness = 2

            # Overlay the text on the frame
            cv2.putText(frame, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
            cv2.putText(frame, text2, (10, 60), font, font_scale, color, thickness, cv2.LINE_AA)

            ret, buffer = cv2.imencode('.jpg', frame)  # Encode the frame as JPEG
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # Concatenate frame one by one and show result

@app.route('/cctv')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)