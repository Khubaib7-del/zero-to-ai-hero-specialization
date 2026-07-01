import numpy as np
import matplotlib.pyplot as plt

# Sigmoid Function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Generate values for z
z = np.linspace(-10, 10, 100)
sigmoid_values = sigmoid(z)

# plot the sigmoid function
plt.figure(figsize=(8, 6))
plt.plot(z, sigmoid_values, label='Sigmoid Function', color='blue')
plt.xlabel('z')
plt.ylabel('σ(z)')
plt.title('Sigmoid Function')
plt.legend()
plt.grid(True)
plt.show()