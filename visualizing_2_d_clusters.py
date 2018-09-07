import numpy as np
import matplotlib.pyplot as plt

SAMPLES = 100

RED_COLOR    = "#E25151"
ORANGE_COLOR = "#F45328"
GREEN_COLOR  = "#A0CE94" 
BLUE_COLOR   = "#738992"
PURPLE_COLOR = "#B300C4"

GRAPH_NAME = "visualizing_2_d_for_classification"

def generate_class_1_x_and_y():
    x = np.random.normal(0.75, 0.4, int(SAMPLES/2))    
    y = np.random.normal(0.75, 0.4, int(SAMPLES/2))
    return x, y
    
def generate_class_2_x_and_y():
    x = np.random.normal(-0.75, 0.4, int(SAMPLES/2))    
    y = np.random.normal(-0.75, 0.4, int(SAMPLES/2))
    return x, y
    
def plot_data(x1, x2, y1, y2):
    fig, ax = plt.subplots()
    
    ax.scatter(x1, y1, marker="o", color=ORANGE_COLOR, label = "Classs 1")
    ax.scatter(x2, y2, marker="x", color=GREEN_COLOR, label = "Class 2")
    
    #Some other common marker options for class 2
    #ax.scatter(x2, y2, marker="^", color=GREEN_COLOR, label = "Class 2")
    #ax.scatter(x2, y2, marker="s", color=GREEN_COLOR, label = "Class 2")
    #ax.scatter(x2, y2, marker="D", color=GREEN_COLOR, label = "Class 2")
    #ax.scatter(x2, y2, marker="*", color=GREEN_COLOR, label = "Class 2")
    #ax.scatter(x2, y2, marker=".", color=GREEN_COLOR, label = "Class 2")

                        
    ax.set_title("Two Class Classification Data Visualization")
    
    ax.legend
    ax.legend(loc='upper left')
    #ax.legend(loc='lower right')
    
    ax.set_xlabel("Feature X")
    ax.set_ylabel("Feature Y")
    
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    
    fig.show()
    fig.savefig("G:/My Drive/RIT/Teaching/" + GRAPH_NAME)
    
def main():
    x1, y1 = generate_class_1_x_and_y()
    x2, y2 = generate_class_2_x_and_y()
    plot_data(x1, x2, y1, y2)
    
if __name__ == '__main__':
    main()
    
