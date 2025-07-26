from youtube_transcript_api import YouTubeTranscriptApi
import json
import srt
from datetime import timedelta

video_id = "ccFbfwTWkMA"

ytt_api = YouTubeTranscriptApi().fetch(video_id, languages=['id'])

# for item in ytt_api:
#     print(item)

subs = []
for i, entry in enumerate(ytt_api):
    start = timedelta(seconds=entry.start)
    end = start + timedelta(seconds=entry.duration)
    sub = srt.Subtitle(index=i+1, start=start, end=end, content=entry.text)
    subs.append(sub)

srt_content = srt.compose(subs)
with open(f"{video_id}.srt", "w", encoding="utf-8") as f:
    f.write(srt_content)