#!/usr/bin/env python3

import pandas as pd


def gen_os_fc(file: str):
    df = pd.read_csv(file)

    oss = ["Linux", "Windows (NT family)", "Mac OS Classic"]
    df = df[df["Name"].isin(oss)]

    features = ["Name", "Computer architecture supported", "Kernel type", "File system supported"]

    cols_todrop = [col for col in df.columns if col not in features]
    df = df.drop(cols_todrop, axis=1)


    df2 = df["File system supported"].str.get_dummies(sep=",").add_prefix('fs_')
    df3 = df["Computer architecture supported"].str.get_dummies(sep=",").add_prefix('arch_')

    df.drop("File system supported", inplace=True, axis=1)
    df.drop("Computer architecture supported", inplace=True, axis=1)

    df = pd.get_dummies(df, columns=["Kernel type"], dtype=int)
    df = pd.concat([df, df2, df3], axis=1, join="inner")

    df.replace("Windows (NT family)", "Windows", inplace=True)
    df.replace("Mac OS Classic", "Mac OS", inplace=True)
    df.to_csv("./Cleaned/clean_os.csv", index=False)


if __name__ == "__main__":
    file = "./OS/Comparison_of_operating_systems_1_raw.csv"
    gen_os_fc(file)
