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

    def descriptive_stats_handler(self, event=None, year_select=None):
        """Display descriptive statistics"""
        for widget in self.information_display_frame.winfo_children():
            widget.destroy()

        selected_index = event.widget.curselection()
        if selected_index:
            menu_selected = event.widget.get(selected_index[0])

            # Get descriptive statistics for the selected attribute
            descriptive_statistics = self.controller.get_descriptive_statistics_values(
                menu_selected)

            # Display the descriptive statistics
            for key, value in descriptive_statistics.items():
                label = tk.Label(self.information_display_frame,
                                 text=f"{key}: {value}")
                label.pack()

    def correlation_stats_page(self, event=None):
        """Correlation statistics page"""
        # clear previous frame
        self.clearing_frame()

        self.correlation_attributes = ["Matches Played and Goals",
                                       "On Target and Goals",
                                       "Expected Goals and Goals",
                                       "Shots and Goals"]
        correlation_menu = tk.Frame(self.information_menu_frame)
        correlation_menu_listbox = tk.Listbox(correlation_menu)
        for attribute in self.correlation_attributes:
            correlation_menu_listbox.insert(tk.END, attribute)
        correlation_menu_listbox.bind("<<ListboxSelect>>",
                                        self.correlation_stats_handler)
        correlation_menu_listbox.pack(side=tk.TOP,
                                        fill=tk.BOTH,
                                        expand=True)
        correlation_menu.pack(side=tk.LEFT,
                              fill=tk.BOTH,
                              expand=True)

    def correlation_stats_handler(self, event=None):
        """Display correlation statistics"""
        for widget in self.information_display_frame.winfo_children():
            widget.destroy()

        selected_index = event.widget.curselection()
        if selected_index:
            menu_selected = event.widget.get(selected_index[0])
            if menu_selected == "Matches Played and Goals":
                key1 = "Matches Played"
                key2 = "Goals"
            elif menu_selected == "On Target and Goals":
                key1 = "On Target"
                key2 = "Goals"
            elif menu_selected == "Expected Goals and Goals":
                key1 = "Expected Goals"
                key2 = "Goals"
            elif menu_selected == "Shots and Goals":
                key1 = "Shots"
                key2 = "Goals"
            self.controller.get_correlation_values(key1, key2,
                                                   self.information_display_frame)

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

        perf_trends_menu = tk.Frame(self.information_menu_frame)

        performance_button = tk.Button(perf_trends_menu,
                                      text="TOP SCORERS/LEAGUES",
                                      width=20,
                                      height=3)
        performance_button.bind("<Button-1>", self.toprank)
        performance_button.pack(side=tk.TOP,
                                fill=tk.BOTH,
                                expand=True)

        comparing_button = tk.Button(perf_trends_menu,
                                      text="COMPARING",
                                      width=20,
                                      height=3)
        comparing_button.bind("<Button-1>", self.comparing)
        comparing_button.pack(side=tk.TOP,
                              fill=tk.BOTH,
                              expand=True)

        timeseries_button = tk.Button(perf_trends_menu,
                                    text="TIMESERIES",
                                    width=20,
                                    height=3)
        timeseries_button.configure(command=self.timeseries)
        timeseries_button.pack(side=tk.TOP,
                            fill=tk.BOTH,
                            expand=True)

        perf_trends_menu.pack(side=tk.TOP,
                              fill=tk.BOTH,
                              expand=True)

    def toprank(self, event=None):
        """Performance handler(in progress)"""
        # clear previous frame
        self.clearing_frame()

        year_list = ["2016", "2017", "2018", "2019", "2020"]
        timeseries_list = ["TOP SCORERS", "TOP LEAGUES"]

        topranked_menu = tk.Frame(self.information_menu_frame)

        year_label = tk.Label(topranked_menu,
                              text="SELECT YEAR")
        year_label.pack(side=tk.TOP,
                        fill=tk.BOTH,
                        expand=True)
        self.year_combobox = ttk.Combobox(topranked_menu,
                                          values=year_list)
        self.year_combobox.pack(side=tk.TOP,
                                fill=tk.BOTH,
                                expand=True)

        timeseries_label = tk.Label(topranked_menu,
                                    text="SELECT CATEGORY")
        timeseries_label.pack(side=tk.TOP,
                              fill=tk.BOTH,
                              expand=True)
        self.tp_combobox = ttk.Combobox(topranked_menu,
                                        values=timeseries_list)
        self.tp_combobox.pack(side=tk.TOP,
                              fill=tk.BOTH,
                              expand=True)

        show_button = tk.Button(topranked_menu,
                                text="SHOW",
                                width=10,
                                height=2)
        show_button.bind("<Button-1>", self.toprank_handler)
        show_button.pack(side=tk.TOP,
                         fill=tk.BOTH,
                         expand=True)

        topranked_menu.pack(side=tk.TOP,
                             fill=tk.BOTH,
                             expand=True)

    def toprank_handler(self, event=None):
        """Timeseries handler"""
        for widget in self.information_display_frame.winfo_children():
            widget.destroy()

        year_selected = self.year_combobox.get()
        category_selected = self.tp_combobox.get()

        if year_selected and category_selected != "":
            if category_selected == "TOP SCORERS":
                key1 = year_selected
                key2 = "Player Names"
            elif category_selected == "TOP LEAGUES":
                key1 = year_selected
                key2 = "League"
        self.controller.get_top_ranked_values(key1, key2,
                                              self.information_display_frame)

    def comparing(self, event=None):
        """Comparing handler(in progress)"""
        pass

    def timeseries(self, event=None):
        """Trends of the top scorers and leagues."""


    def clearing_frame(self):
        """Clearing every widget in the frame"""
        for widget in self.information_menu_frame.winfo_children():
            widget.destroy()
        for widget in self.information_display_frame.winfo_children():
            widget.destroy()

    def run(self):
        """Run the application"""
        self.mainloop()
