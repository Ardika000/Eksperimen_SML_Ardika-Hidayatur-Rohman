# Eksperimen Sistem Machine Learning - Data Preprocessing 🚀

Repositori ini merupakan bagian dari tugas akhir (Submission) untuk kelas **Membangun Sistem Machine Learning** di Dicoding. Fokus utama dari repositori ini adalah pada pemenuhan **Kriteria 1**, yaitu melakukan eksperimen *Exploratory Data Analysis* (EDA) secara mendalam dan merancang arsitektur automasi *Data Preprocessing* menggunakan pendekatan MLOps.

## 📊 Dataset
Proyek ini menggunakan **Titanic Dataset** (Kaggle). Dataset ini dipilih karena karakteristiknya yang sangat ideal untuk memamerkan keterampilan *data preprocessing* tingkat lanjut, seperti:
- Penanganan nilai yang hilang (*Missing values imputation*).
- Penghapusan kolom yang tidak memiliki daya prediktif tinggi (Kardinalitas tinggi).
- Penanganan data kategorikal (*One-Hot Encoding* / *Label Encoding*).
- Standardisasi data numerik yang memiliki *skewness* (*StandardScaler*).

## 📂 Struktur Repositori
Repositori ini disusun mengikuti standar *best practice* MLOps untuk memisahkan data mentah, proses eksperimen, skrip automasi, dan data hasil proses.

```text
Eksperimen_SML_Ardika-Hidayatur-Rohman/
├── .github/
│   └── workflows/
│       └── preprocessing.yml                          # Konfigurasi GitHub Actions CI/CD
├── data/
│   └── Titanic-Dataset_raw.csv                        # Data mentah awal (Raw data)
├── preprocessing/
│   ├── Eksperimen_MSML_Ardika-Hidayatur-Rohman.ipynb  # Notebook Eksperimen & EDA
│   └── automate_Ardika-Hidayatur-Rohman.py            # Skrip automasi preprocessing (Pipeline)
│   └── titanic_processed.csvy                         # Hasil data preprocessing
└── README.md