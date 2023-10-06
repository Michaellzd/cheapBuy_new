"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

# Import Libraries
import webbrowser
import pandas as pd
from source.web_scrappers.WebScrapper import WebScrapper
import os
import streamlit as st
import sys

from mailgun import send_email_via_mailgun



sys.path.append('../')

title = '<p style="font-family:Bradley Hand, cursive; color:#64b3f4; font-size: 157px;">cheapBuy</p>'
# st.title("CheapBuy")
st.markdown(title, unsafe_allow_html=True)
# st.image("media/saveMoney2.gif")
url_sidebar = st.sidebar.text_input('Quick Action: Open a new page')

# st.sidebar.image("media/cheapBuy_Banner.gif")
st.sidebar.image("media/saveMoney2.gif")
st.sidebar.title("Customize Options Here:")
sites = st.sidebar.selectbox("Select the website:", ("All Sites",
                             "amazon", "walmart", "ebay", "costco", "bestbuy"))

price_range = st.sidebar.selectbox("Select the price range:", (
    "all", "Under $50", "[$50, $100)", "[$100, $150)", "[$150, $200)", "$200 & Above"))
st.header("Website: " + sites.capitalize() +
          '| |' + "Price Range: " + price_range)
#st.header("Price Range: " + price_range)


if url_sidebar:
    webbrowser.open(url_sidebar)

# Hide Footer in Streamlit
hide_menu_style = """
        <style>
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


# Display Image

st.sidebar.write("cheapBuy provides you ease to buy any product through your favourite website's like Amazon, Walmart, Ebay, Costco, etc, by providing prices of the same product from all different websites")
#st.write("cheapBuy provides you ease to buy any product through your favourite website's like Amazon, Walmart, Ebay, Bjs, Costco, etc, by providing prices of the same product from all different websites")
url = st.text_input('Enter the product website link')
email = st.text_input('Enter your email address to get the results')


def price_filter(price_range):
    #price_min, price_max = 0.0, 0.0
    if price_range == "Under $50":
        price_min, price_max = 0.0, 49.99
    elif price_range == "[$50, $100)":
        price_min, price_max = 50.0, 99.99
    elif price_range == "[$100, $150)":
        price_min, price_max = 100.0, 149.99
    elif price_range == "[$150, $200)":
        price_min, price_max = 150.0, 199.99
    elif price_range == "$200 & Above":
        price_min, price_max = 200.0, float('inf')
    else:
        price_min, price_max = 0.0, float('inf')
    return price_min, price_max


price_min, price_max = price_filter(price_range)

# Pass url to method
if url:
    webScrapper = WebScrapper(url)
    results = webScrapper.call_scrapper()

    # Use st.columns based on return values
    description, url, price, site = [], [], [], []

    if sites == "All Sites":
        for result in results:
            # add results that only fit to selected price range :
            if result:
                try:
                    if price_min <= float(result['price'][1:]) <= price_max:
                        description.append(result['description'])
                        url.append(result['url'])
                        price.append(
                            float(result['price'].strip('$').rstrip('0')))
                        site.append(result['site'])
                except Exception as e:
                    print(e)

    else:
        # if sites not in site:
        #st.error('Sorry, there is no same product in your selected website.')

        # else:
        for result in results:
            # add results that only fit to selected price range :
            if result:
                try:
                    if price_min <= float(result['price'][1:]) <= price_max:
                        # print(result['site'])
                        if result['site'].strip() == sites:
                            description.append(result['description'])
                            url.append(result['url'])
                            price.append(
                                float(result['price'].strip('$').rstrip('0')))
                            site.append(result['site'])
                except Exception as e:
                    print(e)

    if len(price):

        def highlight_row(dataframe):
            # copy df to new - original data are not changed
            df = dataframe.copy()
            minimumPrice = df['Price'].min()
            # set by condition
            mask = df['Price'] == minimumPrice
            df.loc[mask, :] = 'background-color: lightgreen'
            df.loc[~mask, :] = 'background-color: ""'
            return df

        dataframe = pd.DataFrame(
            {'Description': description, 'Price': price, 'Link': url}, index=site)
        st.balloons()
        st.markdown(
            "<h1 style='text-align: center; color: #1DC5A9;'>RESULT</h1>", unsafe_allow_html=True)
        st.dataframe(dataframe.style.apply(highlight_row, axis=None))
        st.markdown(
            "<h1 style='text-align: center; color: #1DC5A9;'>Visit the Website</h1>", unsafe_allow_html=True)

        for s, u, p in zip(site, url, price):
            if p == min(price):
                if st.button('👉'+s+'👈'):
                    webbrowser.open(u)
            else:
                if st.button(s):
                    webbrowser.open(u)

        subject = "Your cheapBuy Results"
        email_content = f"Here are your results for {url}:\n\n"
        for s, u, p in zip(site, url, price):
            email_content += f"Website: {s}, Price: ${p}, Link: {u}\n"

        send_email_via_mailgun(email, subject, email_content)

    elif not description or not url or not price or not site:
        st.error('Sorry, there is no product on your selected options.')
    else:
        st.error('Sorry, there is no other website with same product.')


# Add footer to UI
footer = """<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0%;
width: 100%;
background-color: #FBD786;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p><a style='display: block; text-align: center;' href="https://github.com/freakleesin/cheapBuy" target="_blank">Developed with ❤ by cheapBuy</a></p>
<p><a style='display: block; text-align: center;' href="https://github.com/freakleesin/cheapBuy/blob/main/LICENSE" target="_blank">MIT License Copyright (c) 2021 cheapBuy</a></p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)
