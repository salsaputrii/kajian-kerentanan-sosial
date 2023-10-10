import streamlit as st
import pandas as pd
import geopandas as gpd
from matplotlib import pyplot as plt
from PIL import Image
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Desa Ngadirejo, Kecamatan Jabung, Kabupaten Malang", page_icon=":round_pushpin:", layout="wide")

st.markdown("<h1 style='text-align: center'>Analisis Desa Ngadirejo, Kabupaten Malang</h1>"
            "<br><i><div style='text-align: center; color: red'>*Silahkan klik salah satu menu di bawah untuk langsung menuju ke bagian yang diinginkan</div>", unsafe_allow_html=True)

st.markdown(f'''
<style>
.button-container {{
    text-align: center;
}}
</style>

<div class="button-container">
<a href='#peta-persil-desa-ngadirejo'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px">
Peta Persil
</button>
</a>

<a href='#persebaran-responden-desa-ngadirejo'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px">
Persebaran Responden
</button>
</a>

<a href='#peta-batas-administratif-desa-ngadirejo'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Peta Batas Administratif
</button>
</a>


<a href='#peta-batas-hutan-desa-ngadirejo'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px">
Peta Batas Hutan
</button>
</a>

<a href='#peta-klasifikasi-gender-kepemilikan-lahan-desa-ngadirejo'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Peta Klasifikasi Gender
</button>
</a>

<a href='#peta-jangkauan-terhadap-kantor-desa-ngadirejo'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Peta Jangkauan Kantor Desa
</button>
</a>

<a href='#peta-kelerengan-desa-ngadirejo'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Peta Kelerengan
</button>
</a>

<a href='#peta-klasifikasi-luas-persil-desa-ngadirejo'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Peta Klasifikasi Luas Persil
</button>
</a>

<a href='#peta-klasifikasi-petani-gurem-desa-ngadirejo'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Peta Petani Gurem
</button>
</a>

<a href='#peta-tata-guna-lahan-desa-ngadirejo'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Peta Tata Guna Lahan
</button>
</a>

<a href='#pemeringkatan-level-risiko-desa-ngadirejo'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Pemeringkatan Level Risiko
</button>
</a>

<a href='#desa-yang-berada-di-klaster-yang-sama-dengan-desa-ngadirejo-klaster-2'>
<button
style="background-color:#ffffff; border:1px solid #dcdcdc; font-size:15px; padding:12px;">
Desa yang Mirip dengan Ngadirejo
</button>
</a>
</div>
<br>

''',
unsafe_allow_html=True)

# ------------------------------------------------ANALISIS SPASIAL------------------------------------------------------
# st.title("Analisis Spasial")

# PETA PERSIL
st.header(":arrow_forward: Peta Persil Desa Ngadirejo")
coba_map = gpd.read_file('malang_ngadirejo/Malang_Ngadirejo.shp').to_crs(epsg=4326)

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
st.header(":arrow_forward: Persebaran Responden Desa Ngadirejo")
col1, col2 = st.columns([1.5, 1.5])
col1.markdown("")
labels = 'Kelompok Non-rentan', 'Belum mendapat kuota', 'PBT', 'Lokasi Khusus', 'Pendatang', 'Kelompok Rentan', 'Konflik'
sizes = [2, 2, 0, 2, 2, 14, 3]
colors = ['#035f03','#5b8915', '#a5c30b', '#fcfb03', '#ecba29', '#fb7b03', '#e53110']
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
st.header(":arrow_forward: Peta Batas Administratif Desa Ngadirejo")
administratif = Image.open('malang_ngadirejo/PETA BATAS ADMINISTRASI MALANG NGADIREJO.jpg')
st.image(administratif)

# PETA BATAS HUTAN
st.header(":arrow_forward: Peta Batas Hutan Desa Ngadirejo")
batas_hutan = Image.open('malang_ngadirejo/PETA BATAS HUTAN MALANG NGADIREJO.jpg')
st.image(batas_hutan)

# PETA GENDER
st.header(":arrow_forward: Peta Klasifikasi Gender Kepemilikan Lahan Desa Ngadirejo")
col1, col2 = st.columns([3.5, 1.5])
col1.markdown("")
gender = Image.open('malang_ngadirejo/PETA GENDER KEPEMILIKAN LAHAN MALANG NGADIREJO.jpg')
col1.image(gender)
col2.markdown("")
labels = 'Laki-laki', 'Perempuan'
sizes = [865, 475]
colors = ['#bfe8fe','#ffbee6']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax1.axis('equal')
col2.pyplot(fig1)
tabel_gender = {'GENDER': labels, 'JUMLAH PERSIL': sizes}
df_gender = pd.DataFrame(tabel_gender).to_html(index=False)
df_gender = df_gender.replace('<tr', '<tr style="text-align:center;"')
df_gender = df_gender.replace('<table', '<table style="width:100%; text-align:center"')
col2.markdown(df_gender, unsafe_allow_html=True)

