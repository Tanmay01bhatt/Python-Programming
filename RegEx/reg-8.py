# Lambda Implementation

import re

# Eg : Removing digits

# 1 - List: use map()

txt = ["hello123", "world456", "python789"]

clean = list(map(lambda x: re.sub(r"\d+", "", x), txt))

print(clean)


# 2 - Dataframe : use  apply()

import pandas as pd

df = pd.DataFrame({"text": ["hello123", "world456", "python789"]})

df["clean"] = df["text"].apply(lambda x: re.sub(r"\d+", "", x))

print(df)

# ectracting only alphabets

df["alphabets"] = df["text"].apply(lambda x: re.sub(r"[^a-zA-Z]", "", x))

print(df)
