import streamlit as st
import pandas as pd
import plotly.express as px
import math

st.write("# Personal Loan")
col1, col2, col3 = st.columns(3)



def loanCalc(P,N,R):
    # Converting years to months
    n = N*12
    r = R/1200

    #Calculating EMI
    x = (1+r)**n
    emi = P*r*x/(x-1)

    #Calculating Amount
    amt = emi*n

    # Calculating intrest
    I = amt - P
    
    #Calculating percent Intrest
    perI = (I/amt)*100

    return emi, amt, I, perI

P = col1.number_input("Principal Amount", min_value=0, value=100000)
R = col2.number_input("Rate of intrest", min_value=0.00, value=11.00)
N = col3.number_input("Tenure of Loan", min_value=1, value=5)


emi, amt, I, perI = loanCalc(P,N,R)

col1, col2 = st.columns(2)
col1.write("\n")
col1.write("\n")
col1.metric(label="Monthly EMI", value=f"Rs {emi:,.0f}")
col1.metric(label="Total Intrest", value=f"Rs {I:,.0f}")
col1.metric(label="Total Amount", value=f"Rs {amt:,.0f}")

# Visual
data = {"Index":["Principal", "Intrest"],
        "Values":[P, I]}
df = pd.DataFrame(data)
pie = px.pie(data_frame=df, names="Index", values="Values", color_discrete_sequence=["green", "orange"], height=400)

col2.plotly_chart(pie)


# Creating dataframe with payment schedule
schedule = []
rem_amt = P

n=N*12
r = R/1200
for i in range(1,n+1):
    int_pay = rem_amt * r
    prin_pay = emi - int_pay
    rem_amt -= prin_pay
    year = math.ceil(i/12)      # Calculate year into loan
    schedule.append([i, emi, prin_pay, int_pay, rem_amt, year])
    d = pd.DataFrame(
        schedule,
        columns=["Month", "EMI", "Principal Payment", "Intrest Payment", "Remaining Amount", "Year"],
        )
    
# Displaying data_frame as chart
st.write("### Schedule showing EMI paymnets")
payments = d[["Year", "Remaining Amount"]].groupby(by="Year").min()
st.line_chart(payments)