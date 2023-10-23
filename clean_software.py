#!/usr/bin/env python3
import pandas as pd


file = "Comparison_of_accounting_software_0_raw.csv"
df = pd.read_csv(file)

df_2 = pd.get_dummies(df, columns=['Market focus', 'Structure', 'Language'], dtype=int)
df_2.drop(["License", "Windows", "Mac OS", "Linux", "Other Features"], axis=1, inplace=True)


df_2.replace("Yes", "1", inplace=True)
df_2.replace("yes", "1", inplace=True)
df_2.replace("No", "0", inplace=True)
df_2.replace("no", "0", inplace=True)
df_2.fillna("0", inplace=True)

print(df_2.head())
# df_2.to_csv("clean.csv")
