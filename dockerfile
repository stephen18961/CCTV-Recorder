# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# install ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the rest of the application code into the container
COPY . .

# Set environment variables for the container
ENV RTSP_URL=""
ENV DURATION="60"

# Command to run the application
CMD ["python", "record.py"]