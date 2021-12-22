import streamlit as st
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import numpy as np
from matplotlib import pyplot as plt
import warnings

warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from matplotlib import pyplot
from tabulate import tabulate

data = pd.read_excel("C:\\Users\\Lenovo\\Desktop\\ExcelR\\Data Science - Project P81\\CO2 dataset.xlsx")

final_arima = ARIMA(data['CO2'], order=(3, 1, 4))
final_arima = final_arima.fit()

data2 = data.copy()

st.title("Forecasting CO2 Emission")
nav = st.sidebar.radio("Navigation", ["About data", "Prediction", "Forecast"])
if nav == "About data":
    st.subheader("Data")
    data
    st.subheader("Scatter plot of the data")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.figure(figsize=(10, 5))
    plt.scatter(data["Year"], data["CO2"])
    plt.ylim(0)
    plt.xlabel("Years")
    plt.ylabel("CO2 Emission")
    plt.tight_layout()
    st.pyplot()

    st.subheader("Area plot of the data")
    st.area_chart(data=data.CO2, width=150, height=300, use_container_width=True)

    st.subheader("Line plot of the data")
    st.line_chart(data=data.CO2, width=150, height=300, use_container_width=True)

    st.subheader("Histogram of the data")
    fig = plt.figure(figsize=(10, 4))
    plt.hist(data.CO2)
    st.pyplot(fig)

if nav == "Prediction":
    predict = final_arima.fittedvalues
    data["predicted_value"] = predict
    data
    plt.plot(data.CO2, label='original')
    plt.plot(predict, label='forecast')
    plt.title('Forecast')
    plt.legend(loc='upper left', fontsize=8)
    st.pyplot()

if nav == "Forecast":

    year = st.slider("Select number of Year from 2015", 1, 100, step=1)

    st.subheader("Forecasting the data for next few years")

    pred = final_arima.forecast(year)

    if st.button("Predict"):
        st.subheader(f"Your predicted CO2 emission from year 2015")
        pred

        st.subheader("Line plot of the Forecasted data")
        st.line_chart(pred)