import streamlit as st
import time

# Algorithms
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# UI
st.title("Time Comparison: Linear vs Binary Search")

size = st.slider("Input Size", 100, 100000, 1000)
key = st.number_input("Enter number to search", min_value=0, max_value=size-1, value=0)

if st.button("Compare Algorithms"):
    arr = list(range(size))  

    # Linear Search
    start = time.time()
    linear_result = linear_search(arr, key)
    linear_time = time.time() - start

    # Binary Search
    start = time.time()
    binary_result = binary_search(arr, key)
    binary_time = time.time() - start

    # Displaying Results
    st.subheader("Time Comparison")
    st.write(f"Linear Search Time: {linear_time:.8f} seconds")
    st.write(f"Binary Search Time: {binary_time:.8f} seconds")

    #  Faster algorithm
    if linear_time < binary_time:
        st.success("Linear Search is faster (unexpected for large input!)")
    else:
        st.success("Binary Search is faster ")
