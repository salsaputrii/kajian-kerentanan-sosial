# IMPORT LIBRARY
import geopandas as gpd
import streamlit as st
import pandas as pd
import pandas_bokeh
pandas_bokeh.output_file("bpn.html")
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Analisis Kerentanan Sosial", page_icon=":earth_asia:", layout="wide")

# add_logo("logo_small.png", height=50)

# TITLE
st.title("Analisis Kerentanan Sosial Provinsi Jawa Timur")
st.markdown("###")

# READ SHP FILE
bpn_map = gpd.read_file('batas_desa/BATAS_DESA_JATIM.shp')

# # CREATE PLOT FROM SHP FILE
# # Create a plot
# fig, ax = plt.subplots(figsize=(30, 10))
#
# st.set_option('deprecation.showPyplotGlobalUse', False)
#
# # Plot the GeoDataFrame
# bpn_map.plot(ax=ax)




# Create a folium map centered at a specific location
m = folium.Map(location=[bpn_map['geometry'].centroid.y.mean(), bpn_map['geometry'].centroid.x.mean()], zoom_start=8)

# # Iterate over the GeoDataFrame rows and add each geometry to the map
# for idx, row in bpn_map.iterrows():
#     geom = row['geometry']
#     folium.GeoJson(geom).add_to(m)

