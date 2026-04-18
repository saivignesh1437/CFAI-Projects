import streamlit as st

# Algorithms
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low = 0
    high = 0 
    len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


st.title("Algorithm Comparator")

size = st.slider("Input Size", 100, 100000, 1000)
target = st.number_input("Enter number to search", min_value=0, max_value=size-1, value=0)

if st.button("Compare Algorithms"):
    arr = list(range(size))  # already sorted

    # Linear Search
    start = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start

    # Binary Search
    start = time.time()
    binary_result = binary_search(arr, target)
    binary_time = time.time() - start
