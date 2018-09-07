import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pylab

SAMPLES = 50

RED_COLOR    = "#E25151"
ORANGE_COLOR = "#F45328"
GREEN_COLOR  = "#A0CE94" 
BLUE_COLOR   = "#738992"
PURPLE_COLOR = "#B300C4"

GRAPH_NAME = "visualizing_3d_data"

def generate_x_and_y():
    x = np.random.uniform(0, 1, SAMPLES)
    
    noise = np.random.normal(0, .5, SAMPLES)
    
    y = (x * 3) + noise

    z = (x * 2.5) + noise
    return x, y, z
    
def plot_data(x, y, z):
    #fig = pylab.figure()
    fig = pylab.figure(figsize=(7,7))
    ax = fig.add_subplot(111, projection = '3d')
    

    ax.scatter(x, y, z, color=BLUE_COLOR)
    
    ax.set_title("Feature X vs Feature Y vs Feature Z")
    
    ax.set_xlabel("Feature X")
    ax.set_ylabel("Feature Y")
    ax.set_zlabel("Feature Z")
    
    #ax.set_xlim([-0.05, 1.05])
    #ax.set_ylim([-1.5, 4.5])
    #ax.set_zlim([0, 0])
    
    fig.show()
    fig.savefig("G:/My Drive/RIT/Teaching/" + GRAPH_NAME)
    
def main():
    x, y, z = generate_x_and_y()
    plot_data(x, y, z)
    
if __name__ == '__main__':
    main()