# ADD POP UP INFO FOR 14 DESA
# Load village data (replace this with your own DataFrame)
village_data = pd.DataFrame({
    'latitude': [-7.977497,
                 -7.972366,
                 -7.99269,
                 -8.12738,
                 -8.011067,
                 -8.0022901,
                 -7.432432,
                 -7.562588,
                 -7.760288,
                 -7.633579,
                 -8.144528,
                 -8.214888,
                 -8.13278,
                 -8.238039],

    'longitude': [112.797999,
                  112.769333,
                  113.012049,
                  113.076584,
                  113.7701558,
                  113.9749953,
                  112.01696,
                  111.832128,
                  111.346833,
                  111.259857,
                  111.607264,
                  111.555691,
                  111.153539,
                  111.221155
                  ],

    'village_name': ["Ngadirejo",
                     "Sukopuro",
                     "Argosari",
                     "Pasrujambe",
                     "Gunungsari",
                     "Gunosari",
                     "Bajang",
                     "Mancon",
                     "Mategal",
                     "Tapak",
                     "Ngrandu",
                     "Petung",
                     "Karanggede",
                     "Worawari"],

    'kecamatan': ["Jabung",
                  "Jabung",
                  "Senduro",
                  "Pasrujambe",
                  "Maesan",
                  "Tlogosari",
                  "Ngluyu",
                  "Wilangan",
                  "Parang",
                  "Panekan",
                  "Suruh",
                  "Dongko",
                  "Arjosari",
                  "Kebonagung"],

    'kabupaten': ["Malang",
                  "Malang",
                  "Lumajang",
                  "Lumajang",
                  "Bondowoso",
                  "Bondowoso",
                  "Nganjuk",
                  "Nganjuk",
                  "Magetan",
                  "Magetan",
                  "Trenggalek",
                  "Trenggalek",
                  "Pacitan",
                  "Pacitan"],

    'gambaran': [# Ngadirejo
                f"<br> Memiliki total luas wilayah sebesar 143.140 m², Desa Ngadirejo terbagi menjadi 2 dusun, yaitu Dusun Krajan Bendolawang dan Dusun Kampunganyar. Dengan total penduduk sebanyak 2079 jiwa, Desa Ngadirejo terdiri dari penduduk perempuan sebanyak 1028 jiwa dan penduduk laki-laki sebanyak 1051 jiwa. Sementara itu, jumlah kepala keluarga di desa ini adalah sebanyak 714 KK. Jarak kantor pemerintahan Desa Ngadirejo ke kantor Kecamatan Jabung adalah sejauh 25 km. Sedangkan, jarak kantor Desa Ngadirejo ke kantor Kabupaten Malang terletak sejauh 35 km.",

                # Sukopuro
                f"<br> Desa Sukopuro merupakan desa yang terletak di Kecamatan Jabung yang berada di Kabupaten Malang yang memiliki total luas wilayah sebesar 630.000 m2 dan terbagi menjadi 4 Dusun, yaitu Dusun Loring seluas 200.000 m², Dusun Karangrejo seluas 150.000 m2, Dusun Kepuh seluas 140.000 m2, dan Dusun  Pandanrejo seluas 140.000 m2. Mata pencaharian utama penduduk di desa ini adalah petani. Total penduduk di Desa Sukopuro adalah sebanyak 6627 jiwa dengan rincian penduduk perempuan sebanyak 3260 jiwa dan laki-laki sebanyak 3367 jiwa. Sementara itu, jumlah Kepala Keluarga di desa ini adalah sebanyak 1996 KK. Jarak kantor pemerintahan Desa Sukopuro ke kantor Kecamatan Jabung adalah sejauh 5 km. Sedangkan jarak kantor Desa Sukopuro ke kantor Kabupaten Malang terletak sejauh 30 km. Mengingat letak desa ini cukup jauh dari wilayah pusat pemerintahan Kabupaten Malang.",

                # Argosari
                f"<br> Desa Argosari memiliki total luas wilayah sebesar 56.050.000 m² dan terbagi menjadi 4 Dusun, yaitu Dusun Argosari, Dusun Gedok, Dusun Bakalan, dan Dusun Pusung Duwur. Total penduduk di Desa Argosari sebanyak 4780 jiwa dengan rincian penduduk perempuan sebanyak 2389 jiwa dan penduduk laki-laki sebanyak 2391 jiwa. Sementara itu, jumlah kepala keluarga di desa ini sebanyak 1360 KK. Jarak kantor pemerintahan Desa Argosari ke kantor Kecamatan Senduro adalah sejauh 21 km. Sedangkan, jarak kantor Desa Argosari ke kantor Kabupaten Lumajang terletak sejauh 46 km. Mengingat letak desa ini cukup jauh dari wilayah pusat pemerintahan Kabupaten Lumajang.",

                # Pasrujambe
                f"<br> Desa Pasrujambe memiliki total luas wilayah sebesar 43.890.000 m² dan terbagi menjadi 11 Dusun yang diantaranya adalah Dusun Pasrepan, Dusun Krajan I, Dusun Krajan II, Dusun Jabon, Dusun Munggir, Dusun Tulung Rejo, Dusun Tawon Songo, Dusun Ngampo, Dusun Plambang, Dusun Suco, dan Dusun Sumberingin. Total penduduk di Desa Pasrujambe adalah sebanyak 14.310 jiwa dengan rincian jumlah penduduk perempuan sebanyak 6.968 jiwa dan penduduk laki-laki sebanyak 7.342 jiwa. Sementara, jumlah kepala keluarga di desa ini adalah sebanyak 3.511 KK. Jarak kantor pemerintahan Desa Pasrujambe ke kantor Kecamatan Pasrujambe adalah sejauh 5 km. Sedangkan, jarak kantor Desa Pasrujambe ke kantor Kabupaten Lumajang terletak sejauh 32 km.",

                # Gunungsari
                f"<br> Desa Gunungsari merupakan desa yang terletak di Kecamatan Maesan yang berada di Kabupaten Bondowoso. Desa Gunungsari terbagi menjadi 8 Dusun yang diantaranya adalah Dusun Krajan, Dusun Kosawah, Dusun, Dusun Kodeduk, Dusun Gadingan, Dusun Gunungsari Barat, Dusun Gunungsari Timur, dan Dusun Peh. Total penduduk di Desa Gunungsari adalah sebanyak 4.107 jiwa dengan rincian jumlah penduduk perempuan sebanyak 2.033 jiwa dan penduduk laki-laki sebanyak 2.074 jiwa. Sementara, jumlah kepala keluarga di desa ini adalah sebanyak 1.352 KK. Jarak kantor pemerintahan Desa Gunungsari ke kantor Kecamatan Maesan adalah sejauh 3 km. Sedangkan, jarak kantor Desa Gunungsari ke kantor Kabupaten Bondowoso terletak sejauh 15 km. ",

                # Gunosari
                f"<br> Desa Gunosari memiliki total luas wilayah sebesar 17.710 m2 dan terbagi menjadi 9 Dusun yang diantaranya adalah Dusun Bedian seluas 2.125 m2, Dusun Gunungsari seluas 1.771 m2, Dusun Margasari seluas 1.771 m2, Dusun Karang Senggan 1 seluas 2.125 m2, Dusun Karang Senggan II seluas 2.125 m2, Dusun Krajan I seluas 619 m2, Dusun Krajan II seluas 619 m2, Dusun Lauk Kebun Barat seluas 3.099 m2, dan Dusun Lauk Kebun Timur seluas 3.099 m2. Mata pencaharian utama penduduk di desa ini adalah bekerja sebagai petani dan buruh tani. Total penduduk di Desa Gunosari adalah sebanyak 7.570 jiwa dengan rincian jumlah penduduk perempuan sebanyak 3.921 jiwa dan penduduk lakilaki sebanyak 3.649 jiwa. Sementara, jumlah kepala keluarga di desa ini adalah sebanyak 2.757 KK. Jarak kantor pemerintahan Desa Gunosari ke kantor Kecamatan Tlogosari adalah sejauh 9,3 km. Sedangkan, jarak kantor Desa Gunosari ke kantor Kabupaten Bondowoso terletak sejauh 17 km. Mengingat letak desa ini cukup jauh dari wilayah pusat pemerintahan Kabupaten Bondowoso.",

                # Bajang
                f"Desa Bajang merupakan desa yang terletak di Kecamatan Ngluyu yang berada di Kabupaten Nganjuk. Desa Bajang memiliki total luas wilayah sebesar 771.974 m2 dan terbagi menjadi 3 Dusun yang diantaranya adalah Dusun Bajang seluas 267.437 m2, Dusun Krondong seluas 65.376 m2, dan Dusun Dance seluas 447.790 m2. Mata pencaharian utama penduduk di desa ini adalah bekerja sebagai petani. Total penduduk di Desa Bajang adalah sebanyak 1.211 jiwa dengan rincian jumlah penduduk perempuan sebanyak 586 jiwa dan penduduk laki-laki sebanyak 625 jiwa. Sementara, jumlah kepala keluarga di desa ini adalah sebanyak 374 KK. Jarak kantor pemerintahan Desa Bajang ke kantor Kecamatan Ngluyu adalah sejauh ±8–9 km. Sedangkan, jarak kantor Desa Bajang ke kantor Kabupaten Nganjuk terletak sejauh 34 km. Mengingat letak desa ini cukup jauh dari wilayah pusat pemerintahan Kabupaten Nganjuk.",

                # Mancon
                f"<br> Desa Mancon merupakan desa yang terletak di Kecamatan Wilangan yang berada di Kabupaten Nganjuk. Desa Mancon memiliki total luas wilayah sebesar 375.800 m2 dan terbagi menjadi 4 Dusun yang diantaranya adalah Dusun Dawuhan, Dusun Jajar, Dusun Awar-Awar, dan Dusun Manggarejo. Mata pencaharian utama penduduk di desa ini adalah bekerja sebagai petani dan karyawan swasta. Total penduduk di Desa Mancon adalah sebanyak 5.075 jiwa dengan rincian jumlah penduduk perempuan sebanyak 3.000-an jiwa dan penduduk laki-laki sebanyak 2.500-an jiwa. Sementara, jumlah kepala keluarga di desa ini adalah sebanyak 1.696 KK. Jarak kantor pemerintahan Desa Mancon ke kantor Kecamatan Wilangan adalah sejauh 4 km. Sedangkan, jarak kantor Desa Mancon ke kantor Kabupaten Nganjuk terletak sejauh 5 km. Letak desa ini cukup dekat dari wilayah pusat pemerintahan Kabupaten Nganjuk.",

                # Mategal
                f"<br> Desa Mategal memiliki total luas wilayah sebesar 735.970 m2 dan terbagi menjadi 4 Dusun yang diantaranya adalah Dusun Mategal, Dusun Kalitengah, Dusun Sangen, dan Dusun Gangsiran. Mata pencaharian utama penduduk di desa ini adalah bekerja sebagai petani, pedagang, dan perantau. Jumlah kepala keluarga di desa ini adalah sebanyak 1.280 KK. Jarak kantor pemerintahan Desa Mategal ke kantor Kecamatan Parang adalah sejauh 3 km. Sedangkan, jarak kantor Desa Mategal ke kantor Kabupaten Magetan terletak sejauh 2,5 km. Letak desa ini cukup dekat dari wilayah pusat pemerintahan Kabupaten Magetan.",

                # Tapak
                f"<br> Desa Tapak memiliki total luas wilayah sebesar 316.000 m2 dan terbagi menjadi 3 Dusun yang diantaranya adalah Dusun Gunting seluas 110.000 m2, Dusun Sekarung seluas 106.000 m2, dan Dusun Banteran seluas 100.000 m2. Mata pencaharian utama penduduk di desa ini adalah bekerja sebagai petani, pedagang, dan peternak. Total penduduk di Desa Tapak adalah sebanyak 2.607 jiwa dengan rincian jumlah penduduk perempuan sebanyak 1301 jiwa dan penduduk laki-laki sebanyak 1.306 jiwa. Sementara, jumlah kepala keluarga di desa ini adalah sebanyak 401 KK. Jarak kantor pemerintahan Desa Tapak ke kantor Kecamatan Panekan adalah sejauh 5 km. Sedangkan, jarak kantor Desa Tapak ke kantor Kabupaten Magetan terletak sejauh 7 km. Mengingat letak desa ini cukup dekat dari wilayah pusat pemerintahan Kabupaten Magetan.",

                # Ngrandu
                f"<br> Desa Ngrandu merupakan desa yang terletak di Kecamatan Suruh yang berada di Kabupaten Trenggalek. Desa Ngrandu memiliki total luas wilayah sebesar 551.048 m2 dan terbagi menjadi 4 Dusun yang diantaranya adalah Dusun Depok, Dusun Babadan, Dusun Guwo, dan Dusun Crabak. Mata pencaharian utama penduduk di desa ini adalah bekerja sebagai petani dan peternak. Total penduduk di Desa Ngrandu adalah sebanyak 2.598 jiwa dengan rincian jumlah penduduk perempuan sebanyak 1.287 jiwa dan penduduk laki-laki sebanyak 1.311 jiwa. Sementara, jumlah kepala keluarga di desa ini adalah sebanyak 885 KK. Jarak kantor pemerintahan Desa Ngrandu ke kantor Kecamatan Suruh adalah sejauh 6 km. Sedangkan, jarak kantor Desa Ngrandu ke kantor Kabupaten Trenggalek terletak sejauh 22 km. Letak desa ini cukup jauh dari wilayah pusat pemerintahan Kabupaten Trenggalek.",

                # Petung
                f"<br> Desa Petung merupakan desa yang terletak di Kecamatan Dongko yang berada di Kabupaten Trenggalek. Desa Petung memiliki total luas wilayah sebesar 1.194 m2 dan terbagi menjadi 2 Dusun yang diantaranya adalah Dusun Krajan seluas 613 m2 dan Dusun Banar seluas 581 m2. Mata pencaharian utama penduduk di desa ini adalah bekerja sebagai Petani. Total penduduk di Desa Petung adalah sebanyak 5.863 jiwa dengan rincian jumlah penduduk perempuan sebanyak 2.901 jiwa dan penduduk lakilaki sebanyak 2.962 jiwa. Sementara, jumlah kepala keluarga di desa ini adalah sebanyak 2.094 KK. Jarak kantor pemerintahan Desa Petung ke kantor Kecamatan Dongko adalah sejauh ±1–1,5 km. Sedangkan, jarak kantor Desa Petung ke kantor Kabupaten Trenggalek terletak sejauh ±32–34 km. Mengingat letak desa ini cukup jauh dari wilayah pusat pemerintahan Kabupaten Trenggalek.",

                # Karanggede
                f"<br> Desa Karanggede merupakan desa yang terletak di Kecamatan Arjosari yang berada di Kabupaten Pacitan. Desa Karanggede memiliki total luas wilayah sebesar 14.001.000 m2 dan terbagi Dusun Krajan, Dusun Sendang, Dusun Kebonsari, Dusun Bangunrejo, dan Dusun Tukul. Total penduduk di Desa Karanggede adalah sebanyak 4.050 jiwa dengan rincian jumlah penduduk perempuan sebanyak 2.032 jiwa dan penduduk laki-laki sebanyak 2.016 jiwa. Sementara, jumlah kepala keluarga di desa ini adalah sebanyak 1.481 KK. Jarak kantor pemerintahan Desa Karanggede ke kantor Kecamatan Arjosari adalah sejauh 11 km. Sedangkan, jarak kantor Desa Karanggede ke kantor Kabupaten Pacitan terletak sejauh 22 km. Mengingat letak desa ini cukup jauh dari wilayah pusat pemerintahan Kabupaten Pacitan.",

                # Worawari
                f"<br> Desa Worawari merupakan desa yang terletak di Kecamatan Kebonagung yang berada di Kabupaten Pacitan. Desa Worawari memiliki total luas wilayah sebesar 8.178.300 m2 dan terbagi menjadi 6 Dusun yang diantaranya adalah Dusun Pringkatung, Dusun Tanggung, Dusun Ngrampal, Dusun Banjarjo, Dusun Krajan, dan Dusun Ledok. Mata pencaharian utama penduduk di desa ini adalah bekerja sebagai petani atau pekebun. Total penduduk di Desa Worawari adalah sebanyak 2.524 jiwa dengan rincian jumlah penduduk perempuan sebanyak 1.257 jiwa dan penduduk lakilaki sebanyak 1.257 jiwa. Sementara, jumlah kepala keluarga di desa ini adalah sebanyak 913 KK. Jarak kantor pemerintahan Desa Worawari ke kantor Kecamatan Kebonagung adalah sejauh ±15 km. Sedangkan, jarak kantor Desa Worawari ke kantor Kabupaten Pacitan terletak sejauh ±23 km. Mengingat letak desa ini cukup jauh dari wilayah pusat pemerintahan Kabupaten Pacitan.",
                ],

    'more': ['/Desa_Ngadirejo,_Kabupaten_Malang',
             '/Desa_Sukopuro,_Kabupaten_Malang',
             '/Desa_Argosari,_Kabupaten_Lumajang',
             '/Desa_Pasrujambe,_Kabupaten_Lumajang',
             '/Desa_Gunungsari,_Kabupaten_Bondowoso',
             '/Desa_Gunosari,_Kabupaten_Bondowoso',
             '/Desa_Bajang,_Kabupaten_Nganjuk',
             '/Desa_Mancon,_Kabupaten_Nganjuk',
             '/Desa_Mategal,_Kabupaten_Magetan',
             '/Desa_Tapak,_Kabupaten_Magetan',
             '/Desa_Ngrandu,_Kabupaten_Trenggalek',
             '/Desa_Petung,_Kabupaten_Trenggalek',
             '/Desa_Karanggede,_Kabupaten_Pacitan',
             '/Desa_Worawari,_Kabupaten_Pacitan'
             ]
})



