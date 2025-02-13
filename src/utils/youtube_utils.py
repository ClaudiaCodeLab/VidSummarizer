import re
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url):
    regex = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/[^\s\n\/]*\?v=|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.match(regex, url)
    return match.group(1) if match else None

def get_transcript(video_id, language='en'):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        return " ".join([item['text'] for item in transcript])
    except Exception as e:
        return f"Error fetching transcript: {e}"