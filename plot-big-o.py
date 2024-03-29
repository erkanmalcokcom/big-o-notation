import matplotlib.pyplot as plt
import numpy as np

# Define the range of n
n = np.arange(1, 21)

# Calculate complexities
constant_time = np.ones_like(n)
linear_time = n
log_time = np.log(n)
linearithmic_time = n * np.log(n)
quadratic_time = n**2
cubic_time = n**3
exponential_time = 2**n

# Due to the rapid growth of exponential and factorial functions, they will be excluded from the plot for better readability
# Plot the complexities
plt.figure(figsize=(10, 8))
plt.plot(n, constant_time, label='O(1) - Constant Time', marker='o')
plt.plot(n, log_time, label='O(log n) - Logarithmic Time', marker='o')
plt.plot(n, linear_time, label='O(n) - Linear Time', marker='o')
plt.plot(n, linearithmic_time, label='O(n log n) - Linearithmic Time', marker='o')
plt.plot(n, quadratic_time, label='O(n^2) - Quadratic Time', marker='o')
plt.plot(n, cubic_time, label='O(n^3) - Cubic Time', marker='o')

plt.yscale('log')  # Use logarithmic scale for better visibility
plt.xlabel('n - Size of Input Data')
plt.ylabel('Time Complexity (log scale)')
plt.title('Time Complexity Graph')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()

# Save the plot
plt.savefig('plot-big-o.jpg')

'''
O(1) - Constant Time: Remains constant regardless of n.

O(log n) - Logarithmic Time: Increases very slowly with n.

O(n) - Linear Time: Increases proportionally with n.

O(n log n) - Linearithmic Time: Grows slightly faster than linear time due to the additional logarithmic factor.

O(n^2) - Quadratic Time: Grows much faster than linear or logarithmic, but still manageable for small values of n.

O(n^3) - Cubic Time: Grows very quickly and can become infeasible for even moderately sized n.

'''