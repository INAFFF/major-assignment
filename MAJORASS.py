import streamlit as st
import pandas as pd
import numpy as np

st.title("Blac jack game")

PlayerName = st.text_input("Player Name", "Mc Damon")
st.write("Player name is", PlayerName)

