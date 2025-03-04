import streamlit as st
from Views import FeedView, AddPostView
from Services import get_feed, add_post
AddPostView.AddPostView(add_post)
st.write("___")
FeedView.FeedView(get_feed)