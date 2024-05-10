import tkinter as tk

import matplotlib
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
import seaborn as sns


class FootballScorersAnalyzerMODEL:
    def __init__(self):
        self.df = pd.read_csv("Football_Scorers_Analyzer.csv")

    def describe_data(self):
        """Compute the descriptive statistics of the data"""
        if "Year" in self.df.columns:
            return self.df.drop(columns=["Year"]).select_dtypes(
                include=['int64', 'float64']).describe()
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

            return canvas

    def get_correlation(self, key1, key2, display_frame):
        """Compute and display the correlation graph between two keys"""
        graph_color = ["red", "green", "blue", "purple"]
        if key1 in self.df.columns and key2 in self.df.columns:
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.scatterplot(data=self.df, x=key1, y=key2,
                             color=random.choice(graph_color), ax=ax)
            ax.set_xlabel(key1)
            ax.set_ylabel(key2)
            ax.set_title(f'Correlation between {key1} and {key2}')
            ax.grid(True)
            plt.tight_layout()

            # Plot the graph in the display frame
            canvas = FigureCanvasTkAgg(fig, master=display_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            return canvas

    def get_top_ranked(self, key1, key2, display_frame):
        """Display the top 5 players in a selected year based on the selected key"""
        graph_color = ["red", "green", "blue", "purple"]
        year_selected = self.df[self.df['Year'] == int(key1)]
        year_selected = year_selected.sort_values(by='Goals',
                                                  ascending=False)
        top10 = year_selected.head(5)
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(data=top10, x=str(key2), y='Goals', color=random.choice(graph_color),
                    ax=ax)
        ax.set_xlabel(key2)
        ax.set_ylabel('Goals')
        ax.set_title(f'Top 5 {key2} in {key1}')
        ax.grid(True)
        plt.tight_layout()

        # Plot the graph in the display frame
        canvas = FigureCanvasTkAgg(fig, master=display_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        return canvas

    def get_player_names(self):
        return self.df["Player Names"].value_counts()[self.df["Player Names"].value_counts() >= 3].index.tolist()

    def get_club_names(self):
        return self.df["Club"].value_counts().index.tolist()

    def get_league_names(self):
        return self.df["League"].value_counts().index.tolist()

    def get_timeseries(self, key1, key2, key3, display_frame):
        """Plot the time series graph(2016 - 2020) of the selected key
        key1: column attribute, key2: stat that will be plotted on the y-axis
        x = Year"""
        graph_color = ["red", "green", "blue", "purple"]
        key_selected = self.df[self.df[key1] == key2]
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.lineplot(data=key_selected, x='Year', y=str(key3),
                     color=random.choice(graph_color), ax=ax)
        ax.set_xlabel('Year')
        ax.set_ylabel(key3)
        ax.set_title(f'Time Series of {key3} for {key2}')
        ax.grid(True)
        plt.tight_layout()

        # Plot the graph in the display frame
        canvas = FigureCanvasTkAgg(fig, master=display_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


