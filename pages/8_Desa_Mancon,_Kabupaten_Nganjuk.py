import streamlit as st
import pandas as pd
import geopandas as gpd
from matplotlib import pyplot as plt
from PIL import Image
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Desa Mancon, Kecamatan Wilangan, Kabupaten Nganjuk", page_icon=":round_pushpin:", layout="wide")

st.markdown("<h1 style='text-align: center'>Analisis Desa Mancon, Kabupaten Nganjuk</h1>"
            "<br><i><div style='text-align: center; color: red'>*Silahkan klik salah satu menu di bawah untuk langsung menuju ke bagian yang diinginkan</div>", unsafe_allow_html=True)

st.markdown(f'''
<style>
.button-container {{
    text-align: center;
}}
</style>

<div class="button-container">
<a href='#peta-persil-desa-mancon'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px; margin:-1">
Peta Persil
</button>
</a>

<a href='#persebaran-responden-desa-mancon'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px">
Persebaran Responden
</button>
</a>

<a href='#peta-batas-administrasi-desa-mancon'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Peta Batas Administratif
</button>
</a>

<a href='#peta-batas-hutan-desa-mancon'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px">
Peta Batas Hutan
</button>
</a>

<a href='#peta-klasifikasi-gender-kepemilikan-lahan-desa-mancon'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Peta Klasifikasi Gender
</button>
</a>

<a href='#peta-jangkauan-terhadap-kantor-desa-mancon'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Peta Jangkauan Kantor Desa
</button>
</a>

<a href='#peta-kelerengan-desa-mancon'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Peta Kelerengan
</button>
</a>

<a href='#peta-klasifikasi-luas-persil-desa-mancon'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Peta Klasifikasi Luas Persil
</button>
</a>

<a href='#peta-klasifikasi-petani-gurem-desa-mancon'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Peta Petani Gurem
</button>
</a>

<a href='#peta-tata-guna-lahan-desa-mancon'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Peta Tata Guna Lahan
</button>
</a>

<a href='#pemeringkatan-level-risiko-desa-mancon'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Pemeringkatan Level Risiko
</button>
</a>

<a href='#desa-yang-berada-di-klaster-yang-sama-dengan-desa-mancon-klaster-1'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Desa yang Mirip dengan Mancon
</button>
</a>

</div>
<br>
''',
unsafe_allow_html=True)

# ------------------------------------------------ANALISIS SPASIAL------------------------------------------------------
# st.title("Analisis Spasial")

# PETA PERSIL
st.header(":arrow_forward: Peta Persil Desa Mancon")
coba_map = gpd.read_file('nganjuk_mancon/Nganjuk_Mancon.shp').to_crs(epsg=4326)

fig, ax = plt.subplots()
st.set_option('deprecation.showPyplotGlobalUse', False)
coba_map.plot(ax=ax)
# st.pyplot(fig)

m = folium.Map(location=[coba_map['geometry'].centroid.y.mean(), coba_map['geometry'].centroid.x.mean()], zoom_start=15)
for _, r in coba_map.iterrows():
    # Without simplifying the representation of each borough,
    # the map might not be displayed
    sim_geo = gpd.GeoSeries(r["geometry"]).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function=lambda x: {"fillColor": "orange"})
    # folium.Popup(r["BoroName"]).add_to(geo_j)
    geo_j.add_to(m)
st_data = st_folium(m, width=1000)

# CHART PERSEBARAN RESPONDEN
st.header(":arrow_forward: Persebaran Responden Desa Mancon")
col1, col2 = st.columns([1.5, 1.5])
col1.markdown("")
labels = 'Kelompok Non-rentan', 'Lokasi Khusus', 'KTP Luar', 'Pendatang', 'Belum Mendapat Kuota', 'Kelompok Rentan', 'Konflik'
sizes = [4, 3, 0, 0, 1, 20, 0]
colors = ['#035f03','#5b8915', '#a5c30b', '#fcfb03', '#ecba29', '#fb7b03']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax1.axis('equal')
col1.pyplot(fig1)
tabel_responden = {'KEADAAN TANAH': labels, 'TOTAL': sizes}
df_responden = pd.DataFrame(tabel_responden).to_html(index=False)
df_responden = df_responden.replace('<tr', '<tr style="text-align:center;"')
df_responden = df_responden.replace('<table', '<table style="width:100%; text-align:center"')
col2.markdown("#")
col2.markdown("#")
col2.markdown(df_responden, unsafe_allow_html=True)

# PETA BATAS ADMINISTRATIF
st.header(":arrow_forward: Peta Batas Administratif Desa Mancon")
administratif = Image.open('nganjuk_mancon/PETA BATAS ADMINISTRASI MANCON.jpg')
st.image(administratif)

