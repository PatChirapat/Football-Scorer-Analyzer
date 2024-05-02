from FSA_model import FootballScorersAnalyzerMODEL
from FSA_ui import FootballScorersAnalyzerUI

class FootballScorersAnalyzerCONTROLLER:
    def __init__(self):
        self.model = FootballScorersAnalyzerMODEL()
        self.view = FootballScorersAnalyzerUI(self)

    def run(self):
        self.view.run()
