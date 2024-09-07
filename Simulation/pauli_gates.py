from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit_aer import Aer, AerSimulator
import matplotlib.pyplot as plt

# Set up the circuits with the Pauli gates
qc = QuantumCircuit(3, 3)
qc.x(0)
qc.y(1)
qc.z(2)

# Measure the quantum state of each qubit
qc.measure(0, 0)
qc.measure(1, 1)
qc.measure(2, 2)

# Simulate the circuit using statevector for visualization
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit).result()

# Count and plot the results
counts = result.get_counts()
plot_histogram(counts)
plt.show()
