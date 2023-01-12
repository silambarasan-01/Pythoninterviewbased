import pandas as pd

#create DataFrame

df = pd.DataFrame({'A': [4, 0, 3, 3, 6, 8, 7, 9, 12],
                   'B': [4, 2, 3, 5, 6, 4, 7, 7, 12],
                   'C': [4, 0, 3, 5, 5, 10, 7, 9, 12]})

#view DataFrame
#print(df)
#create new column that displays whether or not all column values match
df['all_matching'] = df.apply(lambda x: x.A == x.B == x.C, axis = 1)

#view updated DataFrame
print(df)