#!/usr/bin/env python3

import pandas as pd


def gen_licence_fc(file, output):
    df = pd.read_csv(file)

    # Licenses dans Soft :
    # Apache                                    ok
    # Apache License                            ok
    # GPL                                       ?
    # GPL2                                      ok
    # other proprietary                         ?
    # MPL derivative with badgeware clause      ok
    # AGPL                                      ok
    # CPAL                                      ?

    # Match dans licenses.csv :

    # "Apache License 2.0"                        Apache License

    # "GNU Lesser General Public License"         GPL
    # "GNU General Public License v2"             GPL2

    # "GNU Affero General Public License"         AGPL

    # "Mozilla Public License 2.0"                MPL

    # "Common Public License"                     CPAL

    li = [
        "Apache License 2.0",
        "GNU Lesser General Public License",
        "GNU General Public License v2",
        "GNU General Public License v3",
        "GNU Affero General Public License",
        "Mozilla Public License 2.0",
        "Common Public License",
    ]

    df = df[df["License and version"].isin(li)]

    features = [
        "FSF approval",
        "GPL (v3) compatibility",
        "OSI approval",
        "Copyfree approval",
        "Debian approval",
        "Fedora approval",
    ]

    # rennommage des noms pour correspondre à la table soft
    df.replace("Apache License 2.0", "Apache License", inplace=True)
    df.replace("GNU Lesser General Public License", "GPL", inplace=True)
    df.replace("GNU General Public License v2", "GPL2", inplace=True)
    df.replace("GNU General Public License v3", "GPL3", inplace=True)
    df.replace("GNU Affero General Public License", "AGPL", inplace=True)
    df.replace("Mozilla Public License 2.0", "MPL", inplace=True)
    df.replace("Common Public License", "CPAL", inplace=True)

    # rennommage des valeurs pour correspondre au format binaire demandé
    df.replace("Yes", 1, inplace=True)
    df.replace("Partial", 1, inplace=True)
    df.replace("No", 0, inplace=True)

    df.to_csv(output, index=False)


if __name__ == "__main__":
    import os

    cur_dir = os.getcwd()
    filep = "RawData/Licenses/Comparison_of_free_and_open-source_software_licenses_1_raw.csv"
    file = os.path.abspath(os.path.join(cur_dir, filep))
    output = "CleanedData/clean_license.csv"
    gen_licence_fc(file, output)
