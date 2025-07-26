from youtube_transcript_api import YouTubeTranscriptApi
import srt
from datetime import timedelta

def download_srt_from_youtube(video_id, language='id'):
    try:
        ytt_api = YouTubeTranscriptApi().fetch(video_id, languages=[language])
    except Exception as e:
        raise RuntimeError(f"❌ Gagal ambil subtitle: {e}")

    subs = []
    for i, entry in enumerate(ytt_api):
        start = timedelta(seconds=entry.start)
        end = start + timedelta(seconds=entry.duration)
        sub = srt.Subtitle(index=i+1, start=start, end=end, content=entry.text)
        subs.append(sub)

    srt_content = srt.compose(subs)
    return srt_content
