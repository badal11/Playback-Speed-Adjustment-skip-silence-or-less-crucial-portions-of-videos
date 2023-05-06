import os
import requests

SERVER_URL = 'https://videosummarizer.soptik.tech/'

def is_video_indexed(video_hash):
    try:
        response = requests.get(SERVER_URL + video_hash)
        return response.status_code == 200
    except requests.RequestException:
        return False

def index_video(video_hash, predictions):
    video_data = "\n".join(f"{i * AUDIO_CHUNK_SIZE} {int(predictions[i])}" for i in range(len(predictions)))
    with open(f"{video_hash}.txt", 'w') as output_file:
        output_file.write(video_data)

    # Placeholder: Simulate sending data to the server for indexing
    requests.post(SERVER_URL, files={'file': open(f"{video_hash}.txt", 'rb')})
