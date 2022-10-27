import random
import string
import math
import streamlit as st
import pandas as pd
import numpy as np
import os
import yfinance as yf
import datetime
from datetime import date, timedelta
import cufflinks as cf



today = date.today()

st.title("Stock price")

d1 = st.date_input("start date",
                   datetime.date(date.today))
st.write("Start Date: ", d1)

class Stock:
    def __init__(self, name, startDate, endDate):
        self.name = name
        self.start = startDate
        self.end = endDate

    def getData(self):
        stockData = yf.Ticker(name)
        stockHist = stockData.history(period = '1d', start = self.startDate, end = self.endDate)

        st.write("Price changes")
        band = cf.QuantFig(stockHist, title = "Price figure", legend = "top", name = "Price range" )
        band.add_bollinger_bands()
        graph = band.iplot(asFigure = True)
        st.ploty_chart(graph)


st.title("Stock price")
option = st.selectbox(
    "Select the company price change you want to check out", ("APPL", "NFLX", "NVDA","ADBE", "INTC", "MSFT", "GOOGL", "TSLA", "ORCL"))
    

d1 = st.date_input("start date", datetime.date(date.today()))
st.write("Start Date: ", d1)

d2 = st.date_input("end date", datetime.date(date.today()))
st.wrtie("End Date: ", d2)
stockFetch = Stock(option,d1,d2)
stockFetch.getData()



