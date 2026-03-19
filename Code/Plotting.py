import skrf as rf

ntwk = rf.Network("../Data/2adapter_phase.sp1")

# Frequencies
print(ntwk.f)

# S-parameters (complex values)
print(ntwk.s)

# Example: print S11
s11 = ntwk.s[:, 0, 0]
print(s11)