# PETA JANGAKAUAN KE KANTOR DESA
st.header(":arrow_forward: Peta Jangkauan Terhadap Kantor Desa Ngadirejo")
jangkauan = Image.open('malang_ngadirejo/PETA JANGKAUAN TERHADAP KANTOR DESA MALANG NGADIREJO.jpg')
st.image(jangkauan)

# PETA KELERENGAN
st.header(":arrow_forward: Peta Kelerengan Desa Ngadirejo")
kelerengan = Image.open('malang_ngadirejo/PETA KELERENGAN MALANG NGADIREJO.jpg')
st.image(kelerengan)

# PETA LUAS PERSIL
st.header(":arrow_forward: Peta Klasifikasi Luas Persil Desa Ngadirejo")
col1, col2 = st.columns([3.5, 1.5])
col1.markdown("")
luas = Image.open('malang_ngadirejo/PETA KLASIFIKASI LUAS PERSIL MALANG NGADIREJO.jpg')
col1.image(luas)
col2.markdown("")
labels = '< 100 m²', '100 - 400 m²', '400 - 1000 m²', '1000 - 2000 m²', '2000 - 5000 m²', '> 5000 m²'
sizes = [224, 574, 192, 200, 148, 28]
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
st.header(":arrow_forward: Peta Klasifikasi Petani Gurem Desa Ngadirejo")
col1, col2 = st.columns([3.5, 1.5])
col1.markdown("")
petani_gurem = Image.open('malang_ngadirejo/PETA KLASIFIKASI PERSIL PETANI GUREM MALANG NGADIREJO2.jpg')
col1.image(petani_gurem)
col2.markdown("")
labels = 'Bukan Petani Gurem', 'Petani Gurem'
sizes = [49, 249]
colors = ['#016201','#fe2201']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
ax1.axis('equal')
col2.markdown("#")
col2.pyplot(fig1)
tabel_petani_gurem = {'KEADAAN TANAH': labels, 'TOTAL': sizes}
df_petani_gurem = pd.DataFrame(tabel_petani_gurem).to_html(index=False)
df_petani_gurem = df_petani_gurem.replace('<tr', '<tr style="text-align:center;"')
df_petani_gurem = df_petani_gurem.replace('<table', '<table style="width:100%; text-align:center"')
col2.markdown(df_petani_gurem, unsafe_allow_html=True)

# PETA TATA GUNA
st.header(":arrow_forward: Peta Tata Guna Lahan Desa Ngadirejo")
col1, col2 = st.columns([3.5, 1.5])
col1.markdown("")
tata_guna_lahan = Image.open('malang_ngadirejo/PETA TATA RUANG MALANG NGADIREJO.jpg')
col1.image(tata_guna_lahan)
col2.markdown("")
labels = 'Pertanian', 'Pekarangan', 'Perumahan', 'Fasilitas Umum'
sizes = [527, 90, 728, 21]
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

st.header(":arrow_forward: Pemeringkatan Level Risiko Desa Ngadirejo")

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

    'PROBABILITAS/KEMUNGKINAN': ['Hampir Tidak Mungkin (1)',
                                 'Sangat Mungkin (4)',
                                 'Mungkin (3)',
                                 'Mungkin (3)',
                                 'Mungkin (3)',
                                 'Hampir Tidak Mungkin (1)',
                                 'Mungkin (3)',
                                 'Mungkin (3)',
                                 'Hampir Tidak Mungkin (1)',
                                 'Mungkin (3)',
                                 'Mungkin (3)',
                                 'Hampir Tidak Mungkin (1)'],

    'KONSEKUENSI/DAMPAK': ['Tidak Signifikan (1)',
                           'Tidak Signifikan (1)',
                           'Tidak Signifikan (1)',
                           'Sedang (3)',
                           'Tidak Signifikan (1)',
                           'Tidak Signifikan (1)',
                           'Kecil (2)',
                           'Kecil (2)',
                           'Tidak Signifikan (1)',
                           'Tidak Signifikan (1)',
                           'Tidak Signifikan (1)',
                           'Tidak Signifikan (1)'],

    'TINGKAT RISIKO': ['Rendah (1)',
                       'Menengah (4)',
                       'Menengah (3)',
                       'Menengah (9)',
                       'Menengah (3)',
                       'Rendah (1)',
                       'Menengah (6)',
                       'Menengah (6)',
                       'Rendah (1)',
                       'Menengah (3)',
                       'Menengah (3)',
                       'Rendah (1)'],

    'PRIORITAS': ['IX',
                  'IV',
                  'VIII',
                  'I',
                  'V',
                  'XII',
                  'II',
                  'III',
                  'XI',
                  'VII',
                  'VI',
                  'X']
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

