# Student Task Manager

A simple Flask-based Student Task Manager application packaged with Docker.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000

## Build the Docker image

```bash
docker build -t student-task-manager:v1 .
```

## Run the container

```bash
docker run -d -p 5000:5000 --name student-app student-task-manager:v1
```

Open http://localhost:5000

## Health check

Visit http://localhost:5000/health. A healthy application returns:

```json
{"status": "healthy"}
```
