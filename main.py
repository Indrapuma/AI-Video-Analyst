import streamlit as st
import tempfile
from srt_downloader import download_srt_from_youtube
from video_analyzer import load_transcript_srt, split_into_scenes, describe_scene

st.set_page_config(page_title="🎥 YouTube Scene Visualizer", layout="wide")
st.title("🎬 AI YouTube Scene Describer")
st.markdown("Masukkan ID video YouTube (contoh: `ccFbfwTWkMA`) dan AI akan menganalisis isi subtitle-nya.")

video_id = st.text_input("🔗 YouTube Video ID", placeholder="contoh: ccFbfwTWkMA")

if video_id:
    try:
        # srt_text = download_srt_from_youtube(video_id)
        with open("ccFbfwTWkMA.srt", "r", encoding="utf-8") as file:
            srt_text = file.read()        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".srt") as tmp:
            tmp.write(srt_text.encode("utf-8"))
            tmp_path = tmp.name

        st.success("✅ Subtitle berhasil diambil")

        subtitles = load_transcript_srt(tmp_path)
        scenes = split_into_scenes(subtitles)
        st.info(f"🎞️ Terdeteksi {len(scenes)} scene dari subtitle")

        if st.button("🔍 Jalankan Analisis AI"):
            scenes_with_desc = []
            progress = st.progress(0, text="⏳ Memproses...")
            for i, scene in enumerate(scenes):
                desc = describe_scene(scene)
                scene['description'] = desc
                scenes_with_desc.append(scene)
                progress.progress((i + 1) / len(scenes), text=f"Scene {i + 1}/{len(scenes)}")

            st.success("🎉 Analisis selesai!")

            for i, scene in enumerate(scenes_with_desc):
                with st.expander(f"Scene {i + 1} | ⏱ {scene['start']} - {scene['end']}"):
                    st.markdown(f"**🗣 Dialog:**\n\n{scene['text']}")
                    st.markdown(f"**🎥 Deskripsi Visual:**\n\n{scene['description']}")

    except Exception as e:
        st.error(str(e))
