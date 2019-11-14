import pandas as pd 


class FileLoader:
    @staticmethod
    def load(path):
        df = pd.read_csv('athlete_events.csv', index_col=0)
        col, row = df.shape
        print('Loading dataset of dimensions', col ,'x', row)
        return df
    @staticmethod
    def display(df, n):
        if n >= 0:
            print(df.head(n))
        else:
            print(df.tail(abs(n)))

file = FileLoader()
df = file.load('athlete_events.csv')
file.display(df, -2)