#!/usr/bin/env python3
import pandas as pd


file = "./Accounting_Soft/Comparison_of_accounting_software_0_raw.csv"
df = pd.read_csv(file)

df2 = df["Market focus"].str.get_dummies(",")
df3 = df["Structure"].str.get_dummies(",")
df4 = df["Language"].str.get_dummies(",")

df.drop(["License", "Windows", "Mac OS", "Linux", "Other Features"], axis=1, inplace=True)
df = pd.concat([df["Package"], df2, df3, df4], axis=1)


df.replace("Yes", "1", inplace=True)
df.replace("yes", "1", inplace=True)
df.replace("ltd", "1", inplace=True)
df.replace("No", "0", inplace=True)
df.replace("no", "0", inplace=True)
df.fillna("0", inplace=True)

df.to_csv("Cleaned/cleanSoft.csv", index=False)