# Add markers for each village with popup information
for _, village in village_data.iterrows():
    popup_content = f"<b>Desa:</b> {village['village_name']}" \
                    f"{village['gambaran']}" \
                    f"<br><a href='{village['more']}' target='_blank'>Tampilkan hasil analisis</a>"
    folium.Marker(
        location=[village['latitude'], village['longitude']],
        popup=folium.Popup(popup_content, max_width=400),
        tooltip=f"Desa {village['village_name']}, Kecamatan {village['kecamatan']}, Kabupaten {village['kabupaten']}"
    ).add_to(m)

# Display the folium map using the folium_static function
st_data = st_folium(m, width=1000)

# # -----------------------------------------------CLUSTER--------------------------------------------------------------
# Load the data
data = pd.read_csv("klaster.csv")

data = data.rename(columns={'desa': 'DESA', 'kab': 'KABUPATEN', 'kec': 'KECAMATAN'})

data['klaster'] = data['klaster'] + 1

col1, col2 = st.columns([1, 1.5])

with col1:
    st.subheader("Cari Desa")
    select_kab = st.selectbox('Masukkan Kabupaten', data['KABUPATEN'].unique())

    desa_options = data[data['KABUPATEN'] == select_kab]['DESA'].unique()
    select_desa = st.selectbox('Masukkan Desa', desa_options)

    result_data = data[(data['KABUPATEN'] == select_kab) & (data['DESA'] == select_desa)]
    # result_data = result_data.rename(columns={'desa': 'DESA', 'kec': 'KECAMATAN', 'kab': 'KABUPATEN'})

