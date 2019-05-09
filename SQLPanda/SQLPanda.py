import pandas as pd, sqlite3
class SQLDF:
    def __init__(self,path):
        self.c = sqlite3.connect(path).cursor()
    def q(self,query):
        self.c.execute(query)
        df = pd.DataFrame(self.c.fetchall())
        df.columns = [x[0] for x in self.c.description]
        return df
