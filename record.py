import subprocess
import os
from datetime import datetime
import time

def record_rtsp_stream(rtsp_url, output_dir, duration, max_retries=10, retry_interval=2):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create a filename with the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"video_{timestamp}.mp4")

    attempt = 0
    while attempt < max_retries:
        # FFmpeg command to capture the RTSP stream
        command = [
            'ffmpeg',
            '-rtsp_transport', 'tcp',  # Use TCP for better reliability
            '-i', rtsp_url,             # Input RTSP URL
            '-c:v', 'copy',             # Copy video codec
            '-c:a', 'copy',             # Copy audio codec
            '-t', str(duration),        # Duration of the recording
            output_file                 # Output file
        ]

        try:
            # Run FFmpeg command
            subprocess.run(command, check=True)
            print(f"Video saved to {output_file}")
            break  # Exit loop if successful
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
            attempt += 1
            if attempt < max_retries:
                print(f"Retrying in {retry_interval} seconds... ({attempt}/{max_retries})")
                time.sleep(retry_interval)
            else:
                print("Max retries reached. Exiting.")

if __name__ == "__main__":
    # Read environment variables
    rtsp_url = os.getenv('RTSP_URL')
    output_dir = "./videos"
    duration = int(os.getenv('DURATION', 60))  # Default to 60 seconds if not set

    if not rtsp_url:
        print("RTSP_URL environment variable is not set. Exiting.")
    else:
        record_rtsp_stream(rtsp_url, output_dir, duration)
