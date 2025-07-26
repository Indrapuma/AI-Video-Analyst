# AI Video Analyst

Project ini menganalisis subtitle video (format SRT) dan menghasilkan deskripsi visual serta tone/emosi tiap scene menggunakan Gemini AI.

## Fitur
- Membaca file subtitle `.srt`
- Membagi subtitle menjadi scene berdasarkan jeda waktu
- Menghasilkan deskripsi visual dan tone tiap scene dengan AI
- Menyimpan hasil analisis ke file Markdown

## Cara Pakai

1. **Install dependencies**  
   ```
   uv pip install -r requirements.txt
   ```
   atau jika pakai pyproject.toml:
   ```
   uv sync
   ```

2. **Siapkan file `.env`**  
   Tambahkan API key Gemini:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

3. **Jalankan script**  
   ```
   python main.py
   ```

4. **Hasil**  
   File `video_analysis.md` akan berisi analisis scene dari subtitle.

## Struktur Project

- `main.py` : Script utama analisis
- `ccFbfwTWkMA.srt` : Contoh file subtitle
- `pyproject.toml` : Konfigurasi project & dependencies

## Kontribusi
Pull request dan issue sangat diterima!

##