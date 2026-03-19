import skrf as rf
import matplotlib.pyplot as plt
import numpy as np
import h5py


E_plane = "E_plane_y14.h5ant"
H_plane = "H_plane_y14.h5ant"
Calibrated = "calibrated_patch_y14_ets_lindgren_3117_0azim_0elev.s2p" #vet egt ikke hva denne calibreringen er for. kan være for å finne gain?



with h5py.File(E_plane,'r') as f:
    key_list=list(f.keys())
    #print(key_list)
    E_data={}
    for i in key_list:
        E_data[i]=f[i][:]


with h5py.File(H_plane,'r') as f:
    key_list=list(f.keys())
    #print(key_list)
    H_data={}
    for i in key_list:
        H_data[i]=f[i][:]

with h5py.File(E_plane, "r") as f:
    def show(name, obj):
        if isinstance(obj, h5py.Dataset):
            print(f"{name} -> shape: {obj.shape}")
    f.visititems(show)


powers = np.array(E_data["powers"])
angles = np.array(E_data["angles"])
frequencies = np.array(E_data["frequencies"])
velocities = np.array(E_data["velocities"])


for i in range(9):
    # Convert angles to radians for polar plotting
    angles_rad = np.deg2rad(E_data["angles"])  # degrees → radians

    # Choose the dataset column you want to plot (e.g., column 3)
    powers = np.array(E_data["powers"])  # ensure it's a NumPy array
    data_to_plot = powers[:, i]

    # Create a polar plot
    fig, ax = plt.subplots(figsize=(15, 10), subplot_kw={'projection': 'polar'})
    ax.plot(angles_rad, data_to_plot  - np.max(data_to_plot), label="E-plane", color='blue')

    # Optional: add labels and styling
    ax.set_theta_zero_location('N')  # 0 degrees at the top
    ax.set_theta_direction(-1)       # clockwise
    ax.set_rlabel_position(90)       # radial labels on the left
    print("E_field_max power for frequency " + str(frequencies[i]) + "GHz: ", np.max(data_to_plot))
    plt.savefig("Pictures/E_plane_Normalised_Radiation_pattern_at_frequency_" + str(frequencies[i]) + "GHz.png", dpi=300, bbox_inches='tight')


for i in range(9):
    # Convert angles to radians for polar plotting
    angles_rad = np.deg2rad(H_data["angles"])  # degrees → radians

    # Choose the dataset column you want to plot (e.g., column 3)
    powers = np.array(H_data["powers"])  # ensure it's a NumPy array
    data_to_plot = powers[:, i]

    # Create a polar plot
    fig, ax = plt.subplots(figsize=(15, 10), subplot_kw={'projection': 'polar'})
    ax.plot(angles_rad, data_to_plot  - np.max(data_to_plot), label="H-plane", color='red')

    # Optional: add labels and styling
    ax.set_theta_zero_location('N')  # 0 degrees at the top
    ax.set_theta_direction(-1)       # clockwise
    ax.set_rlabel_position(90)       # radial labels on the left
    print("H_field_max power for frequency " + str(frequencies[i]) + "GHz: ", np.max(data_to_plot))
    plt.savefig("Pictures/H_plane_Normalised_Radiation_pattern_at_frequency_" + str(frequencies[i]) + "GHz.png", dpi=300, bbox_inches='tight')
