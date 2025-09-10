import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.default_rng(2).integers(0, 2, (4, 4)),
    columns=["a", "b", "c", "d"],
)

try:
    df["gr"] = df.groupby(["b", "c"]).count()
except ValueError as e:
    print(e)
