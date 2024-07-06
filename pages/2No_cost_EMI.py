import streamlit as st
import pandas as pd
import plotly.express as px

st.write("# No Cost EMI")

def calc(P,N,D):
    emi = (P-D)/N
    return emi


col1, col2, col3 = st.columns(3)
P = col1.number_input("Price", min_value=0, value=10000)
N = col2.number_input("Tenure (In Months)", min_value=1, value=1)
D = col3.number_input("Downpayment (if any)", min_value=0)

emi = calc(P,N,D)
col1.write("\n")
col1.metric(label="Monthly EMI", value=f"Rs {emi:,.0f}")
col1.write(f" for {N} months")