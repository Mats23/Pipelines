import sys
import os
#script para fazer downloads automaticos de datasets
#https://trace.ncbi.nlm.nih.gov/Traces/study/?acc=SRP069976
#link para as pastas dos datasets ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR316/
i= 2
#o laco percorre todas as pastas buscando os 35 arquivos SRR 
for t in range(42,76):
	link = 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR316/00'+ str(i) +'/SRR31628'+str(t)+'/SRR31628'+str(t)+'_1.fastq.gz'
	os.system("wget" + " "+ link)
	link = 'ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR316/00'+ str(i) +'/SRR31628'+str(t)+'/SRR31628'+str(t)+'_2.fastq.gz'
	os.system("wget" + " "+ link)
	
	i +=1
	if (i==9):
		i = 0