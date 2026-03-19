import skrf as rf
import matplotlib.pyplot as plt
import numpy as np

path1 = "adapter_phase_fixed.s1p"
path2 = "2adapter_phase_fixed.s1p"
path3 = "3adapter_phase_fixed.s1p"


def plot_1_adapter():
    ntwk = rf.Network(path1)  
    freq = ntwk.f            
    phase = ntwk.s_deg[:,0,0] 
    f_target = 2.4e9
    idx = np.argmin(np.abs(freq - f_target))
    plt.plot(freq, phase)

    plt.plot(freq[idx], phase[idx], 'ko')  # red dot

    # Add text in the format (freq, phase)
    # Format frequency to 2 decimal GHz, phase to 1 decimal deg
    label_text = f"({freq[idx]/1e9:.2f} GHz, {phase[idx]:.1f}°)"
    plt.annotate(label_text,
                xy=(freq[idx], phase[idx]),
                xytext=(5, 0),          # offset text slightly
                textcoords='offset points',
                color='black',
                fontsize=10,
                )



    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (deg)")
    plt.title("S11 Phase single adapter")
    plt.savefig("S11_Phase_single adapter.png", dpi=300, bbox_inches='tight')
    plt.show()
def plot_2_adapter():
    ntwk = rf.Network(path2)  
    freq = ntwk.f            
    phase = ntwk.s_deg[:,0,0] 
    f_target = 2.4e9
    idx = np.argmin(np.abs(freq - f_target))
    plt.plot(freq, phase)

    plt.plot(freq[idx], phase[idx], 'ko')  # red dot

    # Add text in the format (freq, phase)
    # Format frequency to 2 decimal GHz, phase to 1 decimal deg
    label_text = f"({freq[idx]/1e9:.2f} GHz, {phase[idx]:.1f}°)"
    plt.annotate(label_text,
                xy=(freq[idx], phase[idx]),
                xytext=(5, 0),          # offset text slightly
                textcoords='offset points',
                color='black',
                fontsize=10,
                )



    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (deg)")
    plt.title("S11 Phase double adapter")
    plt.savefig("S11_Phase_double_adapter.png", dpi=300, bbox_inches='tight')
    plt.show()

def plot_3_adapter():
    ntwk = rf.Network(path3)  
    freq = ntwk.f            
    phase = ntwk.s_deg[:,0,0] 
    f_target = 2.4e9
    idx = np.argmin(np.abs(freq - f_target))
    plt.plot(freq, phase)

    plt.plot(freq[idx], phase[idx], 'ko')  # red dot

    # Add text in the format (freq, phase)
    # Format frequency to 2 decimal GHz, phase to 1 decimal deg
    label_text = f"({freq[idx]/1e9:.2f} GHz, {phase[idx]:.1f}°)"
    plt.annotate(label_text,
                xy=(freq[idx], phase[idx]),
                xytext=(5, 0),          # offset text slightly
                textcoords='offset points',
                color='black',
                fontsize=10,
                )



    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (deg)")
    plt.title("S11 Phase triple adapter")
    plt.savefig("S11_Phase_triple_adapter.png", dpi=300, bbox_inches='tight')

    plt.show()


plot_1_adapter()
plot_2_adapter()
plot_3_adapter()