#!/bin/bash

clean_os_script="./clean_os.py"
clean_license_script="./clean_license.py"
clean_software_script="./clean_software.py"

clean_os_csv="../CleanedData/clean_os.csv"
clean_license_csv="../CleanedData/clean_license.csv"
clean_soft_csv="../CleanedData/clean_soft.csv"
software2license_csv="../CleanedData/software2license.csv"
software2os_csv="../CleanedData/software2os.csv"

results_ae_dir="../Results/results_ae"
results_hermes_dir="../Results/results_hermes"

rulebasis_software_dir="../Rulebasis/software"
rulebasis_os_dir="../Rulebasis/os"
rulebasis_license_dir="../Rulebasis/license"

# nettoyage des données
python3 "$clean_os_script"
python3 "$clean_license_script"
python3 "$clean_software_script"

# génération du fichier RCFT
java -jar fca4j.jar family softwaresRCFT.rcft -a IMPORT "$clean_os_csv" -n os -x CSV -s COMMA
java -jar fca4j.jar family softwaresRCFT.rcft -a IMPORT "$clean_license_csv" -n licenses -x CSV
java -jar fca4j.jar family softwaresRCFT.rcft -a IMPORT "$clean_soft_csv" -n softwares -x CSV
java -jar fca4j.jar family softwaresRCFT.rcft -a IMPORT "$software2license_csv" -n software2license -x CSV -v -s COMMA -op exist -source softwares -target licenses
java -jar fca4j.jar family softwaresRCFT.rcft -a IMPORT "$software2os_csv" -n software2os -x CSV -v -s COMMA -op exist -source softwares -target os

mkdir -p "$results_ae_dir"
mkdir -p "$results_hermes_dir"
mkdir -p "$rulebasis_software_dir"
mkdir -p "$rulebasis_os_dir"
mkdir -p "$rulebasis_license_dir"

# générer FCA
java -jar fca4j.jar RCA softwaresRCFT.rcft "$results_ae_dir" -v -a ADD_EXTENT
dot -Tpdf "$results_ae_dir/step2.dot" -o "$results_ae_dir/resultat.pdf"

# générer FCA avec l'algorithme HERMES
java -jar fca4j.jar RCA softwaresRCFT.rcft "$results_hermes_dir" -v -a HERMES -e
dot -Tpdf "$results_hermes_dir/step2.dot" -o "$results_hermes_dir/resultat_hermes.pdf"

# extraction des règles
java -jar fca4j.jar RULEBASIS "$clean_soft_csv" -i CSV -folder "$rulebasis_software_dir"
java -jar fca4j.jar RULEBASIS "$clean_os_csv" -i CSV -folder "$rulebasis_os_dir"
java -jar fca4j.jar RULEBASIS "$clean_license_csv" -i CSV -folder "$rulebasis_license_dir"
