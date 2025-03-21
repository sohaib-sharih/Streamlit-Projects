import random
import streamlit as st

def createData():
       
    f = 90
    while f <= 120:
        f += 1
        
        print(random.randint(f, 250))
        st.write(f"{random.randint(f, 250)}")

createData()


