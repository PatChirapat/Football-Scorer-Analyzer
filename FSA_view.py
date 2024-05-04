import tkinter as tk
from tkinter import ttk


class FootballScorersAnalyzerUI(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.information_display_frame = None
        self.information_menu_frame = None
        self.navbar_frame = None
        self.controller = controller
        self.bind("<Button-1>", self.init_components)
        self.title("Football Scorers Analyzer")
        self.welcome_page()

    def init_components(self, event=None):
        """Initialize the components of the application"""
        self.unbind("<Button-1>")

        # clear start page
        for widget in self.winfo_children():
            widget.destroy()

        self.navbar_frame = tk.LabelFrame(self,
                                          text="NAVIGATION BAR")
        self.navbar_frame.pack(side=tk.TOP,
                               fill=tk.Y)

        self.information_menu_frame = tk.LabelFrame(self,
                                                    text="SELECTOR")
        menu_label = tk.Label(self.information_menu_frame,
                              text="SELECT A MENU FROM THE NAVIGATION BAR...",
                              font=("Courier", 15))
        menu_label.pack(expand=True)
        self.information_menu_frame.pack(side=tk.LEFT,
                                         fill=tk.BOTH,
                                         expand=True,
                                         ipadx=5,
                                         ipady=5)

        self.information_display_frame = tk.LabelFrame(self, text="DISPLAY")
        display_label = tk.Label(self.information_display_frame,
                                 text="DISPLAY WILL APPEAR HERE...",
                                 font=("Courier", 15))
        display_label.pack(expand=True)
        self.information_display_frame.pack(side=tk.LEFT,
                                            fill=tk.BOTH,
                                            expand=True,
                                            ipadx=5,
                                            ipady=5)
        self.nav_bar()

    def nav_bar(self):
        """The navigation bar for the application"""
        data_story_button = tk.Button(self.navbar_frame,
                                      text="DATA STORYTELLING",
                                      width=20,
                                      height=3)
        data_story_button.bind("<Button-1>", self.data_story_telling_page)
        data_story_button.grid(row=0,
                               column=0,
                               sticky=tk.NSEW,
                               ipadx=3,
                               ipady=3)

        descrpt_button = tk.Button(self.navbar_frame,
                                        text="DESCRIPTIVE STATISTICS",
                                        width=30,
                                        height=3)
        descrpt_button.bind("<Button-1>", self.descriptive_stats_page)
        descrpt_button.grid(row=0,
                            column=1,
                            sticky=tk.NSEW,
                            ipadx=3,
                            ipady=3)

        corr_button = tk.Button(self.navbar_frame,
                                text="CORRELATION",
                                width=30,
                                height=3)
        corr_button.bind("<Button-1>", self.correlation_stats_page)
        corr_button.grid(row=0,
                         column=2,
                         sticky=tk.NSEW,
                         ipadx=3,
                         ipady=3)

        distribution_button = tk.Button(self.navbar_frame,
                                        text="DISTRIBUTION GRAPH",
                                        width=20, height=3)
        distribution_button.bind("<Button-1>", self.distribution_graph_page)
        distribution_button.grid(row=0,
                                column=3,
                                sticky=tk.NSEW,
                                ipadx=3,
                                ipady=3)

        perf_trends_button = tk.Button(self.navbar_frame,
                                       text="PERFORMANCE & TRENDS",
                                       width=20, height=3)
        perf_trends_button.bind("<Button-1>", self.performance_trends_page)
        perf_trends_button.grid(row=0,
                                column=4,
                                sticky=tk.NSEW,
                                ipadx=3,
                                ipady=3)

        quit_button = tk.Button(self.navbar_frame, text="QUIT", width=10,
                                height=3,
                                command=self.quit)
        quit_button.grid(row=0,
                         column=5,
                         sticky=tk.NSEW,
                         ipadx=3,
                         ipady=3)

    def welcome_page(self):
        ascii_saved = """
    ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░        
    ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
    ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
    ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
    ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
    ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
    ░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░  ░▒▓█▓▒░   ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░ 
                                                                                                            
        ░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓███████▓▒░  
       ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         
       ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         
        ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░ ░▒▓██████▓▒░   
            ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░  
            ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░  
        ░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░   
                                                                                                        
     ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓███████▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░    ░▒▓██▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░
    ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░    ░▒▓██████▓▒░   ░▒▓██▓▒░  ░▒▓██████▓▒░ ░▒▓███████▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░    ░▒▓██▓▒░    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░   ░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░
        """
        ascii_frame = ttk.Frame(self)
        ascii_frame.pack(expand=True)
        ascii_label = tk.Label(ascii_frame, text=ascii_saved,
                               font=("Courier", 20))
        ascii_label.pack(expand=True)
        press_anywhere_label = tk.Label(ascii_frame,
                                        text="CLICK ANYWHERE TO CONTINUE...",
                                        font=("Courier", 15))
        press_anywhere_label.pack(expand=True)

    def data_story_telling_page(self, event=None):
        """Data storytelling page(in progress)"""
        # clear previous frame
        self.clearing_frame()

    def descriptive_stats_page(self, event=None):
        """Descriptive statistics page"""
        # clear previous frame
        self.clearing_frame()

        descriptive_menu = tk.Frame(self.information_menu_frame)
        descriptive_key = self.controller.get_descriptive_statistics_keys()
        descriptive_menu_listbox = tk.Listbox(descriptive_menu)
        for key, val in descriptive_key.items():
            descriptive_menu_listbox.insert(tk.END, key)
        descriptive_menu_listbox.bind("<<ListboxSelect>>",
                                      self.descriptive_stats_handler)
        descriptive_menu_listbox.pack(side=tk.LEFT,
                                      fill=tk.BOTH,
                                      expand=True)
        descriptive_menu.pack(side=tk.LEFT,
                              fill=tk.BOTH,
                              expand=True)

    def descriptive_stats_handler(self, event=None):
        """Display descriptive statistics"""
        for widget in self.information_display_frame.winfo_children():
            widget.destroy()

        selected_index = event.widget.curselection()
        if selected_index:
            menu_selected = event.widget.get(selected_index[0])

            # Get descriptive statistics for the selected attribute
            descriptive_statistics = self.controller.get_descriptive_statistics_values(menu_selected)

            # Display the descriptive statistics
            for key, value in descriptive_statistics.items():
                label = tk.Label(self.information_display_frame,
                                 text=f"{key}: {value}")
                label.pack()

    def correlation_stats_page(self, event=None):
        """Correlation statistics page(in progress)"""
        # clear previous frame
        self.clearing_frame()

    def distribution_graph_page(self, event=None):
        """Distribution graph page"""
        # clear previous frame
        self.clearing_frame()

        self.distribution_attributes = ["Goals",
                                   "Expected Goals",
                                   "Shots",
                                   "On Target"]
        distribution_menu = tk.Frame(self.information_menu_frame)
        distribution_menu_listbox = tk.Listbox(distribution_menu)
        for attribute in self.distribution_attributes:
            distribution_menu_listbox.insert(tk.END, attribute)
        distribution_menu_listbox.bind("<<ListboxSelect>>",
                                      self.distribution_graph_handler)
        distribution_menu_listbox.pack(side=tk.LEFT,
                                       fill=tk.BOTH,
                                       expand=True)
        distribution_menu.pack(side=tk.LEFT,
                               fill=tk.BOTH,
                               expand=True)

    def distribution_graph_handler(self, event=None):
        """Display distribution graph"""
        for widget in self.information_display_frame.winfo_children():
            widget.destroy()

        selected_index = event.widget.curselection()
        if selected_index:
            menu_selected = event.widget.get(selected_index[0])
            self.controller.get_distribution_values(menu_selected,
                                                    self.information_display_frame)

    def performance_trends_page(self, event=None):
        """Performance and trends page(in progress)"""
        # clear previous frame
        self.clearing_frame()

    def clearing_frame(self):
        """Clearing every widget in the frame"""
        for widget in self.information_menu_frame.winfo_children():
            widget.destroy()
        for widget in self.information_display_frame.winfo_children():
            widget.destroy()

    def run(self):
        self.mainloop()