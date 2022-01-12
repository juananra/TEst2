import pandas as pd

class RadExcelFile(object):

    def __init__(self, name):
        self.name = name

    def Read(self):
        df = pd.read_excel(self.name)
        return df