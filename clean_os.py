#!/usr/bin/env python3

import pandas as pd

file = "./Comparison_of_operating_systems_1/Comparison_of_operating_systems_1_raw.csv"
df = pd.read_csv(file)

oss = ["Linux", "Windows (NT family)", "Mac OS Classic"]
df = df[df["Name"].isin(oss)]

features = ["Computer architecture supported", "Kernel type", "File system supported"]

cols_todrop = [col for col in df.columns if col not in features]
print(cols_todrop)
df = df.drop(cols_todrop, axis=1)

df = pd.get_dummies(df, columns=features, dtype=int)
# df = df.drop(df.columns[df.apply(lambda n: not n.isin(features))], axis=1)


print(df.head())
df.to_csv("./Cleaned/clean_os.csv")
