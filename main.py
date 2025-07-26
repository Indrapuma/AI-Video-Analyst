from dotenv import load_dotenv
import google.generativeai as genai
import os
import srt

# Load API key dari .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Init Gemini model (bisa pilih gemini-pro atau gemini-1.5)
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


def save_to_markdown(scenes_with_descriptions, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for i, scene in enumerate(scenes_with_descriptions):
            f.write(f"## Scene {i+1}\n")
            f.write(f"⏱️ Waktu: {scene['start']} - {scene['end']}\n\n")
            f.write(f"🗣️ Dialog:\n{scene['text']}\n\n")
            f.write(f"🎬 Deskripsi Visual & Tone:\n{scene['description']}\n\n")
            f.write("---\n\n")


def main():
    srt_file_path = "ccFbfwTWkMA.srt"
    subtitles = load_transcript_srt(srt_file_path)
    scenes = split_into_scenes(subtitles)

    scenes_with_description = []
    for scene in scenes:
        print(f"Processing scene from {scene['start']} to {scene['end']}")
        description = describe_scene(scene)
        scene['description'] = description
        scenes_with_description.append(scene)

    save_to_markdown(scenes_with_description, "video_analysis.md")
    print("✅ Video analysis saved to video_analysis.md")


if __name__ == "__main__":
    main()
