import skrf as rf
import matplotlib.pyplot as plt
import numpy as np
import re


path1 = "y13.s1p"
path2 = "y13_5.s1p"
path3 = "y14.s1p"
path4 = "y15.s1p"
paths = [path1, path2, path3, path4]


def plot_all_feeds():
    for i in paths:
        ntwk = rf.Network(i)
        ntwk.plot_s_smith(m=0, n=0)  # m=n=0 means S11





    plt.title("S11 Smith Chart for all antenna feeds")
    plt.savefig("Pictures/S11_Smith_Chart_all.png", dpi=300, bbox_inches='tight')
    plt.show()

def plot_all_feeds_normal_graph():
    for i in paths:
        ntwk = rf.Network(i)
        ntwk.plot_s_db(m=0, n=0)  # m=n=0 means S11





    plt.title("S11 for all antenna feeds")
    plt.savefig("Pictures/S11_Normal_Graph_all.png", dpi=300, bbox_inches='tight')
    plt.show()


def plot_individual_feeds():
    for i in paths:
        ntwk = rf.Network(i)
        ntwk.plot_s_smith(m=0, n=0)  # m=n=0 means S11
        match = re.match(r"y([\d_]+)\.", i)
    
        print(match.group(1).replace("_", "."))
        plt.title("S11 Smith Chart for antenna with feedpoint at y = " + match.group(1).replace("_", ".") + "mm")
        plt.savefig("Pictures/S11_Smith_Chart_" + match.group(1).replace("_", ".") + ".png", dpi=300, bbox_inches='tight')
        plt.show()



def find_smallest_s11():
    for i in paths:
        ntwk = rf.Network(i)
        freq = ntwk.f
        s11 = ntwk.s[:,0,0]
        idx_min = np.argmin(np.abs(s11))
        print(f"Smallest |S11| for {i} is {np.abs(s11[idx_min])} at frequency {freq[idx_min]/1e9:.2f} GHz")

plot_all_feeds_normal_graph()