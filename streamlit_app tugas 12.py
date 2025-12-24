import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =======================
# TITLE
# =======================
st.title("Web Pengaderan Elektro 2025")

# =======================
# HEADER
# =======================
st.header("Kelompok Circulex")

# =======================
# SUBHEADER
# =======================
st.subheader("Program Pengaderan Mahasiswa Teknik Elektro")

# =======================
# CAPTION
# =======================
st.caption("Politeknik Negeri Batam • Teknik Elektro • Himpunan Mahasiswa Elektro")
st.caption("Dibuat Oleh : Nur Atika Fadillah 4232401028 RPE 3A PAGI")

# =======================
# TEXT (PARAGRAF)
# =======================
st.text("""
Kelompok Circulex merupakan salah satu kelompok dalam kegiatan pengaderan 
mahasiswa baru Teknik Elektro 2025. Kelompok ini bertujuan untuk membentuk 
karakter mahasiswa yang disiplin, bertanggung jawab, dan mampu bekerja dalam tim.

Melalui kegiatan ini, peserta akan dibekali dengan nilai kepemimpinan, 
kerjasama, serta pemahaman tentang dunia akademik dan organisasi di Teknik Elektro.
""")

# =======================
# CODE (POTONGAN CODE)
# =======================
st.code("""
import streamlit as st
st.title("Hello Pengaderan Elektro!")
""", language="python")

# =======================
# DATA FRAME
# =======================
data = {
    "Nama": ["Alvian", "Satrio", "Dika", "Benedicta", "Alya", "Zilgani"],
    "Prodi": ["Mekatronika", "Teknologi Rekayasa Elektronika", "Teknologi Rekayasa Pembangkit Energi", "Elektronika Manukfaktur", "Robotika", "Intrumentasi"],
    "Kehadiran (%)": [90, 85, 95, 88, 92, 82]
}

df = pd.DataFrame(data)

st.subheader("Data Anggota Kelompok Circulex")
st.dataframe(df)

# =======================
# CHART
# =======================
st.subheader("Grafik Kehadiran Anggota")

fig, ax = plt.subplots()
ax.bar(df["Nama"], df["Kehadiran (%)"])
ax.set_xlabel("Nama Anggota")
ax.set_ylabel("Kehadiran (%)")
ax.set_title("Persentase Kehadiran Anggota Circulex")

st.pyplot(fig)

# =======================
# FOOTER
# =======================
st.caption("© 2025 Pengaderan Teknik Elektro — Kelompok Circulex")

