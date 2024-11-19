# webcam-to-ipcamera

## Description
This project is a simple implementation of a webcam to IP camera. It uses OpenCV to capture the webcam feed and Flask to serve the feed as an IP camera. The feed can be accessed by visiting the URL `http://localhost:5000/cctv`. You can access the feed from another device on the same network by replacing `localhost` with the IP address of the host machine.

This project originated from a personal need to monitor a kitten 🐱. At the time, the only tools available were a webcam and a laptop, which inspired the development of this solution.

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
