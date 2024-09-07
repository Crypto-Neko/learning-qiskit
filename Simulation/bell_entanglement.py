from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit_aer import Aer, AerSimulator
import matplotlib.pyplot as plt

# Create the quantum circuit and set it up with H and CNOT
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)

qc.draw('mpl')

# Simulate the citcuit with statevector for visualization
simulator = Aer.get_backend('statevector_simulator')
compiled_circuit = transpile(qc, simulator)
state_result = simulator.run(compiled_circuit).result()

# Plot the state vector on the Bloch sphere
statevector = state_result.get_statevector(qc)
plot_bloch_multivector(statevector)

# Measure the qubits and simulate the circuit
qc.measure([0, 1], [0, 1])
measurement_simulator = AerSimulator()
compiled_circuit = transpile(qc, measurement_simulator)
result = measurement_simulator.run(compiled_circuit).result()

# Get the counts and visualize the result
counts = result.get_counts(qc)
plot_histogram(counts)
plt.show()
