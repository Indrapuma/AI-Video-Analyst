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

## Contoh Input

File SRT (contoh):
```
1
00:00:01,268 --> 00:00:03,729
Turbin kincir angin sejauh mata memandang.

2
00:00:03,917 --> 00:00:05,494
Ada enam lagi yang masih dibuat.
```

## Contoh Output

File Markdown (`video_analysis.md`):
```
## Scene 1
⏱️ Waktu: 00:00:01,268 - 00:00:03,729

🗣️ Dialog:
Turbin kincir angin sejauh mata memandang.

🎬 Deskripsi Visual & Tone:
Di layar tampak hamparan ladang luas dengan deretan turbin kincir angin yang berputar perlahan di bawah langit biru. Suasana terasa tenang dan penuh harapan, menggambarkan kemajuan teknologi ramah lingkungan.

---

## Scene 2
⏱️ Waktu: 00:00:03,917 - 00:00:05,494

🗣️ Dialog:
Ada enam lagi yang masih dibuat.

🎬 Deskripsi Visual & Tone:
Beberapa pekerja tampak sibuk merakit bagian-bagian turbin baru di tengah ladang. Suasana penuh aktivitas dan optimisme, menandakan proses pembangunan yang berkelanjutan.

---
```

## Struktur Project

- `main.py` : Script utama analisis
- `ccFbfwTWkMA.srt` : Contoh file subtitle
- `pyproject.toml` : Konfigurasi project & dependencies

## Kontribusi
Pull request dan issue sangat diterima!

##