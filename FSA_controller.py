from FSA_model import FootballScorersAnalyzerMODEL
from FSA_ui import FootballScorersAnalyzerUI
import tkinter as tk
from tkinter import ttk


class FootballScorersAnalyzerCONTROLLER:
    def __init__(self):
        self.model = FootballScorersAnalyzerMODEL()
        self.view = FootballScorersAnalyzerUI(self)

    def get_desciptive_statistics_keys(self):
        descriptive_keys = self.model.describe_data()
        return descriptive_keys

    def get_descriptive_statistics_values(self, key):
        return self.model.describe_data()[key]

    def run(self):
        self.view.run()
