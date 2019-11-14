def howManyMedalsByCountry(df, country):
All = df[(df['Team'] == 'Finland')]
foo = All.groupby(['Event', 'Medal'])['Medal'].count().unstack().fillna(0)
data = foo.rename(columns={
        'Gold': 'G', 
        'Silver': 'S',
        'Bronze': 'B'
    }).astype({
        'G':int,
        'S': int,
        'B': int
    })
    return data