from pytube import YouTube
import os

def download_youtube_video(url, download_path="downloads"):
    try:
        # Create downloads directory if it doesn't exist
        if not os.path.exists(download_path):
            os.makedirs(download_path)
            
        yt = YouTube(url)
        print(f"Downloading: {yt.title}")

        # Download the highest resolution video
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=download_path)

        print(f"Download complete! Video saved to {download_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    video_url = input("Enter the URL of the video: ")
    download_youtube_video(video_url)

if __name__ == "__main__":
    main()
