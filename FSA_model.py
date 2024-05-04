import pandas as pd

class FootballScorersAnalyzerMODEL:
    def __init__(self):
        self.df = pd.read_csv("Football_Scoreres_Analyzer.csv")

    def describe_data(self):
        if "Year" in self.df.columns:
            return self.df.drop(columns=["Year"]).select_dtypes(include=['int64', 'float64']).describe()
        else:
            return self.df.select_dtypes(include=['int64', 'float64']).describe()

