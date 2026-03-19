import skrf as rf
import matplotlib.pyplot as plt
import numpy as np
import re

#left to right
path1 = "SN52934P_phase.s1p"
path2 = "SN52984P_phase.s1p"
path3 = "SN52994P_phase.s1p"
path4 = "SN368354P_phase.s1p"


paths = [path1, path2, path3, path4]
color = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']

def plot_phase_of_wires():
    fig, ax1 = plt.subplots()
    #ax2 = ax1.twinx() 
    j = 0
    color = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
    for i in paths:
        ntwk = rf.Network(i)  # Replace with your filename
        freq = ntwk.f  # frequency array
        s11 = ntwk.s[:,0,0]  # complex S11
        phase = np.angle(s11, deg=True)
        loss = -20 * np.log10(np.abs(s11))
        ax1.plot(freq, phase, label = i.split('_')[0], color = color[j])
        #ax2.plot(freq, loss, label = i, color = color[j])
        j += 1


    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_ylabel('Phase (degrees)')
    ax1.legend()
    ax1.set_xlim(2e9, 3e9)
    ax1.tick_params(axis='y')

    # instantiate a second axes that shares the same x-axis
    color = 'tab:red'
    #ax2.set_ylabel('Return Loss (dB)')

    #ax2.tick_params(axis='y')

    plt.title('Phaseshift of s11 for all wires')
    plt.savefig("Pictures/PhaseShift_all.png", dpi=300, bbox_inches='tight')
    plt.show()


def plot_loss_of_wires():
    fig, ax1 = plt.subplots()
    #ax2 = ax1.twinx() 
    j = 0
    color = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']
    for i in paths:
        ntwk = rf.Network(i)  # Replace with your filename
        freq = ntwk.f  # frequency array
        s11 = ntwk.s[:,0,0]  # complex S11
        phase = np.angle(s11, deg=True)
        loss = -20 * np.log10(np.abs(s11))
        ax1.plot(freq, loss, label = i.split('_')[0], color = color[j])
        #ax2.plot(freq, loss, label = i, color = color[j])
        j += 1


    ax1.set_ylabel('Loss (dB)')
    ax1.set_xlabel('Frequency (Hz)')
    ax1.legend()
    ax1.set_xlim(2e9, 3e9)
    ax1.tick_params(axis='y')

    # instantiate a second axes that shares the same x-axis
    color = 'tab:red'
    #ax2.set_ylabel('Return Loss (dB)')

    #ax2.tick_params(axis='y')

    plt.title('S11 loss for all wires')
    plt.savefig("Pictures/Loss_all_wires.png", dpi=300, bbox_inches='tight')
    plt.show()
    

def print_loss_and_phaseshift_at_2_and_2_4ghz_and_2_6ghz():
    for i in paths:
        ntwk = rf.Network(i)  # Replace with your filename
        freq = ntwk.f  # frequency array
        s11 = ntwk.s[:,0,0]  # complex S11
        phase = np.angle(s11, deg=True)
        loss = -20 * np.log10(np.abs(s11))
        idx_2ghz = np.argmin(np.abs(freq - 2e9))
        idx_2_4ghz = np.argmin(np.abs(freq - 2.4e9))
        idx_2_6ghz = np.argmin(np.abs(freq - 2.6e9))
        print(f"{i.split('_')[0]}: Loss at 2 GHz: {loss[idx_2ghz]:.2f} dB, Phase shift at 2 GHz: {phase[idx_2ghz]:.2f} degrees")
        print(f"{i.split('_')[0]}: Loss at 2.4 GHz: {loss[idx_2_4ghz]:.2f} dB, Phase shift at 2.4 GHz: {phase[idx_2_4ghz]:.2f} degrees")
        print(f"{i.split('_')[0]}: Loss at 2.6 GHz: {loss[idx_2_6ghz]:.2f} dB, Phase shift at 2.6 GHz: {phase[idx_2_6ghz]:.2f} degrees")


plot_phase_of_wires()
plot_loss_of_wires()
print_loss_and_phaseshift_at_2_and_2_4ghz_and_2_6ghz()