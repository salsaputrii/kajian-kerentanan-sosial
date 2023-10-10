import streamlit as st
from PIL import Image

st.set_page_config(page_title="Peta Kerentanan dan Klaster", page_icon=":earth_asia:", layout="wide")

st.header("Klaster Tingkat Bahaya Beberapa Desa di Jawa Timur")
klaster = Image.open('rentan_klaster/PETA KLASTER.jpg')
st.image(klaster)

st.header("Perbedaan Persepsi Mengenai Batas Lahan Masyarakat yang Bersinggungan dan/atau Masuk Kawasan Hutan/Bendungan")
satu = Image.open('rentan_klaster/1.jpg')
st.image(satu)

st.header("Perbedaan Persepsi Batas Lahan dengan Lahan Tetangga")
dua = Image.open('rentan_klaster/2.jpg')
st.image(dua)

st.header("Perselisihan Hak Waris/Gangguan Kekerabatan")
tiga = Image.open('rentan_klaster/3.jpg')
st.image(tiga)

st.header("Ketidakmampuan Masyarakat Terhadap Pembayaran Biaya Pra PTSL-PM")
empat = Image.open('rentan_klaster/4.jpg')
st.image(empat)

st.header("Keterbatasan Kuota PTSL-PM (SHAT)")
lima = Image.open('rentan_klaster/5.jpg')
st.image(lima)

st.header("Kendala Masyarakat dalam Pemenuhan Prasyarat untuk Mendaftar PTSL-PM")
enam = Image.open('rentan_klaster/6.jpg')
st.image(enam)

st.header("Keterbatasan Infrastruktur dalam Pelaksanaan PTSL-PM")
tujuh = Image.open('rentan_klaster/7.jpg')
st.image(tujuh)

st.header("Kendala Kondisi Ekstrim dalam Proses Pengukuran")
delapan = Image.open('rentan_klaster/8.jpg')
st.image(delapan)

st.header("Gangguan Fungsi Institusi/Organisasi")
sembilan = Image.open('rentan_klaster/9.jpg')
st.image(sembilan)

st.header("Gangguan Kerukunan Warga")
sepuluh = Image.open('rentan_klaster/10.jpg')
st.image(sepuluh)

st.header("Rendahnya Tingkat Pemahaman/Kapasitas Pelaksanaan dan Peserta PTSL-PM")
sebelas = Image.open('rentan_klaster/11.jpg')
st.image(sebelas)

st.header("Pelaksanaan PTSL Masih Sensitif Kearifan Lokal di Tingkat Desa")
duabelas = Image.open('rentan_klaster/12.jpg')
st.image(duabelas)

st.markdown("#")
st.markdown("#")
st.markdown("#")
st.markdown("#")
st.markdown("***")
st.markdown("Supported by")
st.image("logo.png", width=250)