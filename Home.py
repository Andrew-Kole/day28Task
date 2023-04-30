import streamlit as st
import controller.content_processing as cs


st.set_page_config(layout="wide")

st.title(cs.get_info()["title"])
st.image(cs.get_info()["url"])
st.write(cs.get_info()["explanation"])






