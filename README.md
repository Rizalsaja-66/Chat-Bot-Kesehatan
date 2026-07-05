# Project UAS: NLP Chatbot Kesehatan

Ini adalah project chatbot sederhana berbasis Natural Language Processing (NLP) untuk menjawab pertanyaan umum seputar kesehatan. Project ini dikembangkan menggunakan **Sentence-Transformers** untuk mencari kemiripan semantik antara pertanyaan pengguna dengan dataset yang telah disusun, serta menggunakan **Streamlit** untuk antarmuka web interaktif.

## Struktur Direktori
- `app.py`: Script utama aplikasi web berbasis Streamlit. Menangani UI (User Interface) dan interaksi chat.
- `chatbot_logic.py`: Script backend NLP. Memuat model `sentence-transformers`, melakukan embedding pada dataset, dan menghitung *Cosine Similarity* untuk mendapatkan jawaban paling relevan.
- `dataset_kesehatan.json`: Dataset pengetahuan kesehatan. Berisi puluhan pasangan pertanyaan dan jawaban seputar penyakit, gaya hidup sehat, nutrisi, dan pertolongan pertama.
- `requirements.txt`: Daftar library Python yang dibutuhkan.

## Cara Instalasi
1. Pastikan Anda memiliki Python yang sudah terinstall di sistem.
2. Buka terminal atau command prompt, arahkan ke folder project ini.
3. Install semua kebutuhan library dengan menjalankan perintah:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Menjalankan Aplikasi
Setelah instalasi selesai, jalankan perintah berikut di terminal:
```bash
streamlit run app.py 
python -m streamlit run app.py
```
Aplikasi akan terbuka secara otomatis di browser default Anda (biasanya di `http://localhost:8501`).

## Cara Kerja (Penjelasan untuk Laporan)
1. **Dataset**: Pengetahuan bot bersumber dari `dataset_kesehatan.json`.
2. **Model NLP**: Aplikasi memuat model pre-trained `paraphrase-multilingual-MiniLM-L12-v2` menggunakan library `sentence-transformers`. Model ini bagus untuk bahasa Indonesia.
3. **Embedding**: Saat aplikasi mulai, semua 'pertanyaan' di dataset diubah menjadi representasi vektor numerik (embedding).
4. **Pencarian Jawaban (Similarity)**: Ketika user mengetik pertanyaan, pertanyaan tersebut juga diubah menjadi vektor. Sistem lalu menghitung *Cosine Similarity* (kedekatan jarak) antara vektor user dengan semua vektor pertanyaan di dataset.
5. **Output**: Jawaban dari pertanyaan di dataset yang memiliki similarity tertinggi (melewati batas/threshold tertentu) akan ditampilkan ke pengguna layaknya sedang chatting.
