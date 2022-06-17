"""
Created on Sun 12 22:58:13 2022
@author: Ana Angélica da Costa Marchiori
"""

# --- LIBRARIES
import pandas            as pd
import streamlit         as st
import folium            as fl
import seaborn           as sns
import matplotlib.pyplot as plt

from streamlit_folium    import folium_static
from folium.plugins      import MarkerCluster

# --- SETTINGS
st.set_page_config(page_title='KC House Sales', layout='wide', page_icon=':house:')
sns.set_style('whitegrid')

# --- DATA
data = pd.read_csv('houses_etl.csv')          # data loading
av_houses = 21613                             # available houses

# --- DASHBOARD
# --- title
st.markdown("<h1 style='text-align: center'>King County houses purchase and sale report</h1>",
            unsafe_allow_html=True)

with st.spinner('Updating Report...'):
    st.write("""""")  # space

    # --- indicators
    mean_profit = round(data['profit'].mean(), 2)

    i1, i2, i3, i4, i5 = st.columns((1, 1, 1, 1, 1))

    i1.write('')
    i2.metric(label='Available houses', value=av_houses)
    i3.metric(label='Houses with business potential', value=int(data.shape[0]))
    i4.metric(label='Average profit per house', value='US$' + str(mean_profit))
    i5.write('')

    st.write("""""")  # space

    # --- graph and zip codes
    g, z = st.columns((1, 0.5))

    # graph
    g.markdown("<h5 style='text-align: center'>Price distribution</h5>", unsafe_allow_html=True)

    fig = plt.figure(figsize=(10, 4))
    sns.histplot(data=data, x='sales_price')
    # plt.xticks(fontsize=10)
    g.pyplot(fig)

    # list of zip codes
    z.markdown("<h5 style='text-align: center'>Average price of the regions</h5>", unsafe_allow_html=True)

    option = z.selectbox('Choose an option', ('Most expensive cities', 'Cheapest cities'))
    var = data[['city', 'sales_price']].groupby('city').mean().sort_values('sales_price',
                                                                           ascending=False).reset_index()
    var['sales_price'] = var['sales_price'].apply(lambda x: 'US$ ' + str(round(x, 2)))
    var = var.rename(columns={'city': 'City', 'sales_price': 'Mean sale price'})

    if option == 'Most expensive cities':
        z.table(var.head(6))
    else:
        z.table(var.tail(6))

# --- map and table
with st.expander('More details'):
    # --- map
    # Base Map - Folium
    density_map = fl.Map(location=[data['lat'].mean(), data['long'].mean()], default_zoom_start=2)

    # filter: range price
    minp = float(data['sales_price'].min())
    maxp = float(data['sales_price'].max())
    price = st.slider('Select a price range (US$)', min_value=minp, max_value=maxp, value=(minp, maxp), step=10000.0)

    data = data[(data['sales_price'] >= price[0]) & (data['sales_price'] <= price[1])]

    # filter: city, period, bedrooms, bathrooms
    f1, f2, f3, f4, f5 = st.columns((0.6, 1, 1, 1, 1))
    f1.write("""""")

    # city
    city = f2.checkbox('City')
    if city:
        city_box = f2.selectbox(label = 'Choose one', options = pd.Series(data['city'].unique()).sort_values())
        data = data[data['city'] == city_box]

    # quarter
    quarter = f3.checkbox('Quarter')
    if quarter:
        quarter_box = f3.selectbox(label = 'Choose one', options = pd.Series(data['quarter_sale'].unique()).sort_values())
        data = data[data['quarter_sale'] == quarter_box]

    # bedrooms
    bedrooms = f4.checkbox('Bedrooms')
    if bedrooms:
        bedrooms_box = f4.selectbox(label = 'Choose one', options = pd.Series(data['bedrooms'].unique()).sort_values())
        data = data[data['bedrooms'] == bedrooms_box]

    # bathrooms
    bathrooms = f5.checkbox('Bathrooms')
    if bathrooms:
        bathrooms_box = f5.selectbox(label = 'Choose one', options = pd.Series(data['bathrooms'].unique()).sort_values())
        data = data[data['bathrooms'] == bathrooms_box]


    st.write(f"""- {len(data)} houses were selected.""")

    st.write("""""")  # space

    # title
    st.markdown("<h5 style='text-align: center'>Location of selected houses</h5>", unsafe_allow_html=True)

    marker_cluster = MarkerCluster().add_to(density_map)

    for name, row in data.iterrows():
        fl.Marker([row['lat'], row['long']],
                  popup=fl.Popup(f'<b>- ID:</b> {row.id};<br>'
                                 f'<b>- ZIPCODE:</b> {row.zipcode};<br>'
                                 f'<b>- City:</b> {row.city};<br>'
                                 f'<b>- Sale Price:</b> US${row.sales_price:.2f};<br>'
                                 f'<b>- Sale period:</b> {row.quarter_sale}º quarter;<br>'
                                 f'<b>- Profit:</b> US${row.profit:.2f}.<br>',
                                 min_width=50, max_width=400)).add_to(marker_cluster)

    folium_static(density_map, width=1130, height=500)

    # --- table
    # select features and format
    data['basement'] = data['sqft_basement'].apply(lambda x: 'Yes' if x != 0 else 'No')
    data['recently_renovated'] = data['yr_renovated'].apply(lambda x: 'Yes' if x >= 2005 else 'No')
    data['waterfront_yn'] = data['waterfront'].apply(lambda x: 'Yes' if x == 1 else 'No')

    data = data[['id', 'zipcode', 'city', 'date', 'price', 'quarter_sale', 'sales_price', 'profit', 'sqft_lot',
                 'sqft_living', 'floors', 'basement', 'yr_built', 'recently_renovated', 'condition', 'grade',
                 'view', 'waterfront_yn', 'bedrooms', 'bathrooms']]

    # date
    data['date'] = pd.to_datetime(data['date'])
    data['date'] = data.apply(lambda x: x['date'].strftime('%m/%d/%Y'), axis=1)

    # floors
    data['floors'] = data['floors'].astype(int)

    data.rename(columns = {'id': 'ID', 'zipcode': 'Zip code', 'city': 'City', 'date': 'Purchase date',
                           'price': 'Purchase price (US$)', 'quarter_sale': 'Sales quarter', 'sales_price': 'Sale price (US$)',
                           'profit': 'Profit', 'sqft_lot': 'Lot area (ft²)', 'sqft_living': 'Building area (ft²)',
                           'floors': 'Floors', 'basement': 'Basement', 'yr_built': 'Building year','recently_renovated': 'Recently renovated',
                           'condition': 'Condition', 'grade': 'Quality of materials', 'view': 'View', 'waterfront_yn': 'Waterfront',
                           'bedrooms': 'Bedrooms', 'bathrooms': 'Bathrooms'}, inplace=True)

    st.write("""""")  # space
    st.markdown("<h5 style='text-align: center'>Information about the houses</h5>", unsafe_allow_html=True)

    st.dataframe(data)

    st.write("""""")
    st.write("""
    Observations:
    - Condition: an index from 1 to 5 on the condition of the house;
    - View: an index from 0 to 4 of how good the view of the property was;
    - Recently renovated: houses renovated since 2005.
    """)