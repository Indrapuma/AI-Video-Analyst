# AI Video Analyst

This project analyzes video subtitles (SRT format) and generates visual scene descriptions using AI.

## Features
- Automatically fetches YouTube subtitles by video ID
- Reads `.srt` subtitle files
- Splits subtitles into scenes based on time gaps
- Generates AI-powered visual descriptions for each scene
- Interactive results display using Streamlit

## Usage

1. **Install dependencies**  
   ```
   uv sync
   ```

2. **Prepare `.env` file**  
   Add your AI API key if required:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

3. **Run the Streamlit app**  
   ```
   streamlit run main.py
   ```

4. **Access the app**  
   Enter a YouTube video ID, click the analyze button, and view the scene descriptions.

## Example Input

App input:
- YouTube video ID: `ccFbfwTWkMA`

Sample SRT file:
```
1
00:00:01,268 --> 00:00:03,729
Wind turbines as far as the eye can see.

2
00:00:03,917 --> 00:00:05,494
Six more are still being built.
```

## Example Output

Streamlit app display:
- Scene 1 | ⏱ 00:00:01,268 - 00:00:03,729  
  **🗣 Dialog:**  
  Wind turbines as far as the eye can see.  
  **🎥 Visual Description:**  
  A wide field filled with slowly spinning wind turbines under a blue sky. The atmosphere is calm and hopeful, reflecting progress in green technology.

- Scene 2 | ⏱ 00:00:03,917 - 00:00:05,494  
  **🗣 Dialog:**  
  Six more are still being built.  
  **🎥 Visual Description:**  
  Workers are assembling new turbine parts in the field. The scene is busy and optimistic, showing ongoing development.

## Project Structure

- `main.py` : Main Streamlit app
- `srt_downloader.py` : YouTube subtitle downloader module
- `video_analyzer.py` : Scene analysis and AI description module
- `ccFbfwTWkMA.srt` : Example subtitle file
- `pyproject.toml` : Project configuration & dependencies

## Contributing
Pull requests and issue sangat diterima!