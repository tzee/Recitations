
import numpy as np
import matplotlib.pyplot as plt

SAMPLES = 50

RED_COLOR    = "#E25151"
ORANGE_COLOR = "#F45328"
GREEN_COLOR  = "#A0CE94" 
BLUE_COLOR   = "#738992"
PURPLE_COLOR = "#B300C4"

GRAPH_NAME = "visualizing_2_d_for_regression"

def generate_x_and_y():
    x = np.random.uniform(0, 1, SAMPLES)
    
    noise = np.random.normal(0, .5, SAMPLES)
    
    y = (x * 3) + noise
    return x, y
    
def plot_data(x, y):
    fig, ax = plt.subplots()
    
    #uses predefined color
    #ax.scatter(x, y, color='orange')
    
    #uses custom color
    ax.scatter(x, y, color=RED_COLOR)
    
    ax.set_title("Feature X vs Feature Y")
    
    ax.set_xlabel("Feature X")
    ax.set_ylabel("Feature Y")
    
    ax.set_xlim([-0.05, 1.05])
    ax.set_ylim([-1.5, 4.5])
    
    fig.show()
    fig.savefig("G:/My Drive/RIT/Teaching/" + GRAPH_NAME)
    
def main():
    x, y = generate_x_and_y()
    plot_data(x, y)
    
if __name__ == '__main__':
    main()