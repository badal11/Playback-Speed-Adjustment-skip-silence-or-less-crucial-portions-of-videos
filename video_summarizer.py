# video_summarizer.py

import os
from audio_processing import extract_audio_features
from model import train_classifier, load_classifier
from indexing import is_video_indexed, index_video

def summarize_video(video_path):
    # Check if the video has already been indexed
    video_hash = os.path.basename(video_path)
    if is_video_indexed(video_hash):
        print(f"Video {video_path} is already indexed.")
        return

    # Extract audio features
    audio_features = extract_audio_features(video_path)

    # Load the trained model
    clf = load_classifier()

    # Predict loudness based on audio features
    predictions = clf.predict(audio_features)

    # Index the video
    index_video(video_hash, predictions)

if __name__ == "__main__":
    train_classifier()  # Train the classifier (if not already trained)
    video_path = "path/to/your/video.mp4"
    summarize_video(video_path)  # Summarize the video
