import streamlit as st

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

st.title("Algorithm Comparator")
