from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit_aer import Aer, AerSimulator
import matplotlib.pyplot as plt

# Set up a circuit to put a qubit into a Hadamard state
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

# Simulate the circuit
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit).result()

# Count and plot the measurement results
counts = result.get_counts()
print(counts)
plot_histogram(counts)
plt.show()