# PETA BATAS HUTAN
st.header(":arrow_forward: Peta Batas Hutan Desa Mancon")
batas_hutan = Image.open('nganjuk_mancon/PETA BATAS HUTAN DESA MANCON NGANJUKI.jpg')
st.image(batas_hutan)

# PETA GENDER
st.header(":arrow_forward: Peta Klasifikasi Gender Kepemilikan Lahan Desa Mancon")
# col1, col2 = st.columns([3.5, 1.5])
# col1.markdown("")
gender = Image.open('nganjuk_mancon/PETA KLASIFIKASI GENDER MANCON.png')
st.image(gender)

# PETA JANGAKAUAN KE KANTOR DESA
st.header(":arrow_forward: Peta Jangkauan Terhadap Kantor Desa Mancon")
jangkauan = Image.open('nganjuk_mancon/PETA JANGKAUAN TERHADAP KANTOR  DESA  MANCON NGANJUKI.jpg')
st.image(jangkauan)

# PETA KELERENGAN
st.header(":arrow_forward: Peta Kelerengan Desa Mancon")
kelerengan = Image.open('nganjuk_mancon/PETAKELERENGAN DESA MANCONNGANJUKI.jpg')
st.image(kelerengan)

# PETA LUAS PERSIL
st.header(":arrow_forward: Peta Klasifikasi Luas Persil Desa Mancon")
col1, col2 = st.columns([3.5, 1.5])
col1.markdown("")
luas = Image.open('nganjuk_mancon/PETA KLASIFIKASI LUAS DESA MANCON NGANJUKI.jpg')
col1.image(luas)
col2.markdown("")
labels = '< 100 m²', '100 - 400 m²', '400 - 1000 m²', '1000 - 2000 m²', '2000 - 5000 m²', '> 5000 m²'
sizes = [149, 1260, 774, 372, 235, 63]
colors = ['#d7d6fe','#a0a3e9', '#6c7dd4', '#3e5dbd', '#1e49a8', '#003994']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax1.axis('equal')
col2.markdown("##")
col2.pyplot(fig1)
tabel_luas = {'LUAS': labels, 'JUMLAH BIDANG': sizes}
df_luas = pd.DataFrame(tabel_luas).to_html(index=False)
df_luas = df_luas.replace('<tr', '<tr style="text-align:center;"')
df_luas = df_luas.replace('<table', '<table style="width:100%; text-align:center"')
col2.markdown(df_luas, unsafe_allow_html=True)

# PETA PETANI GUREM
st.header(":arrow_forward: Peta Klasifikasi Petani Gurem Desa Mancon")
# col1, col2 = st.columns([3.5, 1.5])
# col1.markdown("")
petani_gurem = Image.open('nganjuk_mancon/PETA KLASIFIKASI PETANIGUREM MANCON.jpg')
st.image(petani_gurem)
# col2.markdown("")
# labels = 'Bukan Petani Gurem', 'Petani Gurem'
# sizes = [8, 331]
# colors = ['#016201','#fe2201']
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
# ax1.axis('equal')
# col2.markdown("#")
# col2.pyplot(fig1)
# tabel_petani_gurem = {'KEADAAN TANAH': labels, 'TOTAL': sizes}
# df_petani_gurem = pd.DataFrame(tabel_petani_gurem).to_html(index=False)
# df_petani_gurem = df_petani_gurem.replace('<tr', '<tr style="text-align:center;"')
# df_petani_gurem = df_petani_gurem.replace('<table', '<table style="width:100%; text-align:center"')
# col2.markdown(df_petani_gurem, unsafe_allow_html=True)

# PETA TATA GUNA
st.header("Peta Tata Guna Lahan Desa Mancon")
col1, col2 = st.columns([3.5, 1.5])
col1.markdown("")
tata_guna_lahan = Image.open('nganjuk_mancon/PETA TATA GUNA LAHAN MANCON.jpg')
col1.image(tata_guna_lahan)
col2.markdown("")
labels = 'Pertanian', 'Ladang', 'Bangunan', 'Fasilitas Umum'
sizes = [501, 189, 1660, 0]
colors = ['#3aa700','#b1e000', '#ffaa01', '#fe0003']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax1.axis('equal')
col2.markdown("#")
col2.pyplot(fig1)
tabel_tata_guna_lahan = {'KEADAAN LAHAN': labels, 'TOTAL': sizes}
df_tata_guna_lahan = pd.DataFrame(tabel_tata_guna_lahan).to_html(index=False)
df_tata_guna_lahan = df_tata_guna_lahan.replace('<tr', '<tr style="text-align:center;"')
df_tata_guna_lahan = df_tata_guna_lahan.replace('<table', '<table style="width:100%; text-align:center"')
col2.markdown(df_tata_guna_lahan, unsafe_allow_html=True)


