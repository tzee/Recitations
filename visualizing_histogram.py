import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

RED_COLOR    = "#E25151"
ORANGE_COLOR = "#F45328"
GREEN_COLOR  = "#A0CE94" 
BLUE_COLOR   = "#738992"
PURPLE_COLOR = "#B300C4"

GRAPH_NAME = "visualizing_histogram"

def main():
    mu, sigma = 0, 1
    x = mu + sigma*np.random.randn(10000)

    # the histogram of the data
    fig, ax = plt.subplots()

    n, bins, patches = ax.hist(x, bins=20, normed=1, facecolor=BLUE_COLOR, alpha=0.75)
    
    ax.set_xlabel("Samples")
    ax.set_ylabel("Probability Density")
    ax.set_title("Sampling from a Normal Distribution PDF")
    ax.axis([-5, 5, 0, 0.5]) #X_axis_min, X_axis_max, Y_axis_min, Y_axis_max

    #Shows or hides gridlines
    ax.grid(True)

    fig.show()
    fig.savefig("G:/My Drive/RIT/Teaching/" + GRAPH_NAME)

if __name__ == '__main__':
    main()