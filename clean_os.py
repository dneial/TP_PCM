#!/usr/bin/env python3

import pandas as pd

file = "./Comparison_of_operating_systems_1/Comparison_of_operating_systems_1_raw.csv"
df = pd.read_csv(file)

oss = ["Linux", "Windows (NT family)", "Mac OS Classic"]
df = df[df["Name"].isin(oss)]

features = ["Name", "Computer architecture supported", "Kernel type", "File system supported"]

cols_todrop = [col for col in df.columns if col not in features]
df = df.drop(cols_todrop, axis=1)

df2 = df["File system supported"].str.get_dummies(sep=",")
df3 = df["Computer architecture supported"].str.get_dummies(sep=",")

df.drop("File system supported", inplace=True, axis=1)
df.drop("Computer architecture supported", inplace=True, axis=1)

df = pd.get_dummies(df, columns=["Kernel type"], dtype=int)
df = pd.concat([df, df2, df3], axis=1, join="inner")

df.replace("Windows (NT family)", "Windows", inplace=True)
df.replace("Mac OS Classic", "Mac OS", inplace=True)
df.to_csv("./Comparison_of_operating_systems_1/clean_os.csv", index=False)