with col2:
    st.subheader(f"Hasil pencarian Desa {select_desa}, Kabupaten {select_kab}")
    # selected_desa_name = result_data.iloc[0]['DESA'] if not result_data.empty else ""  # Mengambil nama desa dari selected_data
    # if not result_data.empty:
    #     klaster_sebaris = result_data.iloc[0]['klaster']
    #     st.write(f":point_right: Desa {selected_desa_name} masuk ke dalam klaster {klaster_sebaris}")
    #
    #     # Menampilkan desa-desa dengan klaster yang sama
    #     desa_dengan_klaster_sama = data[data['klaster'] == klaster_sebaris][['DESA', 'KECAMATAN', 'KABUPATEN']]
    #     tabel_desa_klaster = desa_dengan_klaster_sama.to_html(index=False)
    #     tabel_desa_klaster = tabel_desa_klaster.replace('<tr', '<tr style="text-align:center;"')
    #     tabel_desa_klaster = tabel_desa_klaster.replace('<table', '<table style="width:100%; text-align:center"')
    #     st.markdown(tabel_desa_klaster, unsafe_allow_html=True)

    desa_links = {
        'NGADIREJO': '/Desa_Ngadirejo,_Kabupaten_Malang',
        'SUKOPURO': '/Desa_Sukopuro,_Kabupaten_Malang',
        'ARGOSARI': '/Desa_Argosari,_Kabupaten_Lumajang',
        'PASRUJAMBE': '/Desa_Pasrujambe,_Kabupaten_Lumajang',
        'GUNUNGSARI': '/Desa_Gunungsari,_Kabupaten_Bondowoso',
        'GUNOSARI': '/Desa_Gunosari,_Kabupaten_Bondowoso',
        'BAJANG': '/Desa_Bajang,_Kabupaten_Nganjuk',
        'MANCON': '/Desa_Mancon,_Kabupaten_Nganjuk',
        'MATEGAL': '/Desa_Mategal,_Kabupaten_Magetan',
        'TAPAK': '/Desa_Tapak,_Kabupaten_Magetan',
        'NGRANDU': '/Desa_Ngrandu,_Kabupaten_Trenggalek',
        'PETUNG': '/Desa_Petung,_Kabupaten_Trenggalek',
        'KARANGGEDE': '/Desa_Karanggede,_Kabupaten_Pacitan',
        'WORAWARI': '/Desa_Worawari,_Kabupaten_Pacitan'
    }
    selected_desa_name = result_data.iloc[0][
        'DESA'] if not result_data.empty else ""  # Mengambil nama desa dari selected_data
    selected_link = desa_links.get(selected_desa_name, '')  # Mendapatkan tautan sesuai dengan nama desa

    # Menampilkan klaster sebaris dengan desa yang dipilih
    if not result_data.empty:
        klaster_sebaris = result_data.iloc[0]['klaster']
        st.write(f":point_right: Desa {selected_desa_name} masuk ke dalam klaster {klaster_sebaris}")

        # Menampilkan desa-desa dengan klaster yang sama
        desa_dengan_klaster_sama = data[data['klaster'] == klaster_sebaris][['DESA', 'KECAMATAN', 'KABUPATEN']]

        # Mengecek apakah salah satu desa dengan klaster yang sama termasuk dalam desa_links
        desa_links_intersection = set(desa_dengan_klaster_sama['DESA']).intersection(desa_links.keys())
        if desa_links_intersection:
            st.write(f":point_right: Desa kajian dengan klaster yang sama dengan Desa {selected_desa_name}:")
            for desa in desa_links_intersection:
                st.write(f"- [{desa}]({desa_links[desa]})")
        st.write(f":point_right: Seluruh desa yang berada di klaster yang sama seperti Desa {selected_desa_name}:")
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



# # Set labels for x and y axes
# plt.xlabel("Longitude")
# plt.ylabel("Latitude")
#
# # bpn_map.plot()
# # plt.axis("off")
# st.pyplot()

# python -m streamlit run Analisis_Kerentanan_Sosial.py