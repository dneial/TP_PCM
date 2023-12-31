#!/usr/bin/env python3
import pandas as pd


def gen_software_fc(file, output):
    df = pd.read_csv(file)

    df2 = df["Market focus"].str.lower().str.get_dummies(",")

    df3 = df["Structure"].str.get_dummies(",")
    df4 = df["Language"].str.get_dummies(",")
    df.drop(
        ["License", "Windows", "Mac OS", "Linux", "Other Features"],
        axis=1,
        inplace=True,
    )
    df = pd.concat([df["Package"], df2, df3, df4], axis=1)

    df.replace("Yes", "1", inplace=True)
    df.replace("yes", "1", inplace=True)
    df.replace("ltd", "1", inplace=True)
    df.replace("No", "0", inplace=True)
    df.replace("no", "0", inplace=True)
    df.fillna("0", inplace=True)

    df.to_csv(output, index=False)


def gen_software2os(file, output):
    df = pd.read_csv(file)
    os_list = ["Package", "Windows", "Mac OS", "Linux"]

    cols_todrop = [col for col in df.columns if col not in os_list]
    df.drop(cols_todrop, axis=1, inplace=True)
    df.replace("Yes", "1", inplace=True)
    df.replace("No", "0", inplace=True)

    df.to_csv(output, index=False)


def gen_software2license(file, output):
    df = pd.read_csv(file)
    os_list = ["Package", "License"]
    cols_todrop = [col for col in df.columns if col not in os_list]
    df.drop(cols_todrop, axis=1, inplace=True)

    df = pd.get_dummies(df, columns=["License"], prefix="", prefix_sep="", dtype=int)
    df.rename(columns={"MPL derivative with badgeware clause": "MPL"}, inplace=True)
    df["GPL2"] = df["GPL2, other proprietary"] + df["GPL2"]
    df.drop("GPL2, other proprietary", axis=1, inplace=True)
    df.to_csv(output, index=False)


if __name__ == "__main__":
    import os

    cur_dir = os.getcwd()
    filep = "RawData/Accounting_Soft/Comparison_of_accounting_software_0_raw.csv"
    file = os.path.abspath(os.path.join(cur_dir, filep))
    output = "CleanedData/clean_soft.csv"
    output2 = "CleanedData/software2os.csv"
    output3 = "CleanedData/software2license.csv"

    gen_software_fc(file, output)
    gen_software2os(file, output2)
    gen_software2license(file, output3)
