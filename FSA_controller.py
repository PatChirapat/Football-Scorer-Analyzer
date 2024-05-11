from FSA_model import FootballScorersAnalyzerMODEL
from FSA_view import FootballScorersAnalyzerUI


class FootballScorersAnalyzerCONTROLLER:
    def __init__(self):
        """Initialize the controller with the model and view."""
        self.model = FootballScorersAnalyzerMODEL()
        self.view = FootballScorersAnalyzerUI(self)

    def get_descriptive_statistics_keys(self):
        """Get the keys for descriptive statistics."""
        descriptive_keys = self.model.describe_data()
        return descriptive_keys

    def get_descriptive_statistics_values(self, key):
        """Get the descriptive statistics values for a given key.

        Parameters:
            key (str): The key for which descriptive statistics values are needed.

        Returns:
            Series: The descriptive statistics values for the given key.
        """
        return self.model.describe_data()[key]

    def get_distribution_values(self, key, display_frame):
        """Get the distribution values for a given key and display it on a frame.

        Parameters:
            key (str): The key for which distribution is to be plotted.
            display_frame (tk.Frame): The frame where the graph will be displayed.

        Returns:
            FigureCanvasTkAgg: The canvas containing the plotted graph.
        """
        return self.model.get_distribution(key,
                                           self.view.information_display_frame)

    def get_correlation_values(self, key1, key2, display_frame):
        """Get the correlation values for two given keys and display it on a frame.

        Parameters:
            key1 (str): The first key for correlation.
            key2 (str): The second key for correlation.
            display_frame (tk.Frame): The frame where the graph will be displayed.

        Returns:
            FigureCanvasTkAgg: The canvas containing the plotted graph.
        """
        return self.model.get_correlation(key1, key2,
                                          self.view.information_display_frame)

    def get_top_ranked_values(self, key1, key2, display_frame):
        """Get the top ranked values for a given year and key, and display it on a frame.

        Parameters:
           key1 (str): The selected year.
           key2 (str): The attribute based on which top players are to be selected.
           display_frame (tk.Frame): The frame where the graph will be displayed.

        Returns:
            FigureCanvasTkAgg: The canvas containing the plotted graph.
        """
        return self.model.get_top_ranked(key1, key2,
                                         self.view.information_display_frame)

    def get_player(self):
        """Get the list of player names."""
        return self.model.get_player_names()

    def get_club(self):
        """Get the list of club names."""
        return self.model.get_club_names()

    def get_league(self):
        """Get the list of league names."""
        return self.model.get_league_names()

    def get_timeseries_values(self, key1, key2, key3, display_frame):
        """Get the time series values for a given key and display it on a frame.

        Parameters:
            key1 (str): Column attribute.
            key2 (str): Category for which time series will be plotted.
            key3 (str): Stat that will be plotted on the y-axis.
            display_frame (tk.Frame): The frame where the graph will be displayed.

        Returns:
            FigureCanvasTkAgg: The canvas containing the plotted graph.
        """
        return self.model.get_timeseries(key1, key2, key3,
                                         self.view.information_display_frame)

    def get_comparing_values(self, key1, key2, key3, key4, display_frame):
        """Get the comparing values for a given category and display it on a frame.

        Parameters:
            key1 (str): Category.
            key2 (str): First stat.
            key3 (str): Second stat.
            key4 (str): Wanted stat.
            display_frame (tk.Frame): The frame where the graph will be displayed.

        Returns:
            FigureCanvasTkAgg: The canvas containing the plotted graph.
        """
        return self.model.get_comparing(key1, key2, key3, key4,
                                        self.view.information_display_frame)

    def get_factors_affecting_goals(self,display_frame):
        return self.model.factors_affecting_goals(self.view.information_display_frame)

    def get_factors_correlation(self,key1, key2, display_frame):
        return self.model.factors_correlation(key1, key2,
                                                self.view.information_display_frame)

    def get_top10_scorers(self):
        return self.model.top10_scorers()

    def get_top10_stats(self, key1, key2, display_frame):
        return self.model.top10_stats(key1, key2,
                                        self.view.information_display_frame)

    def get_fac_top_ranked(self, key1, key2, display_frame):
        return self.model.fac_top_ranked(key1, key2,
                                         self.view.information_display_frame)

    def get_fac_comparing_values(self, key1, key2, display_frame):
        return self.model.fac_comparing_values(key1, key2,
                                        self.view.information_display_frame)

    def get_fac_timeseries_values(self, key1, key2, display_frame):
        return self.model.fac_timeseries_values(key1, key2,
                                         self.view.information_display_frame)

    def run(self):
        """Run the application."""
        self.view.run()
