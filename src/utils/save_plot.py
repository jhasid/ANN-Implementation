import pandas as pd
import os
import matplotlib.pyplot as plt
import time

def get_unique_filename(filename):
    unique_filename = time.strftime(f"%Y%m%d_%H%M%S_{filename}")  # h5 is the file keras saves as model
    return unique_filename

def save_plot(df,plot_name,plot_dir):
    df.plot(figsize=(8,5))
    plt.grid(True)
    plt.gca().set_ylim(0,1)

    unique_filename = get_unique_filename(plot_name)
    path_to_plot = os.path.join(plot_dir, unique_filename)
    #os.makedirs(plot_dir,exist_ok=True)
    #plotpath= os.path.join(plot_dir,plot_name)
    plt.savefig(path_to_plot)
    plt.show()
