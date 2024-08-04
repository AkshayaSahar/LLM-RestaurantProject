import streamlit as st
import langchain_helper

st.title("Restaurant name genrator")

cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian", "American", "Mexican", "Chinese", "Italian"))


if cuisine:
    response = langchain_helper.gen(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("Menu items")
    for item in menu_items:
        st.write("-", item)

