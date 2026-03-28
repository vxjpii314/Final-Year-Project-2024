import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
g = 1.0  # Example value for g
omega_0 = 1.0  # Example value for omega_0
omega_L = 1.0  # Example value for omega_L
n = 1.0  # Example value for n
t = np.linspace(0, 10, 1000)  # Time range from 0 to 10

# Define the solution functions for a(t), b(t), d1(t), d2(t)
def a(t):
    term1 = np.cos(np.sqrt(2) * np.sqrt(g) * t * np.sqrt(2 * g + 2 * g * n - omega_0**2 * np.sqrt(n + 1) - omega_L**2 * np.sqrt(n + 1) + 2 * omega_0 * omega_L * np.sqrt(n + 1)))
    return -((g * (term1 - 1) * np.sqrt(n + 1)) / (2 * omega_0 * omega_L - omega_0**2 - omega_L**2 + 2 * g * np.sqrt(n + 1)))

def b(t):
    term1 = np.cos(np.sqrt(2) * np.sqrt(g) * t * np.sqrt(2 * g + 2 * g * n - omega_0**2 * np.sqrt(n + 1) - omega_L**2 * np.sqrt(n + 1) + 2 * omega_0 * omega_L * np.sqrt(n + 1)))
    return (2 * omega_0 * omega_L - omega_0**2 - omega_L**2 + g * np.sqrt(n + 1)) / (2 * omega_0 * omega_L - omega_0**2 - omega_L**2 + 2 * g * np.sqrt(n + 1)) + (g * term1 * np.sqrt(n + 1)) / (2 * omega_0 * omega_L - omega_0**2 - omega_L**2 + 2 * g * np.sqrt(n + 1))

def d1(t):
    term1 = np.cos(np.sqrt(2) * np.sqrt(g) * t * np.sqrt(2 * g + 2 * g * n - omega_0**2 * np.sqrt(n + 1) - omega_L**2 * np.sqrt(n + 1) + 2 * omega_0 * omega_L * np.sqrt(n + 1)))
    return (g * (term1 - 1) * (omega_0 - omega_L) * np.sqrt(n + 1)) / (2 * omega_0 * omega_L - omega_0**2 - omega_L**2 + 2 * g * np.sqrt(n + 1))

def d2(t):
    term1 = np.sqrt(2) * g * np.sin(np.sqrt(2) * t * np.sqrt(g * (2 * g + 2 * g * n - omega_0**2 * np.sqrt(n + 1) - omega_L**2 * np.sqrt(n + 1) + 2 * omega_0 * omega_L * np.sqrt(n + 1))))
    return -(np.sqrt(2) * g * term1 * np.sqrt(n + 1)) / (2 * np.sqrt(g * (2 * g + 2 * g * n - omega_0**2 * np.sqrt(n + 1) - omega_L**2 * np.sqrt(n + 1) + 2 * omega_0 * omega_L * np.sqrt(n + 1))))

# Plot the solutions
plt.figure(figsize=(10, 6))

# Plot a(t), b(t), d1(t), d2(t)
plt.plot(t, a(t), label=r'$a(t)$')
plt.plot(t, b(t), label=r'$b(t)$')
plt.plot(t, d1(t), label=r'$d1(t)$')
plt.plot(t, d2(t), label=r'$d2(t)$')

# Customize plot
plt.title('Solutions of a(t), b(t), d1(t), and d2(t) vs Time')
plt.xlabel('Time (t)')
plt.ylabel('Solutions')
plt.legend()
plt.grid(True)

# Show plot
plt.show()