select_kab = 'MALANG'
select_desa = 'NGADIREJO'

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



# # ----------------------PETA PERSEBARAN RESPONDEN-----------------------------
#
# st.header("Peta Persebaran Responden Desa Ngadirejo Berdasarkan Kategori")
#
# # Read SHP file
# ngadirejo_map = gpd.read_file('ngadirejo1/PLOTTING_SURVEY_NGADIREJO2.shp')
#
# # lowercase column name
# ngadirejo_map.columns = map(str.lower, ngadirejo_map.columns)
#
# # kelompok rentan
# kelompok_rentan = ['Penerima bantuan', 'Petani gurem', 'Disabilitas', 'Buruh tani', 'Kepala Rumah Tangga Perempuan', 'Berpenghasilan rendah']
#
# # Ambil daftar nilai unik dari kolom kategori
# unique_categories = ngadirejo_map['kategori'].unique()
#
# # Buat daftar warna acak sebanyak nilai kategori yang unik
# category_colors = {}
#
# # Assign warna yang sama untuk kategori tertentu
# for category in unique_categories:
#     if category in kelompok_rentan:
#         category_colors[category] = '#FF5733'  # Misalnya, warna oranye
#     else:
#         category_colors[category] = f'#{random.randint(0, 0xFFFFFF):06x}'
#
# # Ubah nilai kategori menjadi warna yang sesuai
# ngadirejo_map['color'] = ngadirejo_map['kategori'].map(category_colors)
#
# # Tampilkan peta interaktif menggunakan Streamlit
# st.map(ngadirejo_map, use_container_width=True, color='color', size=10, zoom=15)
#
# st.markdown('#')
#
# # ------------------PIE CHART---------------------------------
#
# # bagian sebelah kiri
# col1, col2 = st.columns([1.5, 1.5])
#
# col1.subheader("Kategori Responden")
#
# # Definisikan kelompok kategori rentan
# kelompok_rentan = ['Penerima bantuan', 'Petani gurem', 'Disabilitas', 'Buruh tani', 'Kepala Rumah Tangga Perempuan', 'Berpenghasilan rendah']
#
# # Gabungkan kategori menjadi "kelompok rentan"
# ngadirejo_map['kategori'] = ngadirejo_map['kategori'].apply(lambda x: 'Kelompok Rentan' if x in kelompok_rentan else x)
#
# # Ambil daftar nilai unik dari kolom kategori
# unique_categories = ngadirejo_map['kategori'].unique()
#
# # Buat mapping antara kategori dan warna yang sesuai dengan peta
# category_colors = {category: ngadirejo_map[ngadirejo_map['kategori'] == category]['color'].iloc[0] for category in unique_categories}
#
# # Hitung jumlah setiap kategori
# kategori_counts = ngadirejo_map['kategori'].value_counts().reset_index()
# kategori_counts.columns = ['kategori', 'jumlah']
#
# # Buat pie chart dengan warna yang sesuai
# fig1, ax = plt.subplots()
# colors = [category_colors[cat] for cat in kategori_counts['kategori']]
# ax.pie(kategori_counts['jumlah'], labels=kategori_counts['kategori'], autopct='%1.1f%%', colors=colors, startangle=90)
# ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
# # tampilkan pie chart
# col1.pyplot(fig1)
#
# # ------------------TABEL---------------------------------
#
# col2.subheader("#")
# col2.subheader("#")
# col2.subheader("#")
#
# # Hitung jumlah setiap kategori
# kategori_counts = ngadirejo_map['kategori'].value_counts().reset_index()
# kategori_counts.columns = ['KATEGORI', 'TOTAL']
#
# html_table2 = kategori_counts.to_html(index=False)
#
# # Apply CSS to center-align text
# centered_table2 = f"""
# <style>
# table {{
#     width: 100%;
#     text-align: center;
# }}
# th, td {{
#     text-align: center;
# }}
# </style>
# {html_table2}
# """
#
# col2.markdown(centered_table2, unsafe_allow_html=True)