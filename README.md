# zip2county
A python script that creates a dictionary for mapping 5-digit U.S. zip codes to county names. I had to do this mapping for my work and figured it might be a useful thing for other people out there who are interested. A mapping to FIPS codes should be straightforward from the county name.

## Summary 

The Python script uses the `.txt` file `zip_codes_county.txt` to initialize a dataframe and then create a dictionary. The dictionary stores 5-digit zip codes as keys and maps to string county names. The zip codes are stored as strings. The code outputs a **numpy** file `.npy` that holds the dictionary. This relies on the `numpy` package. 

Stored in the repository is the `.npy` file itself: `zip2county.npy`. To use it somewhere else in your code, you can load it easily with the `numpy` package like so:

```python
import numpy as np

# load in the dictionary
zip_code_dictionary = np.load('zip2county.npy`).item()

# use the dictionary

county = zip_code_dictionary['19104']
```
