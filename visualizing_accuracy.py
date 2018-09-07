
import numpy as np
import matplotlib.pyplot as plt

SAMPLES = 20

RED_COLOR    = "#E25151"
ORANGE_COLOR = "#F45328"
GREEN_COLOR  = "#A0CE94" 
BLUE_COLOR   = "#738992"
PURPLE_COLOR = "#B300C4"

GRAPH_NAME = "visualizing_accuracy"

def generate_accuracy():

    accuracy = np.zeros(SAMPLES)
    noise = np.random.normal(0, .05, SAMPLES)
    
    for i in range(SAMPLES):
        val = (np.log(i) - noise[i]) / np.log(SAMPLES)
        val = np.maximum(val, 0)
        val = np.minimum(val, .95)
        accuracy[i] = val
    
    return accuracy
    
def plot_data(y):
    fig, ax = plt.subplots()
    
    x = np.linspace(0, 100, SAMPLES)
    
    #ax.plot(x, y, color=PURPLE_COLOR)
    ax.plot(x, y, color=PURPLE_COLOR, marker="o")
    
    ax.set_title("Training Accuracy over Epochs")
    
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Accuracy (%)")
    
    fig.show()
    fig.savefig("G:/My Drive/RIT/Teaching/" + GRAPH_NAME)
    
def main():
    accuracy = generate_accuracy()
    plot_data(accuracy)
    
if __name__ == '__main__':
    main()