import tkinter as tk
from tkinter import messagebox

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
        """Initialize the model by loading the dataset."""
        self.df = pd.read_csv("Football_Scorers_Analyzer.csv")

    def describe_data(self):
        """Compute the descriptive statistics of the data"""
        if "Year" in self.df.columns:
            return self.df.drop(columns=["Year"]).select_dtypes(
                include=['int64', 'float64']).describe()
        return self.df.select_dtypes(include=['int64', 'float64']).describe()

    def get_distribution(self, key, display_frame):
        """Plot the distribution graph of the selected key.

        Parameters:
            key (str): The column name for which distribution is to be plotted.
            display_frame (tk.Frame): The frame where the graph will be displayed.

        Returns:
            FigureCanvasTkAgg: The canvas containing the plotted graph.
        """
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
        """Compute and display the correlation graph between two keys.

        Parameters:
            key1 (str): The first column name for correlation.
            key2 (str): The second column name for correlation.
            display_frame (tk.Frame): The frame where the graph will be displayed.

        Returns:
            FigureCanvasTkAgg: The canvas containing the plotted graph.
        """
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
        """Display the top 5 players in a selected year based on the selected key.

        Parameters:
            key1 (str): The selected year.
            key2 (str): The attribute based on which top players are to be selected.
            display_frame (tk.Frame): The frame where the graph will be displayed.

        Returns:
            FigureCanvasTkAgg: The canvas containing the plotted graph.
        """
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
        """Get the list of player names."""
        return self.df["Player Names"].value_counts()[self.df["Player Names"].value_counts() >= 3].index.tolist()

    def get_club_names(self):
        """Get the list of club names."""
        return self.df["Club"].value_counts().index.tolist()

    def get_league_names(self):
        """Get the list of league names."""
        return self.df["League"].value_counts().index.tolist()

    def get_timeseries(self, key1, key2, key3, display_frame):
        """Plot the time series graph(2016 - 2020) of the selected key.

        Parameters:
            key1 (str): Column attribute.
            key2 (str): Category for which time series will be plotted.
            key3 (str): Stat that will be plotted on the y-axis.
            display_frame (tk.Frame): The frame where the graph will be displayed.

        Returns:
            FigureCanvasTkAgg: The canvas containing the plotted graph.
        """
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

        return canvas

    def get_comparing(self, key1, key2, key3, key4, display_frame):
        """Compare and display the stats of key2 and key3 for a selected category key1.

        Parameters:
            key1 (str): Category.
            key2 (str): First stat.
            key3 (str): Second stat.
            key4 (str): Wanted stat.
            display_frame (tk.Frame): The frame where the graph will be displayed.

        Returns:
            FigureCanvasTkAgg: The canvas containing the plotted graph.
        """
        graph_color = ["red", "green", "blue", "purple"]

        if key2 == key3:
            messagebox.showwarning("Warning",
                                   "Do not select the same stats for comparison.")
            return None

        selected_keys = self.df[
            (self.df[key1] == key2) | (self.df[key1] == key3)]

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=selected_keys, x='Year', y=str(key4), hue=key1,
                    palette=random.sample(graph_color, 2), dodge=True, ax=ax)
        ax.set_xlabel('Year')
        ax.set_ylabel(key4)
        ax.set_title(f'Comparison stats of {key2} and {key3}')
        ax.grid(True)
        ax.legend()
        plt.tight_layout()

        # Plot the graph in the display frame
        canvas = FigureCanvasTkAgg(fig, master=display_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        return canvas

    def factors_affecting_goals(self, display_frame):
        """Display the factors affecting the goals."""
        total_matches = self.df["Matches Played"].sum()
        total_goals = self.df["Goals"].sum()
        avg_goals = total_goals / total_matches
        total_xGoals = self.df["Expected Goals"].sum()
        avg_xGoals = total_xGoals / total_matches
        total_shots = self.df["Shots"].sum()
        avg_shots = total_shots / total_matches
        total_shots_target = self.df["On Target"].sum()
        avg_shots_target = total_shots_target / total_matches

        text = f"Total Matches Played: {total_matches}\n" \
               f"Total Goals Scored: {total_goals}\n" \
               f"Average Goals per Match: {avg_goals:.2f}\n" \
               f"Total Expected Goals: {total_xGoals}\n" \
               f"Average Expected Goals per Match: {avg_xGoals:.2f}\n" \
               f"Total Shots Taken: {total_shots}\n" \
               f"Average Shots per Match: {avg_shots:.2f}\n" \
               f"Total Shots on Target: {total_shots_target}\n" \
               f"Average Shots on Target per Match: {avg_shots_target:.2f}\n"

        label = tk.Label(display_frame, text=text)
        label.pack()

        return label

    def factors_correlation(self,key1, key2, display_frame):
        """Display the correlation graph between the factors."""
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.scatterplot(data=self.df, x=key1, y=key2, ax=ax)
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

    def top10_scorers(self):
        """Get the top 10 scorers names in dataset"""
        top10 = self.df.sort_values(by='Goals', ascending=False).head(10)
        return top10["Player Names"].tolist()

    def top10_stats(self, key1, key2, display_frame):
        """Display the graph of player with goals in top 10."""
        top10 = self.df.sort_values(by='Goals', ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(data=top10, x='Player Names', y=str(key1), ax=ax)
        ax.set_xlabel('Player Names')
        ax.set_ylabel(key1)
        ax.set_title(f'Top 10 Scorers in the Dataset')
        ax.grid(True)
        plt.tight_layout()

        # Plot the graph in the display frame
        canvas = FigureCanvasTkAgg(fig, master=display_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        return canvas

    def fac_top_ranked(self, key1, key2, display_frame):
        """Display the top 5 players in a selected year based on the selected key.

        Parameters:
            key1 (str): The selected year.
            key2 (str): The attribute based on which top players are to be selected.
            display_frame (tk.Frame): The frame where the graph will be displayed.

        Returns:
            FigureCanvasTkAgg: The canvas containing the plotted graph.
        """
        graph_color = ["red", "green", "blue", "purple"]
        year_selected = self.df[self.df['Year'] == int(key1)]
        year_selected = year_selected.sort_values(by=str(key2),
                                                  ascending=False)
        top10 = year_selected.head(5)
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(data=top10, x='Player Names', y=str(key2),
                    color=random.choice(graph_color), ax=ax)
        ax.set_xlabel('Player Names')
        ax.set_ylabel(key2)
        ax.set_title(f'Top 5 Players in {key1}')
        ax.grid(True)
        plt.tight_layout()

        # Plot the graph in the display frame
        canvas = FigureCanvasTkAgg(fig, master=display_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        return canvas

    def fac_comparing_values(self, key1, key2, key3, key4, display_frame):
        """Compare and display the stats of key2 and key3 for a selected category key1.

        Parameters:
            key1 (str): Category.
            key2 (str): First stat.
            key3 (str): Second stat.
            key4 (str): Wanted stat.
            display_frame (tk.Frame): The frame where the graph will be displayed.

        Returns:
            FigureCanvasTkAgg: The canvas containing the plotted graph.
        """
        graph_color = ["red", "green", "blue", "purple"]

        if key2 == key3:
            messagebox.showwarning("Warning",
                                   "Do not select the same stats for comparison.")
            return None

        selected_keys = self.df[
            (self.df[key1] == key2) | (self.df[key1] == key3)]

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=selected_keys, x='Year', y=str(key4), hue=key1,
                    palette=random.sample(graph_color, 2), dodge=True, ax=ax)
        ax.set_xlabel('Year')
        ax.set_ylabel(key4)
        ax.set_title(f'Comparison stats of {key2} and {key3}')
        ax.grid(True)
        ax.legend()
        plt.tight_layout()

        # Plot the graph in the display frame
        canvas = FigureCanvasTkAgg(fig, master=display_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        return canvas

    def fac_timeseries_values(self, key1, key2, display_frame):
        """Display timeseries line graph of the selected key.
        key1 = player name
        key2 = goals
        """
        graph_color = ["red", "green", "blue", "purple"]
        key_selected = self.df[self.df["Player Names"] == key1]
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.lineplot(data=key_selected, x='Year', y=str(key2),
                     color=random.choice(graph_color), ax=ax)
        ax.set_xlabel('Year')
        ax.set_ylabel(key2)
        ax.set_title(f'Time Series of {key2} for {key1}')
        ax.grid(True)
        plt.tight_layout()

        # Plot the graph in the display frame
        canvas = FigureCanvasTkAgg(fig, master=display_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        return canvas
