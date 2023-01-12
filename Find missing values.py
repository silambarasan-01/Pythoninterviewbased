import pandas as pd
import numpy as np

data={'name_col':[101,102,103,101,101,101,102,103],
      'val_col':['A',np.nan,'C','A',np.nan,np.nan,'B',np.nan]}
df=pd.DataFrame(data)
#print(df)
print('='*20)
for i in df['val_col'].index:
    if df['val_col'][i] is np.nan:
        df['val_col'][i] = df[df['name_col']==df['name_col'][i]]['val_col'].dropna().unique()[0]
        print(df)