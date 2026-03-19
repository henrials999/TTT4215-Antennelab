import skrf as rf
import matplotlib.pyplot as plt
import numpy as np
import h5py


E_plane_full_wavelength = "E_plane_patch_array_full_w_phaseshift.h5ant"
E_plane_half_wavelength = "E_plane_patch_array_half_w_phaseshift.h5ant"




with h5py.File(E_plane_full_wavelength,'r') as f:
    key_list=list(f.keys())
    #print(key_list)
    Full_wavelength_data={}
    for i in key_list:
        Full_wavelength_data[i]=f[i][:]


with h5py.File(E_plane_half_wavelength,'r') as f:
    key_list=list(f.keys())
    #print(key_list)
    half_wavelength_data={}
    for i in key_list:
        half_wavelength_data[i]=f[i][:]



for i in range(9):
    # Convert angles to radians for polar plotting
    angles_rad = np.deg2rad(Full_wavelength_data["angles"])  # degrees → radians

    # Choose the dataset column you want to plot (e.g., column 3)
    powers = np.array(Full_wavelength_data["powers"])  # ensure it's a NumPy array
    data_to_plot = powers[:, i]

    # Create a polar plot
    fig, ax = plt.subplots(figsize=(15, 10), subplot_kw={'projection': 'polar'})
    ax.plot(angles_rad, data_to_plot  - np.max(data_to_plot), label="E-plane", color='blue')

    # Optional: add labels and styling
    ax.set_theta_zero_location('N')  # 0 degrees at the top
    ax.set_theta_direction(-1)       # clockwise
    ax.set_rlabel_position(90) 
    ax.set_rmin(-20)      # radial labels on the left
    print("FULL:E_field_max power for frequency " + str(Full_wavelength_data["frequencies"][i]) + "GHz: ", np.max(data_to_plot))
    print()
    plt.savefig("Pictures/Array_W_phasediff_Full_wavelength_E_plane_Normalised_Radiation_pattern_at_frequency_" + str(Full_wavelength_data["frequencies"][i]) + "GHz.png", dpi=300, bbox_inches='tight')
    #plt.show()
print()
print()
print()

for i in range(9):
    # Convert angles to radians for polar plotting
    angles_rad = np.deg2rad(half_wavelength_data["angles"])  # degrees → radians

    # Choose the dataset column you want to plot (e.g., column 3)
    powers = np.array(half_wavelength_data["powers"])  # ensure it's a NumPy array
    data_to_plot = powers[:, i]

    # Create a polar plot
    fig, ax = plt.subplots(figsize=(15, 10), subplot_kw={'projection': 'polar'})
    ax.plot(angles_rad, data_to_plot  - np.max(data_to_plot), label="E-plane", color='blue')

    # Optional: add labels and styling
    ax.set_theta_zero_location('N')  # 0 degrees at the top
    ax.set_theta_direction(-1)       # clockwise
    ax.set_rlabel_position(90) 
    ax.set_rmin(-20)      # radial labels on the left

    print("HALF:E_field_max power for frequency " + str(half_wavelength_data["frequencies"][i]) + "GHz: ", np.max(data_to_plot))
    print()
    plt.savefig("Pictures/Array_W_phasediff_Half_wavelength_E_plane_Normalised_Radiation_pattern_at_frequency_" + str(half_wavelength_data["frequencies"][i]) + "GHz.png", dpi=300, bbox_inches='tight')
    #plt.show()
