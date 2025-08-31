import pandas as pd

try:
    print(pd.count_to_1000_divisible_by_7())
except AttributeError:
    print("Function not found")
