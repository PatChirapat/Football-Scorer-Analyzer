import tkinter as tk
from tkinter import ttk


class FootballScorersAnalyzerUI(tk.Tk):
    def __init__(self, controller):
        """Initialize the UI with the controller."""
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
        """Welcome page"""
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

    def descriptive_stats_handler(self, event=None, year_select=None):
        """Display descriptive statistics handler"""
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
        """Display correlation statistics handler"""
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
        """Display distribution graph handler"""
        for widget in self.information_display_frame.winfo_children():
            widget.destroy()

        selected_index = event.widget.curselection()
        if selected_index:
            menu_selected = event.widget.get(selected_index[0])
            self.controller.get_distribution_values(menu_selected,
                                                    self.information_display_frame)

    def performance_trends_page(self, event=None):
        """Performance and trends page"""
        # clear previous frame
        self.clearing_frame()

        perf_trends_menu = tk.Frame(self.information_menu_frame)

        performance_button = tk.Button(perf_trends_menu,
                                      text="TOP OF THE RANKS",
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
        """Top of the ranks menu page"""
        # clear previous frame
        self.clearing_frame()

        year_list = ["2016", "2017", "2018", "2019", "2020"]
        topranked_list = ["TOP SCORERS",
                          "TOP LEAGUES",
                          "TOP CLUBS"]

        topranked_menu = tk.Frame(self.information_menu_frame)

        self.year_combobox = ttk.Combobox(topranked_menu,
                                          values=year_list)
        self.year_combobox.pack(side=tk.TOP,
                                fill=tk.BOTH,
                                expand=True)
        self.year_combobox.set("SELECT YEAR")

        self.tr_category_combobox = ttk.Combobox(topranked_menu,
                                                 values=topranked_list)
        self.tr_category_combobox.pack(side=tk.TOP,
                                       fill=tk.BOTH,
                                       expand=True)
        self.tr_category_combobox.set("SELECT CATEGORY")

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
        """Top Players and Leagues handler"""
        for widget in self.information_display_frame.winfo_children():
            widget.destroy()

        year_selected = self.year_combobox.get()
        category_selected = self.tr_category_combobox.get()

        if year_selected and category_selected != "":
            if category_selected == "TOP SCORERS":
                key1 = year_selected
                key2 = "Player Names"
            elif category_selected == "TOP LEAGUES":
                key1 = year_selected
                key2 = "League"
            elif category_selected == "TOP CLUBS":
                key1 = year_selected
                key2 = "Club"
        self.controller.get_top_ranked_values(key1, key2,
                                              self.information_display_frame)

    def comparing(self, event=None):
        """Comparing stats of top scorers and leagues"""
        # clear previous frame
        self.clearing_frame()

        comparing_menu = tk.Frame(self.information_menu_frame)

        comparing_list = ["PLAYER", "LEAGUE", "CLUB"]
        self.comparing_combobox = ttk.Combobox(comparing_menu,
                                            values=comparing_list)
        self.comparing_combobox.pack(side=tk.TOP,
                                fill=tk.BOTH,
                                expand=True)
        self.comparing_combobox.bind("<<ComboboxSelected>>", self.comparing_menu_update)
        self.comparing_combobox.set("SELECT CATEGORY")

        comparing_menu.pack(side=tk.TOP,
                            fill=tk.BOTH,
                            expand=True)

    def comparing_menu_update(self, event=None):
        """Update comparing menu"""
        selected_index = self.comparing_combobox.get()

        if hasattr(self, "player1_combobox"):
            self.player1_combobox.destroy()
        if hasattr(self, "player2_combobox"):
            self.player2_combobox.destroy()
        if hasattr(self, "league1_combobox"):
            self.league1_combobox.destroy()
        if hasattr(self, "league2_combobox"):
            self.league2_combobox.destroy()
        if hasattr(self, "club1_combobox"):
            self.club1_combobox.destroy()
        if hasattr(self, "club2_combobox"):
            self.club2_combobox.destroy()
        if hasattr(self, "wanted_combobox"):
            self.wanted_combobox.destroy()
        if hasattr(self, "show_button"):
            self.show_button.destroy()

        if selected_index == "PLAYER":
            player_names = self.controller.get_player()
            self.player1_combobox = ttk.Combobox(self.information_menu_frame,
                                                values=player_names)
            self.player1_combobox.bind("<<ComboboxSelected>>", self.comparing_wanted)
            self.player1_combobox.pack(side=tk.TOP,
                                    fill=tk.BOTH,
                                    expand=True)
            self.player1_combobox.set("SELECT FIRST PLAYER")

            self.player2_combobox = ttk.Combobox(self.information_menu_frame,
                                                values=player_names)
            self.player2_combobox.bind("<<ComboboxSelected>>", self.comparing_wanted)
            self.player2_combobox.pack(side=tk.TOP,
                                    fill=tk.BOTH,
                                    expand=True)
            self.player2_combobox.set("SELECT SECOND PLAYER")
        elif selected_index == "LEAGUE":
            league_names = self.controller.get_league()
            self.league1_combobox = ttk.Combobox(self.information_menu_frame,
                                            values=league_names)
            self.league1_combobox.bind("<<ComboboxSelected>>", self.comparing_wanted)
            self.league1_combobox.pack(side=tk.TOP,
                                    fill=tk.BOTH,
                                    expand=True)
            self.league1_combobox.set("SELECT FIRST LEAGUE")

            self.league2_combobox = ttk.Combobox(self.information_menu_frame,
                                            values=league_names)
            self.league2_combobox.bind("<<ComboboxSelected>>", self.comparing_wanted)
            self.league2_combobox.pack(side=tk.TOP,
                                    fill=tk.BOTH,
                                    expand=True)
            self.league2_combobox.set("SELECT SECOND LEAGUE2")
        elif selected_index == "CLUB":
            club_names = self.controller.get_club()
            self.club1_combobox = ttk.Combobox(self.information_menu_frame,
                                            values=club_names)
            self.club1_combobox.bind("<<ComboboxSelected>>", self.comparing_wanted)
            self.club1_combobox.pack(side=tk.TOP,
                                    fill=tk.BOTH,
                                    expand=True)
            self.club1_combobox.set("SELECT FIRST CLUB")

            self.club2_combobox = ttk.Combobox(self.information_menu_frame,
                                            values=club_names)
            self.club2_combobox.bind("<<ComboboxSelected>>", self.comparing_wanted)
            self.club2_combobox.pack(side=tk.TOP,
                                    fill=tk.BOTH,
                                    expand=True)
            self.club2_combobox.set("SELECT SECOND CLUB")

    def comparing_wanted(self, event=None):
        """Comparing wanted"""
        if hasattr(self, "wanted_combobox"):
            self.wanted_combobox.destroy()
        if hasattr(self, "show_button"):
            self.show_button.destroy()

        wanted_list = ["Matches Played", "Substitution", "Mins", "Goals",
                       "Expected Goals", "Expected Goals Per Avg Match",
                       "Shots", "On Target", "Shots Per Avg Match",
                       "On Target Per Avg Match"]
        self.wanted_combobox = ttk.Combobox(self.information_menu_frame,
                                            values=wanted_list)
        self.wanted_combobox.pack(side=tk.TOP,
                                fill=tk.BOTH,
                                expand=True)
        self.wanted_combobox.set("SELECT TOPIC")

        self.show_button = tk.Button(self.information_menu_frame,
                                    text="SHOW",
                                    width=10,
                                    height=2)
        self.show_button.bind("<Button-1>", self.comparing_handler)
        self.show_button.pack(side=tk.TOP,
                            fill=tk.BOTH,
                            expand=True)

    def comparing_handler(self, event=None):
        """Comparing handler"""
        for widget in self.information_display_frame.winfo_children():
            widget.destroy()

        selected_index = self.comparing_combobox.get()
        key4 = self.wanted_combobox.get()
        if selected_index == "PLAYER":
            key1 = "Player Names"
            key2 = self.player1_combobox.get()
            key3 = self.player2_combobox.get()
        elif selected_index == "LEAGUE":
            key1 = "League"
            key2 = self.league1_combobox.get()
            key3 = self.league2_combobox.get()
        elif selected_index == "CLUB":
            key1 = "Club"
            key2 = self.club1_combobox.get()
            key3 = self.club2_combobox.get()
        self.controller.get_comparing_values(key1, key2, key3, key4,
                                            self.information_display_frame)

    def timeseries(self, event=None):
        """Timeseries of top scorers and leagues"""
        # clear previous frame
        self.clearing_frame()

        ts_menu = tk.Frame(self.information_menu_frame)
        self.menu_combobox = ttk.Combobox(ts_menu,
                                    values=["PLAYER", "LEAGUE", "CLUB"])
        self.menu_combobox.bind("<<ComboboxSelected>>", self.timeseries_menu_update)
        self.menu_combobox.pack(side=tk.TOP,
                            fill=tk.BOTH,
                            expand=True)
        self.menu_combobox.set("SELECT CATEGORY")
        ts_menu.pack(side=tk.TOP,
                    fill=tk.BOTH,
                    expand=True)

    def timeseries_menu_update(self, event=None):
        """Update timeseries menu"""
        selected_index = self.menu_combobox.get()

        if hasattr(self, "player_combobox"):
            self.player_combobox.destroy()
        if hasattr(self, "league_combobox"):
            self.league_combobox.destroy()
        if hasattr(self, "club_combobox"):
            self.club_combobox.destroy()
        if hasattr(self, "ts_wanted_combobox"):
            self.ts_wanted_combobox.destroy()
        if hasattr(self, "ts_show_button"):
            self.ts_show_button.destroy()

        if selected_index == "PLAYER":
            player_names = self.controller.get_player()
            self.player_combobox = ttk.Combobox(self.information_menu_frame,
                                                values=player_names)
            self.player_combobox.bind("<<ComboboxSelected>>", self.timeseries_wanted)
            self.player_combobox.pack(side=tk.TOP,
                                    fill=tk.BOTH,
                                    expand=True)
            self.player_combobox.set("SELECT PLAYER")
        elif selected_index == "LEAGUE":
            league_names = self.controller.get_league()
            self.league_combobox = ttk.Combobox(self.information_menu_frame,
                                            values=league_names)
            self.league_combobox.bind("<<ComboboxSelected>>", self.timeseries_wanted)
            self.league_combobox.pack(side=tk.TOP,
                                    fill=tk.BOTH,
                                    expand=True)
            self.league_combobox.set("SELECT LEAGUE")
        elif selected_index == "CLUB":
            club_names = self.controller.get_club()
            self.club_combobox = ttk.Combobox(self.information_menu_frame,
                                            values=club_names)
            self.club_combobox.bind("<<ComboboxSelected>>", self.timeseries_wanted)
            self.club_combobox.pack(side=tk.TOP,
                                    fill=tk.BOTH,
                                    expand=True)
            self.club_combobox.set("SELECT CLUB")

    def timeseries_wanted(self, event=None):
        """Timeseries wanted"""
        if hasattr(self, "ts_wanted_combobox"):
            self.ts_wanted_combobox.destroy()
        if hasattr(self, "ts_show_button"):
            self.ts_show_button.destroy()

        wanted_list = ["Matches Played", "Substitution", "Mins", "Goals",
                       "Expected Goals", "Expected Goals Per Avg Match",
                       "Shots", "On Target", "Shots Per Avg Match",
                       "On Target Per Avg Match"]
        self.ts_wanted_combobox = ttk.Combobox(self.information_menu_frame,
                                               values=wanted_list)
        self.ts_wanted_combobox.pack(side=tk.TOP,
                                     fill=tk.BOTH,
                                     expand=True)
        self.ts_wanted_combobox.set("SELECT TIMESERIES TOPIC")

        self.ts_show_button = tk.Button(self.information_menu_frame,
                                text="SHOW",
                                width=10,
                                height=2)
        self.ts_show_button.bind("<Button-1>", self.timeseries_handler)
        self.ts_show_button.pack(side=tk.TOP,
                            fill=tk.BOTH,
                            expand=True)

    def timeseries_handler(self, event=None):
        """Timeseries handler"""
        for widget in self.information_display_frame.winfo_children():
            widget.destroy()

        selected_index = self.menu_combobox.get()
        key3 = self.ts_wanted_combobox.get()
        if selected_index == "PLAYER":
            key1 = "Player Names"
            key2 = self.player_combobox.get()
        elif selected_index == "LEAGUE":
            key1 = "League"
            key2 = self.league_combobox.get()
        elif selected_index == "CLUB":
            key1 = "Club"
            key2 = self.club_combobox.get()
        self.controller.get_timeseries_values(key1, key2, key3,
                                              self.information_display_frame)

    def clearing_frame(self):
        """Clearing every widget in the frame"""
        for widget in self.information_menu_frame.winfo_children():
            widget.destroy()
        for widget in self.information_display_frame.winfo_children():
            widget.destroy()

    def run(self):
        """Run the application"""
        self.mainloop()
