def howManyMedals(df, name):
    df = pd.read_csv('athlete_events.csv', index_col=0)
    All = df[(df['Name'] ==  'Kjetil Andr Aamodt')].fillna(0)
    foo = All.groupby(by=['Year', 'Medal'])['Medal'].count().unstack().fillna(0).drop(0 , axis='columns')
    data = foo.rename(columns={
        'Gold': 'G', 
        'Silver': 'S',
        'Bronze': 'B'
    }).astype({
        'G':int,
        'S': int,
        'B': int
    })
    return data.to_dict('index')