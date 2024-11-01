# webcam-to-ipcamera

## Description
This project is a simple implementation of a webcam to IP camera. It uses OpenCV to capture the webcam feed and Flask to serve the feed as an IP camera.

### Create virtual environment
```bash
python3 -m venv venv
```

### Activate virtual environment
```bash
source venv/bin/activate
```

### Install requirements
```bash
pip install -r requirements.txt
```

### Run the server
```bash
python app.py
```

> [!NOTE]  
> If you have multiple webcams, you can specify the webcam index in the `app.py` file. You can run the `list_webcams.py` script to list all the available webcams and their indexes.