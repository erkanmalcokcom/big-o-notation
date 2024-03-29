import streamlit as st
import pandas as pd

# Define the data for the Big-O Cheat Sheet
data = {
    'Big-O': ['O(1)', 'O(log n)', 'O(n)', 'O(n log n)', 'O(n^2)', 'O(n^3)', 'O(2^n)', 'O(n!)'],
    'Name': [
        'Constant Time', 'Logarithmic Time', 'Linear Time', 'Log-Linear Time',
        'Quadratic Time', 'Cubic Time', 'Exponential Time', 'Factorial Time'
    ],
    'Description': [
        'Execution time remains unchanged irrespective of input data',
        'Complexity increases by one unit for each doubling of input data',
        'Execution time increases linearly with the size of the input data',
        'Complexity grows as a combination of linear and logarithmic',
        'Time taken is proportional to the square of the number of elements',
        'Execution time is proportional to the cube of the number of elements',
        'Time doubles for every new element added',
        'Complexity grows factorially based on the size of the dataset'
    ],
    'Example': [
        'Checking if a stack is empty',
        'Finding an item in a balanced search tree',
        'Linear traversal of a list',
        'Merge sort on a collection of items',
        'Checking all possible pairs in an array',
        'Matrix multiplication of n x n matrices',
        'Generating all subsets of a given set',
        'Determining all permutations of a given list'
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Streamlit application
st.title('Big-O Complexity Cheat Sheet')
st.subheader("""
             A mathematical notation that describes the limiting behaviour of a function when the argument tends towards a particular value or infinity. In computer science, it's used to classify algorithms according to how their run time or space requirements grow as the input size grows.
             """)
st.divider()
st.dataframe(df, use_container_width=True, hide_index=True)

st.image('plot-big-o.jpg', caption='Big-O Complexity Chart', use_column_width=True)


