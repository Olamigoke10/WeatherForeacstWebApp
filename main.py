import streamlit as st
import plotly.express as px
from backend import get_data

# Title text
st.title("WEATHER FORECAST")

# Text Input
place = st.text_input("Place:")

# Slider
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

# Select_Box
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

#Sub header
if days != 1:
    st.subheader(f"{option} For The Next {days} Days In {place.title()}")
else:
    st.subheader(f"{option} For The Next {days} Day In {place.title()}")

try:
    if place:
        # get temperature or Sky data
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=(temperatures), labels={"x":"Dates", "y":"Temperature(C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png", "Rain":"images/rain.png","Snow":"snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            print(sky_conditions)
            image_path = [images[condition] for condition in sky_conditions]
            st.image(image_path, width=115)
except(Exception):
    st.warning("Sorry Invalid Place, Pls Input a Valid Place")


# mngipipinitr