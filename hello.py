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

# Set the page configuration
st.set_page_config(
    page_title="Big-O Complexity Cheat Sheet",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com/search?q=big-o-notation',
        'Report a bug': "https://www.google.com",
        'About': "The Big O notation, as you can see, is not just a mathematical concept but a practical tool that gives you a high-level understanding of the algorithm's efficiency. "
    }
)

# Streamlit application
st.title('Big-O Complexity Cheat Sheet')
st.subheader("""
             A mathematical notation that describes the limiting behaviour of a function when the argument tends towards a particular value or infinity. In computer science, it's used to classify algorithms according to how their run time or space requirements grow as the input size grows.
             """)
st.divider()
st.dataframe(df, use_container_width=True, hide_index=True)

st.image('plot-big-o.jpg', caption='Big-O Complexity Chart', use_column_width=True)

st.markdown("""
1. **O(1) - Constant Time**: An algorithm is said to run in constant time if it requires the same amount of time regardless of the size of the input data. For example, accessing any single element in an array by index is an O(1) operation since it takes the same time no matter how large the array is.

2. **O(log n) - Logarithmic Time**: An algorithm runs in logarithmic time when it reduces the size of the input data in each step (usually by half). It's more efficient than linear time but less so than constant time. Binary search is a classic example where you divide the remaining area of search by half each time.

3. **O(n) - Linear Time**: An algorithm has a linear time complexity when the execution time increases linearly with the input size. For example, a single loop over n elements would typically be an O(n) operation.

4. **O(n log n) - Log-Linear Time**: This time complexity combines linear and logarithmic time. Algorithms with this complexity are usually quite efficient for larger data sets. A common example is the merge sort algorithm, where the list is divided into halves (logarithmic part) and then linearly merged back together.

5. **O(n^2) - Quadratic Time**: This describes an algorithm whose performance is directly proportional to the square of the size of the input data set. This is common with algorithms that involve nested iterations over the data set. For example, a double loop for comparing each pair of elements in an array will have O(n^2) complexity.

6. **O(n^3) - Cubic Time**: Similar to quadratic time, but with three nested loops instead of two, leading to the cube of the size of the input data set affecting the performance.

7. **O(2^n) - Exponential Time**: The time doubles with every new element added to the input data set. These kinds of algorithms become infeasible very quickly as the size of the input increases. For example, algorithms that generate all subsets of a set have exponential time complexity.

8. **O(n!) - Factorial Time**: The complexity grows factorially with the size of the input data set. This is the least efficient and is generally impractical with large n. An example is an algorithm that determines all permutations of a list.
                
    """)



