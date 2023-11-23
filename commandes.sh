java -jar fca4j.jar family softwaresRCFT.rcft -a IMPORT Cleaned/clean_os.csv -n os -x CSV -s COMMA;
java -jar fca4j.jar family softwaresRCFT.rcft -a IMPORT Cleaned/clean_license.csv -n licenses -x CSV;
java -jar fca4j.jar family softwaresRCFT.rcft -a IMPORT Cleaned/clean_soft.csv -n softwares -x CSV;
java -jar fca4j.jar family softwaresRCFT.rcft -a IMPORT Cleaned/software2license.csv -n software2license -x CSV -v -s COMMA -op exist -source softwares -target licenses;
java -jar fca4j.jar family softwaresRCFT.rcft -a IMPORT Cleaned/software2os.csv -n software2os -x CSV -v -s COMMA -op exist -source softwares -target os;

mkdir results_ae;
java -jar fca4j.jar RCA softwaresRCFT.rcft ./results_ae -v -a ADD_EXTENT;
dot -Tpdf results_ae/step2.dot -o results_ae/resultat.pdf;

mkdir results_hermes;
java -jar fca4j.jar RCA softwaresRCFT.rcft ./results_hermes -v -a HERMES -e;
dot -Tpdf results_hermes/step2.dot -o results_hermes/resultat_hermes.pdf;

mkdir rules/software2os;
java -jar fca4j.jar RULEBASIS Cleaned/software2os.csv -i CSV -folder ./rules/software2os;

mkdir rules/software2license;
java -jar fca4j.jar RULEBASIS Cleaned/software2license.csv -i CSV -folder ./rules/software2license;
