from FSA_model import FootballScorersAnalyzerMODEL
from FSA_view import FootballScorersAnalyzerUI


class FootballScorersAnalyzerCONTROLLER:
    def __init__(self):
        self.model = FootballScorersAnalyzerMODEL()
        self.view = FootballScorersAnalyzerUI(self)

    def get_descriptive_statistics_keys(self):
        descriptive_keys = self.model.describe_data()
        return descriptive_keys

    def get_descriptive_statistics_values(self, key):
        return self.model.describe_data()[key]

    def get_distribution_values(self, key, display_frame):
        return self.model.get_distribution(key,
                                           self.view.information_display_frame)

    def get_correlation_values(self, key1, key2, display_frame):
        return self.model.get_correlation(key1, key2,
                                          self.view.information_display_frame)

    def get_top_ranked_values(self, key1, key2, display_frame):
        return self.model.get_top_ranked(key1, key2,
                                         self.view.information_display_frame)

    def run(self):
        self.view.run()
