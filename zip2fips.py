import pandas as pd
import numpy as np

# read in text file
csv = pd.read_table('zip_code_county.txt', converters={'zip_code': lambda x: str(x)})

csv = csv[['zip_code','county']]

# format
csv.index = csv['zip_code']
csv = csv[['county']]
csv.fillna("-999", inplace=True)

csv.sort_values('county')

# make dictionary 
zip2fip = csv.to_dict()['county']

# save
np.save('zip2fip.npy', zip2fip)

# test
print zip2fip['19104']

