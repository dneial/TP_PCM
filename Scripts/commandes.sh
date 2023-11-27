python3 ./clean_os.py;
python3 ./clean_license.py;
python3 ./clean_software.py;

java -jar fca4j.jar family softwaresRCFT.rcft -a IMPORT ../CleanedData/clean_os.csv -n os -x CSV -s COMMA;
java -jar fca4j.jar family softwaresRCFT.rcft -a IMPORT ../CleanedData/clean_license.csv -n licenses -x CSV;
java -jar fca4j.jar family softwaresRCFT.rcft -a IMPORT ../CleanedData/clean_soft.csv -n softwares -x CSV;
java -jar fca4j.jar family softwaresRCFT.rcft -a IMPORT ../CleanedData/software2license.csv -n software2license -x CSV -v -s COMMA -op exist -source softwares -target licenses;
java -jar fca4j.jar family softwaresRCFT.rcft -a IMPORT ../CleanedData/software2os.csv -n software2os -x CSV -v -s COMMA -op exist -source softwares -target os;

mkdir ../Results/results_ae;
java -jar fca4j.jar RCA softwaresRCFT.rcft ../Results/results_ae -v -a ADD_EXTENT;
dot -Tpdf ../Results/results_ae/step2.dot -o ../Results/results_ae/resultat.pdf;

mkdir ../Results/results_hermes;
java -jar fca4j.jar RCA softwaresRCFT.rcft ../Results/results_hermes -v -a HERMES -e;
dot -Tpdf ../Results/results_hermes/step2.dot -o ../Results/results_hermes/resultat_hermes.pdf;

mkdir ../Rulebasis/software;
java -jar fca4j.jar RULEBASIS ../CleanedData/clean_soft.csv -i CSV -folder ../Rulebasis/software;

mkdir ../Rulebasis/os;
java -jar fca4j.jar RULEBASIS ../CleanedData/clean_os.csv -i CSV -folder ../Rulebasis/os;

mkdir ../Rulebasis/license;
java -jar fca4j.jar RULEBASIS ../CleanedData/clean_license.csv -i CSV -folder ../Rulebasis/license;

