import numpy as np
import re
class SQASMInterpreter:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        # Initialize qubits in the |0> state
        self.qubits = np.zeros(num_qubits)
        # Classical bits for measurement results
        self.classical_bits = np.zeros(num_qubits, dtype=int)

    def apply_hadamard(self, qubit_idx):
        # Simplified Hadamard operation: Flips the state with 50% probability
        if np.random.rand() < 0.5:
            self.qubits[qubit_idx] = 1 - self.qubits[qubit_idx]

    def apply_cnot(self, control_idx, target_idx):
        # Simplified CNOT operation: If control is 1, flip the target
        if self.qubits[control_idx] == 1:
            self.qubits[target_idx] = 1 - self.qubits[target_idx]

    def measure(self, qubit_idx, classical_idx):
        # Simplified measurement: Collapse to 0 or 1 based on the qubit's value
        self.classical_bits[classical_idx] = int(self.qubits[qubit_idx])

    def execute(self, instructions):
        for line in instructions.strip().split('\n'):
            parts = line.split()
            if parts[0] == 'H':
                qbit = re.sub('\D', '', (parts[1]))
                self.apply_hadamard(int(qbit))
            elif parts[0] == 'CX':
                qbit1 = int(re.sub('\D', '', (parts[1])))
                qbit2 = int(re.sub('\D', '', (parts[2])))
                control, target = map( qbit1, qbit2)
                self.apply_cnot(control, target)
            elif parts[0] == 'measure':
                qubit_idx, classical_idx = map(int, [parts[1][2:-1], parts[3][2:-1]])
                self.measure(qubit_idx, classical_idx)

    def get_results(self):
        return self.classical_bits

sqasm_script = """
qreg q[2];
H q[0];
CX q[0], q[1];
measure q[0] -> c[0];
measure q[1] -> c[1];
"""
print(sqasm_script)
interpreter = SQASMInterpreter(num_qubits=2)
interpreter.execute(sqasm_script)
print("Measurement Results:", interpreter.get_results())