import pandas as pd

class SpatioTemporalData:
    def __init__(self, df):
        self.df = df.copy()
    def when(self, location):
        return self.searchData('City', 'Year', location)
        All = self.df[(self.df['City'] == location)]
        print('alll',All)
        location = All['Year'].drop_duplicates().tolist()
        print(location)
        return location
    
    def where(self, location):
        return self.searchData('Year', 'City', location)

    def searchData(self,searchIn, searchFor, dataToSearch):
        All = self.df[(self.df[searchIn] == dataToSearch)]
        return All[searchFor].drop_duplicates().tolist()
        
# Test
# df = pd.read_csv('../ex00/athlete_events.csv', index_col=0)
# spaceTemp = SpatioTemporalData(df)
# print(spaceTemp.when('Athina'))
# print(spaceTemp.when('Paris'))
# print(spaceTemp.where(2016))