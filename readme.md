# RTSP Stream Recorder

This project provides a Python application for recording RTSP streams using FFmpeg. The application is dockerized and configured to run multiple instances using Docker Compose, allowing you to record from multiple CCTV cameras simultaneously.

## Features

- Records RTSP streams to MP4 files.
- Configurable recording duration and RTSP URL via environment variables.
- Scalable setup using Docker Compose to handle multiple RTSP streams.

## Requirements

- Docker
- Docker Compose

## Project Structure

- `Dockerfile`: Docker configuration to build the application image.
- `requirements.txt`: Python dependencies for the application.
- `record_rtsp.py`: Python script that records the RTSP stream.
- `docker-compose.yml`: Docker Compose configuration for running multiple instances.

## Setup

### 1. Clone the Repository

### 2. Build and Run the Docker Containers

```bash
docker-compose up --build
```

This command builds the Docker images and starts the containers defined in `docker-compose.yml`.

## Configuration

### Environment Variables

Each service in the Docker Compose setup uses the following environment variables:

- `RTSP_URL`: The RTSP stream URL to record from.
- `DURATION`: The duration (in seconds) for which to record each video segment.

### Example Configuration

In `docker-compose.yml`, you can define multiple services for different RTSP streams:

```yaml
services:
  cctv1:
    network_mode: host
    build: .
    environment:
      - RTSP_URL=rtsp://host.docker.internal:8554/cctv_c3
      - DURATION=60
    volumes:
      - ./videos/cctv1:/app/videos
    deploy:
      replicas: 1

  cctv2:
    network_mode: host
    build: .
    environment:
      - RTSP_URL=rtsp://your_camera_ip2:port/stream
      - DURATION=60
    volumes:
      - ./videos/cctv2:/app/videos
    deploy:
      replicas: 1
```

Add more services as needed for additional RTSP streams. Make sure that the volume is mapped to a different path for each cctv, so that there would be no conflicts.

## File Output

Recorded videos are saved to the `./videos` directory, which is mounted as a volume in the Docker containers. Each video file is named with a timestamp for easy identification.

## Troubleshooting

- **No Video Output**: Ensure that the `RTSP_URL` is correct and accessible from within the Docker container. Check the container logs for any FFmpeg errors.
- **Environment Variables Not Set**: Verify that the environment variables are correctly specified in `docker-compose.yml`.