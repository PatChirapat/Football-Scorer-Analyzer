import tkinter as tk
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class FootballScorersAnalyzerMODEL:
    def __init__(self):
        self.df = pd.read_csv("Football_Scorers_Analyzer.csv")

    def describe_data(self):
        """Compute the descriptive statistics of the data"""
        if "Year" in self.df.columns:
            return self.df.drop(columns=["Year"]).select_dtypes(include=['int64', 'float64']).describe()
        return self.df.select_dtypes(include=['int64', 'float64']).describe()

    def get_distribution(self, key, display_frame):
        """Plot the distribution graph of the selected key"""
        graph_color = ["red", "green", "blue", "purple"]
        if key in self.df.columns:
            key_selected = self.df[key]
            fig, ax = plt.subplots(figsize=(6, 4))
            key_selected.hist(bins=10, color=random.choice(graph_color),
                              edgecolor='black',
                              ax=ax)
            ax.set_xlabel(key)
            ax.set_ylabel('Frequency')
            ax.set_title(f'Distribution of {key}')
            ax.grid(True)
            plt.tight_layout()

            # Plot the graph in the display frame
            canvas = FigureCanvasTkAgg(fig, master=display_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
