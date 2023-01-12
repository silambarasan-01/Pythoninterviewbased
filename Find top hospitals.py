import pandas as pd

# Define a dictionary containing employee data
data = {'Hospital_Name': ["abc","def","ghk","lmn","opk"],
        'Available_beds': [1, 5, 2, 0, 7],
        'Location': ["CH", "MU", "DH","PU","OD"]
        }

df = pd.DataFrame(data)
#df.nlargest(3, ['Available_beds'])
print(df.nlargest(3, ['Available_beds']))
