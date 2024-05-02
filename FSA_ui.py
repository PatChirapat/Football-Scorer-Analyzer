import tkinter as tk
from tkinter import ttk

class FootballScorersAnalyzerUI(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Football Scorers Analyzer")
        self.init_components()

    def init_components(self):
        self.welcome_page()

    def welcome_page(self) -> tk.Frame:
        welcome_frame = ttk.Frame(self)

        data_story_button = tk.Button(welcome_frame, text="DATA STORYTELLING",
                                      width=20, height=3)
        data_story_button.pack(side=tk.LEFT, padx=5, pady=5)

        corr_descrpt_button = tk.Button(welcome_frame,
                                        text="CORRELATION / "
                                             "DESCRIPTIVE STATISTICS",
                                        width=30, height=3)
        corr_descrpt_button.pack(side=tk.LEFT, padx=5, pady=5)

        perf_analyzer_button = tk.Button(welcome_frame,
                                         text="PERFORMANCE & TRENDS",
                                         width=20, height=3)
        perf_analyzer_button.pack(side=tk.LEFT, padx=5, pady=5)

        quit_button = tk.Button(welcome_frame, text="QUIT", width=10, height=3,
                                command=self.quit)
        quit_button.pack(side=tk.LEFT, padx=5, pady=5)

        welcome_frame.pack(side=tk.TOP, padx=5, pady=5)
        welcome_frame.columnconfigure(0, weight=1)

        return welcome_frame

    def run(self):
        self.mainloop()
