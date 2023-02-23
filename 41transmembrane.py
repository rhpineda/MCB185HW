# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane

#---------------------------------------------------------------------------
import sys
import mcb185

def KD(seq): #Fxn gives total KD for whatever seq is inputted.
	totalkd = 0 
	aastring= 'IVLFCMAGTSWYPHEQDNKR'
	hydropathytup = (4.5, 4.2,3.8,2.8,2.5,1.9,1.8,-0.4,-0.7,-0.8\
	,-0.9,-1.3,-1.6,-3.2,-3.5,-3.5,-3.5,-3.5,-3.9,-4.5)
	for index in range(len(seq)): 
		index = aastring.find(seq[index]) 
		totalkd = totalkd + hydropathytup[index] 
	return(float(totalkd))
	
def hptest(seq): #Fxn tells if there is a signal and if there's a TM region
	signalseq = seq[:30] 
	tmseq = seq[30:]
	hassignal = False
	hastmregion = False
	
	#Signal test ->tests for KD and see if proline around test window/a-helix
	for i in range(len(signalseq)-8):
		if (KD(signalseq[i:i+8])) > 2.5 and 'P' not in signalseq[i-8:i+8]:
			hassignal = True
			break

	#TM test ->tests for KD and see if proline around test window/a-helix
	for i in range(len(tmseq)-11): 
		if (KD(tmseq[i:i+11])) > 2.0 and 'P' not in tmseq[i-11:i+11]:
			hastmregion = True
			break

	return(hassignal, hastmregion)	
	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if hptest(seq) == (True, True): #Prints only if both signal seq present
		print(defline)			  #and TM region present
	else:
		continue
#ALTERNATIVE WAY, ADD PARAMETERS TO HP TEST AND THEN ADD THE VALUES FOR KD 
#THRESHOLD AND LENGTH OF "WINDOW" OF WHAT'S READ
#---------------------------------------------------------------------------
"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
