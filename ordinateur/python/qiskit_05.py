import qiskit as q
from qiskit_aer import AerSimulator
import numpy as np

### Partie A. Préparation

# On simule un ordinateur quantique
simulator = AerSimulator(method="statevector")


# Initialisation à la main : écriture algébrique
alpha1, beta1 = 3+1j, 1-2j
norme1 = np.sqrt(np.abs(alpha1)**2 + np.abs(beta1)**2)
alpha1, beta1 = alpha1/norme1, beta1/norme1

alpha2, beta2 = 1j, -2
norme2 = np.sqrt(np.abs(alpha2)**2 + np.abs(beta2)**2)
alpha2, beta2 = alpha2/norme2, beta2/norme2


### Partie B. Construction du circuit 1

# Circuit quantique avec 2 qbits
circuit1 = q.QuantumCircuit(2)

etat_initial1 = [alpha1,beta1]
qubit_initial1 = circuit1.initialize(etat_initial1, [0])

etat_initial2 = [alpha2,beta2]
qubit_initial2 = circuit1.initialize(etat_initial2, [1])

circuit1.h(0)  # Porte de Hadamard
circuit1.h(1)  # Porte de Hadamard
circuit1.cx(0, 1) # CNOT classique
circuit1.h(0)  # Porte de Hadamard
circuit1.h(1)  # Porte de Hadamard

circuit1.save_statevector()

print(circuit1.draw(output='text'))

tcircuit1 = q.transpile(circuit1, simulator)
job = simulator.run(tcircuit1)
result = job.result()

coefficients = result.get_statevector()
print("Coefficient alpha1:", coefficients[0])
print("Coefficient beta1 :", coefficients[1])
print("Coefficient alpha2:", coefficients[2])
print("Coefficient beta2 :", coefficients[3])


### Partie B. Construction du circuit 2

# Circuit quantique avec 2 qbits
circuit2 = q.QuantumCircuit(2)

qubit_initial1 = circuit1.initialize(etat_initial1, [0])
qubit_initial2 = circuit1.initialize(etat_initial2, [1])


circuit2.cx(1, 0) # CNOT inversé

circuit2.save_statevector()

print(circuit2.draw(output='text'))

tcircuit2 = q.transpile(circuit2, simulator)
job = simulator.run(tcircuit2)
result = job.result()

coefficients = result.get_statevector()
print("Coefficient alpha1:", coefficients[0])
print("Coefficient beta1 :", coefficients[1])
print("Coefficient alpha2:", coefficients[2])
print("Coefficient beta2 :", coefficients[3])