# --------------------PEMERINGKATAN LEVEL RISIKO------------------------------

st.header(":arrow_forward: Pemeringkatan Level Risiko Desa Mancon")

risiko = {
    'JENIS BAHAYA': ['Bersinggungan dan/atau masuk kawasan hutan/bendungan',
                     'Batas dengan tetangga',
                     'Waris/gangguan kekerabatan',
                     'Biaya pra-PTSL',
                     'Keterbatasan kuota PTSL (SHAT)',
                     'Prasyarat untuk PTSL (riwayat tanah, dll)',
                     'Infrastruktur (internet, dll)',
                     'Teknis pengukuran (topografi, cuaca)',
                     'Gangguan fungsi institusi/organisasi',
                     'Gangguan kerukunan warga (miskomunikasi, dll)',
                     'Tingkat pemahaman/kapasitas rendah',
                     'Tidak sensitif kearifan lokal'],

    'PROBABILITAS/KEMUNGKINAN': ['Mungkin (3)',
                                 'Hampir Tidak Mungkin (1)',
                                 'Sangat Mungkin (4)',
                                 'Hampir Tidak Mungkin (1)',
                                 'Sangat Mungkin (4)',
                                 'Hampir Tidak Mungkin (1)',
                                 'Mungkin (3)',
                                 'Hampir Tidak Mungkin (1)',
                                 'Mungkin (3)',
                                 'Mungkin (3)',
                                 'Hampir Tidak Mungkin (1)',
                                 'Hampir Tidak Mungkin (1)'],

    'KONSEKUENSI/DAMPAK': ['Tidak Signifikan (1)',
                           'Tidak Signifikan (1)',
                           'Kecil (2)',
                           'Tidak Signifikan (1)',
                           'Tidak Signifikan (1)',
                           'Tidak Signifikan (1)',
                           'Kecil (2)',
                           'Tidak Signifikan (1)',
                           'Tidak Signifikan (1)',
                           'Tidak Signifikan (1)',
                           'Tidak Signifikan (1)',
                           'Tidak Signifikan (1)'],

    'TINGKAT RISIKO': ['Menengah (3)',
                       'Rendah (1)',
                       'Menengah (8)',
                       'Rendah (1)',
                       'Menengah (4)',
                       'Rendah (1)',
                       'Menengah (6)',
                       'Rendah (1)',
                       'Menengah (3)',
                       'Menengah (3)',
                       'Rendah (1)',
                       'Rendah (1)'],

    'PRIORITAS': ['IV',
                  'XI',
                  'I',
                  'VIII',
                  'III',
                  'X',
                  'II',
                  'XII',
                  'V',
                  'VI',
                  'IX',
                  'VII']
}

df_risiko = pd.DataFrame(risiko).to_html(index=False)
df_risiko = df_risiko.replace('<tr', '<tr style="text-align:center;"')
df_risiko = df_risiko.replace('<table', '<table style="width:100%; text-align:center"')

st.markdown(df_risiko, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')

# # -----------------------------------------------CLUSTER--------------------------------------------------------------

data = pd.read_csv("klaster.csv")

data = data.rename(columns={'desa': 'DESA', 'kab': 'KABUPATEN', 'kec': 'KECAMATAN'})

data['klaster'] = data['klaster'] + 1

select_kab = 'NGANJUK'
select_desa = 'MANCON'

result_data = data[(data['KABUPATEN'] == select_kab) & (data['DESA'] == select_desa)]
klaster_sebaris = result_data.iloc[0]['klaster']

st.header(f":arrow_forward: Desa yang berada di klaster yang sama dengan Desa {select_desa} (Klaster {klaster_sebaris})")

if result_data.empty:
    st.warning(f'Tidak ada desa yang memiliki kemiripan dengan Desa {select_desa}', icon="❌")
else:
    desa_dengan_klaster_sama = data[data['klaster'] == klaster_sebaris][['DESA', 'KECAMATAN', 'KABUPATEN']]
    tabel_desa_klaster = desa_dengan_klaster_sama.to_html(index=False)
    tabel_desa_klaster = tabel_desa_klaster.replace('<tr', '<tr style="text-align:center;"')
    tabel_desa_klaster = tabel_desa_klaster.replace('<table', '<table style="width:100%; text-align:center"')
    st.markdown(tabel_desa_klaster, unsafe_allow_html=True)





st.markdown("#")
st.markdown("#")
st.markdown("#")
st.markdown("#")
st.markdown("***")
st.markdown("Supported by")
st.image("logo.png", width=250)