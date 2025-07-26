from dotenv import load_dotenv
import google.generativeai as genai
import os
import srt

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def load_transcript_srt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        srt_content = file.read()
    subtitles = list(srt.parse(srt_content))
    return subtitles

def split_into_scenes(subtitles, gap_threshold=3):
    scenes = []
    current_scene = {
        "start": subtitles[0].start,
        "end": subtitles[0].end,
        "text": subtitles[0].content
    }
    for i in range(1, len(subtitles)):
        gap = (subtitles[i].start - subtitles[i - 1].end).total_seconds()
        if gap > gap_threshold:
            scenes.append(current_scene)
            current_scene = {
                "start": subtitles[i].start,
                "end": subtitles[i].end,
                "text": subtitles[i].content
            }
        else:
            current_scene["end"] = subtitles[i].end
            current_scene["text"] += " " + subtitles[i].content

    scenes.append(current_scene)
    return scenes

def describe_scene(scene):
    prompt = f"""
    [Scene]
    Waktu: {scene['start']} - {scene['end']}
    Dialog: "{scene['text']}"

    Buat deskripsi visual dari apa yang kemungkinan terlihat di layar, dan jelaskan tone/emosinya (misal: sedih, lucu, epik, mengharukan). Tulis dengan gaya storytelling.
    """
    response = model.generate_content(prompt)
    return response.text.strip()
