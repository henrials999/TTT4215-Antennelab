import skrf as rf
import matplotlib.pyplot as plt
import numpy as np

path1 = "coupling_full_wave_mag.s1p"
path2 = "coupling_half_wave_mag.s1p"

paths = [path1, path2]

def plot_coupling():
    for path in paths:
        ntwk = rf.Network(path)  
        freq = ntwk.f            
        mag = ntwk.s_mag[:,0,0] 
        phase = ntwk.s_deg[:,0,0] 
        f_target = 2.4e9
        idx = np.argmin(np.abs(freq - f_target))
        plt.plot(freq, mag, label=f'Magnitude {path}')
        #plt.plot(freq, phase, label=f'Phase {path}')
        plt.show()

    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude(db)")
    plt.title("S11 magnitudeCoupling Magnitude")
    plt.legend()
    #plt.savefig("Coupling_Magnitude_Phase.png", dpi=300, bbox_inches='tight')
    


plot_coupling()