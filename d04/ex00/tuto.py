import pandas as pd 

#data = {
##   'apples': [3, 2, 0, 1],
#    'oranges': [1, 6, 9, 3],
#}

#purchase = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])

#print(purchase)
#print(purchase.loc['June'])

df = pd.read_csv('athlete_events.csv', index_col=0)
#df = df.drop_duplicates('Sport')
#yea = df[(df['Name'] ==  'Kjetil Andr Aamodt')]
#test = df['Year']
#yea.loc['Year']
#All = df[(df['Games'] ==  'Athina')]
All = df[(df['Team'] == 'Finland')]
#fo = All['City'].drop_duplicates().tolist()
#foo = All['Year']
#s = foo.ix[:,0]
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
#foo = pd.Categorical(['Year'], categories=['Year'])
#bar = pd.Categorical(['Medal'], categories=['Medal'])
#d = df.crosstab(foo, bar)
#subset = All[['Year', 'Medal']]
#female = df[(df['Year'] == 2004) & (df['Sport'] == "Tennis") & (df['Sex'] == 'F')].drop_duplicates('Name').count()['Sex']
#male = df[(df['Year'] == 2004) & (df['Sex'] == "M")].min()
#data = {'F': female['Age'], 'M': male['Age']}
#total = (female)/ All
#print(df[(df['Year'] == 2016) & (df['Sport'] == "Tennis") & (df['Sex'] == 'F')].drop_duplicates('Name'))
#print(All)
# print("==============\n", yea)
# print("******************\n", test)
# print("+++++++++++++++++\n",subset)
print("#####################\n", All)
print("#####################\n", foo)
print("#####################\n", data)
print("#####################\n", data.to_dict('index'))

