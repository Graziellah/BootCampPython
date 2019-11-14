def proportionBySport(df, year, sport, gender):
All = df[(df['Year'] == year) & (df['Sex'] == gender)].drop_duplicates('Name').count()['Sex']
people = df[(df['Year'] == year) & (df['Sport'] == sport) & (df['Sex'] == gender)].drop_duplicates('Name').count()['Sex']
total = people/ All
return total